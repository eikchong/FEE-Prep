import pymupdf
import pytest

from utils import library


def make_pdf(path, pages):
    doc = pymupdf.open()
    for text in pages:
        pg = doc.new_page()
        pg.insert_textbox(pymupdf.Rect(50, 50, 550, 800), text, fontsize=11)
    path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(path)


FILLER = "General introduction to the course and assessment arrangements for the semester."


@pytest.fixture
def lib(tmp_path):
    mats = tmp_path / "materials"
    make_pdf(mats / "CE202" / "steel_notes.pdf", [
        FILLER,
        "Lateral torsional buckling of unrestrained beams. Compute M_cr and the reduction factor chi_LT "
        "using clause 6.3.2. Lateral-torsional buckling governs long unrestrained spans.",
        "Bolted connections: shear resistance per bolt Fv,Rd from Table 3.4 of EN 1993-1-8. Fillet weld design.",
    ])
    make_pdf(mats / "CE201" / "CE201-10_slender-columns.pdf", ["Second order effects in columns.", "More text."])
    (mats / "_general").mkdir(parents=True)
    (mats / "_general" / "manning.txt").write_text("Manning equation for uniform flow, normal depth and "
                                                    "hydraulic radius. Manning n values for concrete.")
    con = library.connect(tmp_path / "lib.db")
    rep = library.ingest(mats, con)
    yield mats, con, rep
    con.close()


def test_ingest_and_search_correct_page(lib):
    mats, con, rep = lib
    assert len(rep.added) == 3 and not rep.failed
    hits = library.search(con, "lateral torsional")
    assert hits and hits[0]["path"] == "CE202/steel_notes.pdf" and hits[0]["page_no"] == 2
    hits = library.search(con, "Table 3.4")
    assert hits[0]["page_no"] == 3
    assert "**" in hits[0]["snippet"]


def test_auto_tagging(lib):
    mats, con, _ = lib
    tags = {t["topic_id"] for t in library.page_tags(con, "CE202/steel_notes.pdf", 2)}
    assert "CE202-06" in tags
    tags3 = {t["topic_id"] for t in library.page_tags(con, "CE202/steel_notes.pdf", 3)}
    assert "CE202-10" in tags3
    assert not library.page_tags(con, "CE202/steel_notes.pdf", 1)
    # filename prefix forces the sub-topic on every page
    for pg in (1, 2):
        assert "CE201-10" in {t["topic_id"] for t in library.page_tags(con, "CE201/CE201-10_slender-columns.pdf", pg)}
    # _general folder: no subject restriction
    assert "CE205-04" in {t["topic_id"] for t in library.page_tags(con, "_general/manning.txt", 1)}


def test_filters(lib):
    _, con, _ = lib
    assert {h["path"] for h in library.search(con, "", topic_id="CE202-06")} == {"CE202/steel_notes.pdf"}
    # subject filter includes _general pages tagged to that subject
    paths = {h["path"] for h in library.search(con, "manning", code="CE205")}
    assert paths == {"_general/manning.txt"}


def test_manual_tags_override_and_survive_rescan(lib):
    mats, con, _ = lib
    p = "CE202/steel_notes.pdf"
    library.set_page_tags(con, p, 2, ["CE202-03"])            # remove auto CE202-06, add CE202-03
    assert {t["topic_id"] for t in library.page_tags(con, p, 2)} == {"CE202-03"}
    # modify file → re-ingest; manual decisions persist
    make_pdf(mats / "CE202" / "steel_notes.pdf", [FILLER, "Lateral torsional buckling again lateral torsional.", "x"])
    rep = library.ingest(mats, con)
    assert rep.updated == [p]
    assert {t["topic_id"] for t in library.page_tags(con, p, 2)} == {"CE202-03"}


def test_incremental_and_deletion(lib):
    mats, con, _ = lib
    rep = library.ingest(mats, con)
    assert len(rep.skipped) == 3 and not rep.added
    (mats / "_general" / "manning.txt").unlink()
    rep = library.ingest(mats, con)
    assert rep.removed == ["_general/manning.txt"]
    assert not library.search(con, "manning")


def test_new_file_searchable_after_rescan(lib):
    mats, con, _ = lib
    make_pdf(mats / "CE203" / "piles.pdf", ["Pile shaft friction and end bearing; negative skin friction."])
    library.ingest(mats, con)
    h = library.search(con, "negative skin friction")
    assert h and h[0]["path"] == "CE203/piles.pdf" and h[0]["page_no"] == 1
    assert "CE203-07" in {t["topic_id"] for t in library.page_tags(con, "CE203/piles.pdf", 1)}


def test_coverage_gaps(lib):
    _, con, rep = lib
    assert "CE202-06" not in rep.gaps
    assert "CE206-08" in rep.gaps
    assert set(rep.gaps) == set(library.coverage_gaps(con))


def test_bad_query_does_not_crash(lib):
    _, con, _ = lib
    library.search(con, 'M_cr (6.3.2) "')
    library.search(con, "AND OR")


def test_past_papers_use_index_tags_and_skip_coverage(tmp_path):
    mats = tmp_path / "materials"
    # a "brochure" page listing many syllabus names must NOT tag everything
    make_pdf(mats / "_past_papers" / "FEE2026_booklet.pdf",
             ["Syllabus: lateral torsional buckling, Manning uniform flow, consolidation, activated sludge"] * 13)
    con = library.connect(tmp_path / "pp.db")
    library.ingest(mats, con)
    p = "_past_papers/FEE2026_booklet.pdf"
    assert not library.page_tags(con, p, 1)                         # syllabus page: no tags
    assert "CE102-04" in {t["topic_id"] for t in library.page_tags(con, p, 12)}   # indexed Q3 truss
    assert library.topic_page_counts(con) == {}                     # excluded from coverage
    assert library.topic_page_counts(con, include_past=True)
    con.close()

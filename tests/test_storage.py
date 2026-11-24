from utils.storage import JsonStorage


def test_roundtrip_survives_restart(tmp_path):
    s = JsonStorage(tmp_path / "progress.json")
    d = s.load()
    d["topics"]["CE201-02"] = {"status": "Revised", "confidence": 4, "notes": "K' check"}
    d["settings"]["weekday_hours"] = 3
    s.save(d)
    d2 = JsonStorage(tmp_path / "progress.json").load()   # "restart"
    assert d2["topics"]["CE201-02"]["confidence"] == 4
    assert d2["settings"]["weekday_hours"] == 3
    assert d2["settings"]["part2_core"]          # defaults merged in
    assert d2["mcq_attempts"] == []


def test_corrupt_file_is_preserved(tmp_path):
    p = tmp_path / "progress.json"
    p.write_text("{not json")
    d = JsonStorage(p).load()
    assert d["topics"] == {}
    assert (tmp_path / "progress.corrupt.json").exists()

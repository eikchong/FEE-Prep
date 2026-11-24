"""Scan materials/ into data/library.db and print a coverage report.

    python scripts/ingest.py            # incremental
    python scripts/ingest.py --rebuild  # drop the index (manual tags are kept)
"""
from __future__ import annotations

import argparse
import sys
from contextlib import closing
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import library  # noqa: E402
from utils.syllabus import topic_label  # noqa: E402


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--rebuild", action="store_true", help="re-extract every file")
    args = ap.parse_args(argv)
    with closing(library.connect()) as con:
        if args.rebuild:
            con.execute("UPDATE documents SET hash=''")
            con.commit()
        rep = library.ingest(con=con, progress_cb=lambda f, name: print(f"  [{f:4.0%}] {name}"))
        print("\n" + rep.summary())
        for path, err in rep.failed:
            print(f"  FAILED {path}: {err}")
        if rep.ocr_missing:
            print(f"  {rep.ocr_missing} scanned page(s) had no text — install Tesseract for OCR.")
        print(f"\nCoverage report — {len(rep.gaps)} sub-topic(s) with no linked material:")
        for tid in rep.gaps:
            print(f"  · {topic_label(tid)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Hard-coded exam facts and app-wide constants for FEE 2027 (Civil)."""
from datetime import date, time
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent
DATA_DIR = Path(os.environ.get("FEE_DATA_DIR", ROOT / "data"))
MATERIALS_DIR = Path(os.environ.get("FEE_MATERIALS_DIR", ROOT / "materials"))
STATIC_DATA_DIR = ROOT / "data"  # syllabus, banks, reading list ship with the repo

EXAM_DATE = date(2027, 1, 6)
RESULTS = "April 2027 (Pass/Fail only)"
BROCHURE_URL = "https://file.go.gov.sg/fee2027brochure.pdf"
PEB_URL = "https://www.peb.gov.sg"

PART1 = {
    "name": "Part 1 — Breadth",
    "start": time(9, 0), "end": time(12, 10),
    "duration": "3 h 10 min (incl. 10 min reading)",
    "questions": 40, "answer": 40, "fmt": "MCQ, answer all",
    "minutes": 180, "pace_min": 4.5,
}
PART2 = {
    "name": "Part 2 — Depth",
    "start": time(14, 0), "end": time(17, 10),
    "duration": "3 h 10 min (incl. 10 min reading)",
    "questions": 9, "answer": 5, "fmt": "Long questions, answer 5 of 9",
    "minutes": 180, "pace_min": 36,
}
PART2_ALLOCATION = {"CE201": 2, "CE202": 2, "CE203": 2, "CE204": 1, "CE205": 1, "CE206": 1}
PART1_CODES = ["CE101", "CE102", "CE103", "CE104", "CE105"]
PART2_CODES = list(PART2_ALLOCATION)

CODES_RULE = ("Only Eurocodes (SS EN) and the relevant Singapore National Annexes are accepted. "
              "AASHTO is accepted for transportation (CE204).")
OPEN_BOOK = "Open book. Design aids (charts/tables) may be provided in some questions."

COLOR_P1 = "#2a78d6"
COLOR_P2 = "#eb6834"
PART_COLORS = {1: COLOR_P1, 2: COLOR_P2, "Part 1": COLOR_P1, "Part 2": COLOR_P2}

STATUSES = ["Not started", "Learning", "Revised", "Exam-ready"]

DEFAULT_SETTINGS = {
    "part2_core": ["CE201", "CE201", "CE202", "CE202", "CE203"],
    "part2_backup": ["CE203"],
    "weekday_hours": 2.5,
    "weekend_hours": 6.0,
    "plan_start": None,  # ISO date; None → today
}

# Planner weights
PART1_SUBJECT_WEIGHT = 1.0
PART2_SLOT_WEIGHT = 1.0
PART2_BACKUP_WEIGHT = 0.5
CONFIDENCE_FLOOR = 0.2
MCQ_BLOCK_MIN = 30
MOCK_DAYS = 7

# Part 2 self-marking rubric: criterion -> weight (%)
RUBRIC = {
    "Method / approach": 40,
    "Code clause cited": 15,
    "Units & notation": 10,
    "Sketch / diagram": 10,
    "Final answer": 25,
}

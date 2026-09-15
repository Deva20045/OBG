#!/usr/bin/env python3
"""Validate PULSE OBG's standalone app and structured chapter source artifacts."""
from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
APP_PATH = ROOT / "pulse-obg.html"
DATA_DIR = ROOT / "data"

# Book-page scope, exact titles, and intended content volume for every live chapter.
LIVE_CHAPTERS = {
    1: ("Fundamentals of Reproduction", 265, 301, 235, 28),
    2: ("Normal Pregnancy and Antenatal Care", 302, 326, 107, 18),
    3: ("Fetal Assessment and Ultrasound", 327, 339, 61, 12),
    4: ("Fetal Surveillance and Maternal Adaptations", 340, 357, 65, 15),
    5: ("Medical Disorders: Anemia, Drugs and Heart Disease", 358, 374, 70, 18),
    6: ("Thyroid, Diabetes & Shoulder Dystocia", 375, 389, 180, 25),
    7: ("Pregnancy-Induced Hypertension", 390, 401, 125, 16),
    8: ("Eclampsia, Liver Disorders & Rh-Negative Pregnancy", 402, 417, 224, 31),
    9: ("Abortion, Recurrent Loss & MTP", 418, 427, 158, 22),
    10: ("MTP, Ectopic Pregnancy & Gestational Trophoblastic Disease", 428, 441, 228, 28),
}

REQUIRED_UI = [
    '<div id="home">', '<div id="chapters" class="hidden">',
    '<div id="path" class="hidden">', '<div id="guide" class="hidden">',
    '<div id="quiz" class="hidden">', '<div id="unitdone" class="hidden">',
    'id="hStreak"', 'id="hXP"', 'id="sXP"', 'id="sStreak"', 'id="sUnits"',
    'id="chList"', 'id="nodes"', 'id="qbar"', 'id="qtag"', 'id="qtext"',
    'id="opts"', 'id="fb"', 'id="nextBtn"', 'id="dScore"', 'id="dXP"',
    'id="dAcc"', 'id="dRev"', 'continueLearning()', 'unlockAll()', 'beginUnit()',
    'renderQ()', 'answer(o,btn)', 'finishUnit()', 'shuffle(a)',
]


def extract_json(html: str, name: str, next_name: str | None = None) -> object:
    """Extract one JSON array assigned to a top-level JS const."""
    tail = f";\\nconst {next_name}" if next_name else ";"
    match = re.search(rf"const {name} = (\[[\s\S]*?\]){tail}", html)
    if not match:
        raise ValueError(f"Could not extract {name} from {APP_PATH.name}")
    return json.loads(match.group(1))


def check_javascript_syntax(html: str, errors: list[str]) -> None:
    scripts = re.findall(r"<script>([\s\S]*?)</script>", html)
    if len(scripts) != 1:
        errors.append(f"Expected exactly one inline script, found {len(scripts)}")
        return
    temp_name = ""
    try:
        with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as temp:
            temp.write(scripts[0])
            temp_name = temp.name
        result = subprocess.run(
            ["node", "--check", temp_name], text=True, capture_output=True, check=False
        )
        if result.returncode:
            errors.append("JavaScript syntax check failed: " + result.stderr.strip())
    except FileNotFoundError:
        errors.append("Node.js is unavailable, so JavaScript syntax was not checked")
    finally:
        if temp_name:
            Path(temp_name).unlink(missing_ok=True)


def verify() -> None:
    html = APP_PATH.read_text(encoding="utf-8")
    errors: list[str] = []

    for element in REQUIRED_UI:
        if element not in html:
            errors.append(f"Missing UI element/function: {element}")

    try:
        questions = extract_json(html, "QUESTIONS", "UNITS")
        units = extract_json(html, "UNITS", "CHAPTERS")
        chapters = extract_json(html, "CHAPTERS")
    except (ValueError, json.JSONDecodeError) as exc:
        print(f"FAILED: {exc}")
        sys.exit(1)

    print(f"Verified extraction: {len(questions)} questions, {len(units)} units, {len(chapters)} chapters.")

    if len(chapters) != 24:
        errors.append(f"Expected 24 roadmap chapters, found {len(chapters)}")
    chapter_numbers = [chapter.get("n") for chapter in chapters]
    if chapter_numbers != list(range(1, 25)):
        errors.append("Roadmap chapter numbers must be a unique contiguous sequence from 1 through 24")

    metadata = {chapter.get("n"): chapter for chapter in chapters}
    for number, (title, first_page, _last_page, expected_qs, expected_units) in LIVE_CHAPTERS.items():
        entry = metadata.get(number, {})
        if not entry.get("live"):
            errors.append(f"Chapter {number} should be marked live")
        if entry.get("t") != title:
            errors.append(f"Chapter {number} title mismatch: {entry.get('t')!r}")
        if entry.get("p") != first_page:
            errors.append(f"Chapter {number} roadmap page should be {first_page}, got {entry.get('p')}")
        # This makes accidental partial generation or duplicate appends fail loudly.
        if expected_qs < 1 or expected_units < 1:
            errors.append(f"Invalid expected content count configured for Chapter {number}")
    for number in range(11, 25):
        if metadata.get(number, {}).get("live"):
            errors.append(f"Future Chapter {number} should remain marked Soon")

    question_ids = [question.get("id") for question in questions]
    if len(question_ids) != len(set(question_ids)):
        errors.append("Question IDs are not globally unique")
    unit_ids = [unit.get("id") for unit in units]
    if len(unit_ids) != len(set(unit_ids)):
        errors.append("Unit IDs are not globally unique")
    normalized_stems: dict[str, str] = {}
    for question in questions:
        stem = question.get("q", "")
        normalized = re.sub(r"\s+", " ", stem).strip().casefold()
        if normalized and normalized in normalized_stems:
            errors.append(
                f"Duplicate question stem: {question.get('id')} and {normalized_stems[normalized]}"
            )
        elif normalized:
            normalized_stems[normalized] = question.get("id", "")

    qs_by_ch: dict[int, list[dict]] = {}
    q_by_id: dict[str, dict] = {}
    for question in questions:
        qid = question.get("id", "")
        match = re.fullmatch(r"OBG-C(\d+)-(\d{3})", qid)
        if not match:
            errors.append(f"Invalid question ID format: {qid!r}")
            continue
        number = int(match.group(1))
        qs_by_ch.setdefault(number, []).append(question)
        q_by_id[qid] = question

        for key in ("sec", "q", "exp"):
            if not isinstance(question.get(key), str) or not question[key].strip():
                errors.append(f"{qid}: missing/non-text {key}")
        if not isinstance(question.get("page"), int):
            errors.append(f"{qid}: page must be an integer")
        options = question.get("opts")
        if not isinstance(options, list) or len(options) != 4:
            errors.append(f"{qid}: expected exactly 4 options")
        elif any(not isinstance(option, str) or not option.strip() for option in options):
            errors.append(f"{qid}: options must be non-empty text")
        elif len({option.strip().casefold() for option in options}) != 4:
            errors.append(f"{qid}: options must be distinct")
        answer = question.get("ans")
        if isinstance(answer, bool) or not isinstance(answer, int) or not 0 <= answer <= 3:
            errors.append(f"{qid}: invalid answer index {answer!r}")

    unexpected_question_chapters = sorted(set(qs_by_ch) - set(LIVE_CHAPTERS))
    if unexpected_question_chapters:
        errors.append(f"Questions found in non-live chapters: {unexpected_question_chapters}")

    page_coverage: dict[int, set[int]] = {}
    for number, (title, first_page, last_page, expected_qs, _expected_units) in LIVE_CHAPTERS.items():
        chapter_questions = qs_by_ch.get(number, [])
        if len(chapter_questions) != expected_qs:
            errors.append(
                f"Chapter {number}: expected {expected_qs} questions, found {len(chapter_questions)}"
            )
        for index, question in enumerate(chapter_questions, 1):
            expected_id = f"OBG-C{number}-{index:03d}"
            qid = question.get("id")
            if qid != expected_id:
                errors.append(f"Chapter {number} question {index}: expected {expected_id}, got {qid}")
            page = question.get("page")
            if isinstance(page, int):
                page_coverage.setdefault(number, set()).add(page)
                if not first_page <= page <= last_page:
                    errors.append(f"{qid}: Book p{page} outside Chapter {number} range {first_page}–{last_page}")
            explanation = question.get("exp", "")
            page_match = re.search(r"\(Book p(\d+)\)$", explanation)
            if not page_match:
                errors.append(f"{qid}: explanation must end with '(Book pX)'")
            elif isinstance(page, int) and int(page_match.group(1)) != page:
                errors.append(f"{qid}: explanation citation and page field differ")
        missing_pages = set(range(first_page, last_page + 1)) - page_coverage.get(number, set())
        if missing_pages:
            errors.append(f"Chapter {number}: no question cites Book page(s) {sorted(missing_pages)}")

    units_by_ch: dict[int, list[dict]] = {}
    for unit in units:
        number = unit.get("ch")
        if number not in LIVE_CHAPTERS:
            errors.append(f"{unit.get('id')}: unit belongs to non-live/invalid Chapter {number}")
            continue
        units_by_ch.setdefault(number, []).append(unit)

    unexpected_unit_chapters = sorted(set(units_by_ch) - set(LIVE_CHAPTERS))
    if unexpected_unit_chapters:
        errors.append(f"Units found in non-live chapters: {unexpected_unit_chapters}")

    for number, (_title, _first_page, _last_page, _expected_qs, expected_units) in LIVE_CHAPTERS.items():
        chapter_units = units_by_ch.get(number, [])
        if len(chapter_units) != expected_units:
            errors.append(f"Chapter {number}: expected {expected_units} units, found {len(chapter_units)}")
        covered: list[str] = []
        for index, unit in enumerate(chapter_units, 1):
            expected_id = f"OBG-U{number}-{index}"
            uid = unit.get("id")
            if uid != expected_id:
                errors.append(f"Chapter {number} unit {index}: expected {expected_id}, got {uid}")
            if unit.get("n") != index:
                errors.append(f"{uid}: expected n={index}, got {unit.get('n')}")
            for key in ("title", "sec", "guide"):
                if not isinstance(unit.get(key), str) or not unit[key].strip():
                    errors.append(f"{uid}: missing/non-text {key}")
            qids = unit.get("qs")
            if not isinstance(qids, list) or not qids:
                errors.append(f"{uid}: must contain at least one question")
                continue
            covered.extend(qids)
            unit_pages: list[int] = []
            for qid in qids:
                question = q_by_id.get(qid)
                if question is None:
                    errors.append(f"{uid}: references unknown question {qid}")
                    continue
                if question["id"].split("-")[1] != f"C{number}":
                    errors.append(f"{uid}: references question from another chapter ({qid})")
                unit_pages.append(question["page"])
            if any(unit_pages[i] < unit_pages[i - 1] for i in range(1, len(unit_pages))):
                errors.append(f"{uid}: Book pages are not in source order")

        expected_coverage = [question["id"] for question in qs_by_ch.get(number, [])]
        if covered != expected_coverage:
            errors.append(f"Chapter {number}: units must cover every question exactly once and in source order")

    # The editable JSON artifacts must exactly match what the standalone app ships.
    for number, (title, first_page, last_page, _expected_qs, _expected_units) in LIVE_CHAPTERS.items():
        path = DATA_DIR / f"ch{number:02d}.json"
        if not path.exists():
            errors.append(f"Missing source artifact: {path.relative_to(ROOT)}")
            continue
        try:
            artifact = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{path.name}: invalid JSON ({exc})")
            continue
        if artifact.get("chapter") != number or artifact.get("title") != title:
            errors.append(f"{path.name}: chapter metadata mismatch")
        if artifact.get("pageRange") != f"{first_page}-{last_page}":
            errors.append(f"{path.name}: pageRange mismatch")
        if artifact.get("questions") != qs_by_ch.get(number, []):
            errors.append(f"{path.name}: questions do not exactly match the embedded app content")
        if artifact.get("units") != units_by_ch.get(number, []):
            errors.append(f"{path.name}: units do not exactly match the embedded app content")

    check_javascript_syntax(html, errors)

    if errors:
        print(f"FAILED with {len(errors)} error(s):")
        for error in errors[:50]:
            print(" -", error)
        if len(errors) > 50:
            print(f" ... and {len(errors) - 50} more")
        sys.exit(1)

    total_pages = sum(last - first + 1 for _title, first, last, _q, _u in LIVE_CHAPTERS.values())
    print(
        "PASS: 10 live chapters; "
        f"{len(questions)} questions; {len(units)} units; "
        f"all {total_pages} in-scope Book pages represented; "
        "IDs, four-option structure, citations, order, source artifacts, UI hooks, and JavaScript syntax verified."
    )


if __name__ == "__main__":
    verify()

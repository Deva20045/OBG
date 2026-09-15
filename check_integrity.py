#!/usr/bin/env python3
import re
import json
import sys

def verify():
    with open("pulse-obg.html", "r", encoding="utf-8") as f:
        html = f.read()

    # Check key UI elements matching ORTHO architecture
    required_elements = [
        '<div id="home">',
        '<div id="chapters" class="hidden">',
        '<div id="path" class="hidden">',
        '<div id="guide" class="hidden">',
        '<div id="quiz" class="hidden">',
        '<div id="unitdone" class="hidden">',
        'id="hStreak"',
        'id="hXP"',
        'id="sXP"',
        'id="sStreak"',
        'id="sUnits"',
        'id="chList"',
        'id="nodes"',
        'id="qbar"',
        'id="qtag"',
        'id="qtext"',
        'id="opts"',
        'id="fb"',
        'id="nextBtn"',
        'id="dScore"',
        'id="dXP"',
        'id="dAcc"',
        'id="dRev"',
        'continueLearning()',
        'unlockAll()',
        'beginUnit()',
        'renderQ()',
        'answer(o,btn)',
        'finishUnit()',
        'shuffle(a)'
    ]

    for el in required_elements:
        if el not in html:
            print(f"FAILED: Missing UI element/function: {el}")
            sys.exit(1)

    # Extract JSON objects from script
    q_match = re.search(r'const QUESTIONS = (\[[\s\S]*?\]);', html)
    u_match = re.search(r'const UNITS = (\[[\s\S]*?\]);', html)
    c_match = re.search(r'const CHAPTERS = (\[[\s\S]*?\]);', html)

    if not q_match or not u_match or not c_match:
        print("FAILED: Could not extract QUESTIONS, UNITS, or CHAPTERS from pulse-obg.html")
        sys.exit(1)

    questions = json.loads(q_match.group(1))
    units = json.loads(u_match.group(1))
    chapters = json.loads(c_match.group(1))

    print(f"Verified extraction: {len(questions)} questions, {len(units)} units, {len(chapters)} chapters.")

    errors = []

    # Check chapters
    if len(chapters) != 24:
        errors.append(f"Expected 24 chapters, found {len(chapters)}")
    if not chapters[0]["live"]:
        errors.append("Chapter 1 is not marked live")
    for ch in chapters[1:]:
        if ch["live"]:
            errors.append(f"Chapter {ch['n']} should not be live")

    # Check question IDs: contiguous OBG-C1-001 ...
    for i, q in enumerate(questions, 1):
        expected_id = f"OBG-C1-{i:03d}"
        if q["id"] != expected_id:
            errors.append(f"Q ID mismatch at index {i}: expected {expected_id}, got {q['id']}")
        if len(q["opts"]) != 4:
            errors.append(f"{q['id']}: expected 4 options, got {len(q['opts'])}")
        if not isinstance(q["ans"], int) or q["ans"] < 0 or q["ans"] > 3:
            errors.append(f"{q['id']}: invalid ans index {q['ans']}")
        exp = q["exp"]
        match = re.search(r'\(Book p(\d+)\)$', exp)
        if not match:
            errors.append(f"{q['id']}: explanation does not end with '(Book pX)': {exp}")
        else:
            book_p = int(match.group(1))
            if book_p != q["page"]:
                errors.append(f"{q['id']}: page field {q['page']} does not match explanation book page {book_p}")
            if book_p < 265 or book_p > 301:
                errors.append(f"{q['id']}: book page {book_p} outside Chapter 1 range (265-301)")

    # Check units
    covered_ids = []
    for u_idx, u in enumerate(units, 1):
        expected_uid = f"OBG-U1-{u_idx}"
        if u["id"] != expected_uid:
            errors.append(f"Unit ID mismatch at index {u_idx}: expected {expected_uid}, got {u['id']}")
        if u["ch"] != 1:
            errors.append(f"Unit {u['id']} has ch={u['ch']}, expected 1")
        if u["n"] != u_idx:
            errors.append(f"Unit {u['id']} has n={u['n']}, expected {u_idx}")
        if not u["title"] or not u["guide"]:
            errors.append(f"Unit {u['id']} missing title or guide")
        for qid in u["qs"]:
            covered_ids.append(qid)

    if covered_ids != [q["id"] for q in questions]:
        errors.append("Unit question IDs do not match questions array in exact contiguous order")

    # Check page monotonic order
    for i in range(1, len(questions)):
        if questions[i]["page"] < questions[i-1]["page"]:
            errors.append(f"Page order inversion between {questions[i-1]['id']} (p{questions[i-1]['page']}) and {questions[i]['id']} (p{questions[i]['page']})")

    if errors:
        print(f"FAILED with {len(errors)} errors:")
        for err in errors[:15]:
            print(" -", err)
        sys.exit(1)
    else:
        print("PASS: All syntax and integrity checks succeeded perfectly!")

if __name__ == "__main__":
    verify()

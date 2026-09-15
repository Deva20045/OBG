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
    q_match = re.search(r'const QUESTIONS = (\[[\s\S]*?\]);\nconst UNITS', html)
    u_match = re.search(r'const UNITS = (\[[\s\S]*?\]);\nconst CHAPTERS', html)
    c_match = re.search(r'const CHAPTERS = (\[[\s\S]*?\]);', html)

    if not q_match or not u_match or not c_match:
        print("FAILED: Could not extract QUESTIONS, UNITS, or CHAPTERS from pulse-obg.html")
        sys.exit(1)

    questions = json.loads(q_match.group(1))
    units = json.loads(u_match.group(1))
    chapters = json.loads(c_match.group(1))

    print(f"Verified extraction: {len(questions)} questions, {len(units)} units, {len(chapters)} chapters.")

    errors = []

    # Check chapters: 24 chapters total
    if len(chapters) != 24:
        errors.append(f"Expected 24 chapters, found {len(chapters)}")

    # Chapters 1 to 5 must be live; Chapters 6 to 24 must be locked
    for ch in chapters:
        if ch["n"] in [1, 2, 3, 4, 5]:
            if not ch["live"]:
                errors.append(f"Chapter {ch['n']} should be marked live")
        else:
            if ch["live"]:
                errors.append(f"Chapter {ch['n']} should not be live")

    # Chapter page ranges
    ch_ranges = {
        1: (265, 301),
        2: (302, 326),
        3: (327, 339),
        4: (340, 357),
        5: (358, 374)
    }

    # Group questions by chapter
    qs_by_ch = {}
    for q in questions:
        m = re.match(r'OBG-C(\d+)-(\d+)', q["id"])
        if not m:
            errors.append(f"Invalid question ID format: {q['id']}")
            continue
        c_num = int(m.group(1))
        qs_by_ch.setdefault(c_num, []).append(q)

    for c_num, (min_p, max_p) in ch_ranges.items():
        ch_qs = qs_by_ch.get(c_num, [])
        if not ch_qs:
            errors.append(f"No questions found for live Chapter {c_num}")
            continue
        for i, q in enumerate(ch_qs, 1):
            expected_id = f"OBG-C{c_num}-{i:03d}"
            if q["id"] != expected_id:
                errors.append(f"Q ID mismatch in Ch {c_num} index {i}: expected {expected_id}, got {q['id']}")
            if len(q["opts"]) != 4:
                errors.append(f"{q['id']}: expected 4 options, got {len(q['opts'])}")
            if not isinstance(q["ans"], int) or q["ans"] < 0 or q["ans"] > 3:
                errors.append(f"{q['id']}: invalid ans index {q['ans']}")
            exp = q["exp"]
            m_exp = re.search(r'\(Book p(\d+)\)$', exp)
            if not m_exp:
                errors.append(f"{q['id']}: explanation does not end with '(Book pX)': {exp}")
            else:
                book_p = int(m_exp.group(1))
                if book_p != q["page"]:
                    errors.append(f"{q['id']}: page field {q['page']} does not match explanation book page {book_p}")
                if book_p < min_p or book_p > max_p:
                    errors.append(f"{q['id']}: book page {book_p} outside Chapter {c_num} range ({min_p}-{max_p})")

    # Group units by chapter
    units_by_ch = {}
    for u in units:
        units_by_ch.setdefault(u["ch"], []).append(u)

    for c_num in ch_ranges:
        ch_units = units_by_ch.get(c_num, [])
        if not ch_units:
            errors.append(f"No units found for Chapter {c_num}")
            continue
        covered_ids = []
        for u_idx, u in enumerate(ch_units, 1):
            expected_uid = f"OBG-U{c_num}-{u_idx}"
            if u["id"] != expected_uid:
                errors.append(f"Unit ID mismatch in Ch {c_num} index {u_idx}: expected {expected_uid}, got {u['id']}")
            if u["ch"] != c_num:
                errors.append(f"Unit {u['id']} has ch={u['ch']}, expected {c_num}")
            if u["n"] != u_idx:
                errors.append(f"Unit {u['id']} has n={u['n']}, expected {u_idx}")
            if not u["title"] or not u["guide"]:
                errors.append(f"Unit {u['id']} missing title or guide")
            for qid in u["qs"]:
                covered_ids.append(qid)

        ch_qs = qs_by_ch.get(c_num, [])
        if covered_ids != [q["id"] for q in ch_qs]:
            errors.append(f"Chapter {c_num} unit question IDs do not match questions array in exact contiguous order")

    # Check page monotonic order within each unit
    for u in units:
        u_pages = [next(q["page"] for q in questions if q["id"] == qid) for qid in u["qs"]]
        for i in range(1, len(u_pages)):
            if u_pages[i] < u_pages[i-1]:
                errors.append(f"Unit {u['id']} page inversion: p{u_pages[i-1]} followed by p{u_pages[i]}")

    if errors:
        print(f"FAILED with {len(errors)} errors:")
        for err in errors[:20]:
            print(" -", err)
        sys.exit(1)
    else:
        print(f"PASS: All syntax and integrity checks succeeded perfectly across {len(questions)} questions and {len(units)} units in 5 live chapters!")

if __name__ == "__main__":
    verify()

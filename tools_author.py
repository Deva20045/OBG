#!/usr/bin/env python3
"""Small authoring helper: turn a compact chapter script into data/chNN.json.

A chapter script is a Python module exposing CHAPTER, TITLE, PAGE_RANGE and
UNITS, where UNITS is a list of (unit_title, unit_sec, guide, questions) and
questions is a list of (page, stem, options, answer_index, explanation).
Explanations are auto-suffixed with "(Book pN)" so citations never drift.
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def build(module_path: str) -> Path:
    spec = importlib.util.spec_from_file_location("chapter_script", module_path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)

    number = mod.CHAPTER
    questions, units = [], []
    counter = 0
    for unit_index, (title, sec, guide, qs) in enumerate(mod.UNITS, 1):
        ids = []
        for page, stem, opts, ans, exp in qs:
            counter += 1
            qid = f"OBG-C{number}-{counter:03d}"
            if len(opts) != 4:
                raise ValueError(f"{qid}: needs 4 options, got {len(opts)}")
            if len({o.strip().casefold() for o in opts}) != 4:
                raise ValueError(f"{qid}: options not distinct: {opts}")
            if not 0 <= ans <= 3:
                raise ValueError(f"{qid}: bad answer index {ans}")
            questions.append({
                "id": qid,
                "sec": title,
                "page": page,
                "q": stem.strip(),
                "opts": [o.strip() for o in opts],
                "ans": ans,
                "exp": f"{exp.strip()} (Book p{page})",
            })
            ids.append(qid)
        units.append({
            "id": f"OBG-U{number}-{unit_index}",
            "ch": number,
            "n": unit_index,
            "title": title,
            "sec": sec,
            "guide": f"{guide.strip()} Focus for this checkpoint: {title}.",
            "qs": ids,
        })
    out = {
        "chapter": number,
        "title": mod.TITLE,
        "pageRange": mod.PAGE_RANGE,
        "questions": questions,
        "units": units,
    }
    path = ROOT / "data" / f"ch{number:02d}.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    dist = [0, 0, 0, 0]
    for q in questions:
        dist[q["ans"]] += 1
    print(f"ch{number:02d}: {len(questions)} questions, {len(units)} units, answer-position spread {dist}")
    return path


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        build(arg)

#!/usr/bin/env python3
"""Embed the chapter JSON artifacts into the standalone PULSE OBG app.

The browser app is intentionally a single offline HTML file.  Structured chapter
artifacts in data/chNN.json are the editable source of truth; run this script
whenever a chapter artifact changes.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
APP_PATH = ROOT / "pulse-obg.html"
DATA_PATH = ROOT / "data"

# These titles are shared by the source artifacts and the chapter selection UI.
LIVE_CHAPTERS = {
    1: "Fundamentals of Reproduction",
    2: "Normal Pregnancy and Antenatal Care",
    3: "Fetal Assessment and Ultrasound",
    4: "Fetal Surveillance and Maternal Adaptations",
    5: "Medical Disorders: Anemia, Drugs and Heart Disease",
    6: "Thyroid, Diabetes & Shoulder Dystocia",
    7: "Pregnancy-Induced Hypertension",
    8: "Eclampsia, Liver Disorders & Rh-Negative Pregnancy",
    9: "Abortion, Recurrent Loss & MTP",
    10: "MTP, Ectopic Pregnancy & Gestational Trophoblastic Disease",
    11: "Gestational Trophoblastic Disease: Staging & Management",
    12: "Antepartum Hemorrhage & Placenta Accreta Spectrum",
    13: "Multifetal Gestation: Chorionicity, Complications & Delivery",
    14: "Preterm Labour, PROM & Post-term Pregnancy",
    15: "Maternal Pelvis, Contracted Pelvis & CPD",
    16: "Fetal Skull & Terminologies of Labour",
    17: "Stages of Labour: Normal & Abnormal",
    18: "Partogram & WHO Labour Care Guide",
    19: "Normal Labour & Induction of Labour",
    20: "Postpartum Hemorrhage & Third Stage Complications",
    21: "Perineal Trauma, Episiotomy & Malpresentations",
    22: "Breech & Instrumental Delivery",
    23: "Caesarean Section & VBAC",
    24: "Puerperium",
}


def compact(value: object) -> str:
    """Use compact, UTF-8 JSON so the standalone app remains easy to ship."""
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def between(text: str, start: str, end: str) -> tuple[int, int]:
    first = text.index(start)
    second = text.index(end, first)
    return first, second


def main() -> None:
    chapters = []
    for number in range(1, 25):
        path = DATA_PATH / f"ch{number:02d}.json"
        chapter = json.loads(path.read_text(encoding="utf-8"))
        if chapter["chapter"] != number:
            raise ValueError(f"{path.name}: chapter number does not match filename")
        expected_title = LIVE_CHAPTERS[number]
        if chapter["title"] != expected_title:
            raise ValueError(
                f"{path.name}: expected title {expected_title!r}, got {chapter['title']!r}"
            )
        chapters.append(chapter)

    questions = [question for chapter in chapters for question in chapter["questions"]]
    units = [unit for chapter in chapters for unit in chapter["units"]]

    html = APP_PATH.read_text(encoding="utf-8")
    q_start, u_start = between(html, "const QUESTIONS = ", "\nconst UNITS = ")
    _, c_start = between(html, "const UNITS = ", "\nconst CHAPTERS = ")
    _, after_chapters = between(html, "const CHAPTERS = ", "\nconst QBYID = ")

    # Existing chapter metadata is valid JSON; every chapter is now live.
    existing_chapters = json.loads(html[c_start + len("\nconst CHAPTERS = "):after_chapters].rstrip(";"))
    by_number = {entry["n"]: entry for entry in existing_chapters}
    for chapter in chapters:
        entry = by_number[chapter["chapter"]]
        entry["t"] = chapter["title"]
        entry["p"] = int(chapter["pageRange"].split("-", 1)[0])
        entry["live"] = True

    # Rebuild each contiguous inline dataset section without touching the UI.
    html = (
        html[:q_start]
        + "const QUESTIONS = "
        + compact(questions)
        + ";\nconst UNITS = "
        + compact(units)
        + ";\nconst CHAPTERS = "
        + json.dumps(existing_chapters, ensure_ascii=False, indent=2)
        + ";"
        + html[after_chapters:]
    )
    APP_PATH.write_text(html, encoding="utf-8")
    print(
        f"Embedded {len(questions)} questions and {len(units)} units across "
        f"chapters 1–24 in {APP_PATH.name}."
    )


if __name__ == "__main__":
    main()

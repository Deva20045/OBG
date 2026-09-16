#!/usr/bin/env python3
"""Item laboratory: flag weak items and apply curated question patches.

The chapter artifacts in data/ are the single source of truth.  Every change
goes through this tool so that the guarantees checked by check_integrity.py
hold afterwards:

  * question IDs stay sequential (OBG-Cnn-001 ...) and unique
  * a unit's questions keep non-decreasing book-page order
  * units still cover every question exactly once, in order
  * every explanation ends with its '(Book pN)' citation

Commands
--------
    python3 itemlab.py map                     # unit map (id, title, pages, n questions)
    python3 itemlab.py flag CH [--ratio 3]     # predictability offenders
    python3 itemlab.py apply patches/ch01.json [--rebuild]
    python3 itemlab.py stats                   # format mix after changes

A patch file is a JSON list of operations:

    {"op": "add",   "unit": "OBG-U1-3", "page": 265, "sec": "...", "fmt": "match",
     "q": "...", "opts": ["a","b","c","d"], "ans": 2, "exp": "..."}
    {"op": "edit",  "id": "OBG-C1-042", "q": "...", "opts": [...], "ans": 1, "exp": "..."}

`exp` may omit the citation; "(Book pN)" is appended from the question page.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
INTEGRITY = ROOT / "check_integrity.py"
APP = ROOT / "pulse-obg.html"

VALID_FMTS = {"fillup", "match", "truefalse", "scenario", "oddoneout", "recall", "numeric", "management"}


# ------------------------------------------------------------------------ io
def load(ch: int) -> dict:
    return json.loads((DATA_DIR / f"ch{ch:02d}.json").read_text(encoding="utf-8"))


def save(ch: int, data: dict) -> None:
    (DATA_DIR / f"ch{ch:02d}.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
    )


def unit_pages(chapter: dict) -> dict[str, tuple[int, int]]:
    by_id = {q["id"]: q for q in chapter["questions"]}
    out = {}
    for u in chapter["units"]:
        pages = [by_id[qid]["page"] for qid in u["qs"] if qid in by_id]
        out[u["id"]] = (min(pages), max(pages)) if pages else (0, 0)
    return out


# ------------------------------------------------------------------ commands
def cmd_map(_args: argparse.Namespace) -> None:
    for number in range(1, 25):
        chapter = load(number)
        pages = unit_pages(chapter)
        print(f"\n== Chapter {number}: {chapter['title']} ({chapter['pageRange']})")
        for u in chapter["units"]:
            lo, hi = pages[u["id"]]
            span = f"p{lo}" if lo == hi else f"p{lo}-{hi}"
            print(f"  {u['id']:<10} {span:<10} {len(u['qs']):>2}q  {u['title']}")


def length_ratio(q: dict) -> float:
    lengths = [len(o) for o in q["opts"]]
    correct = lengths[q["ans"]]
    others = [l for i, l in enumerate(lengths) if i != q["ans"]]
    return correct / max(max(others), 1)


def cmd_flag(args: argparse.Namespace) -> None:
    chapters = range(1, 25) if args.ch is None else [args.ch]
    rows = []
    for number in chapters:
        chapter = load(number)
        for q in chapter["questions"]:
            ratio = length_ratio(q)
            if ratio >= args.ratio:
                rows.append((ratio, number, q))
    rows.sort(key=lambda r: -r[0])
    print(f"{len(rows)} items with correct-option length >= {args.ratio}x the longest distractor\n")
    for ratio, number, q in rows[: args.limit]:
        print(f"--- C{number} {q['id']} p{q['page']} ratio {ratio:.1f}  [{q.get('sec','')}]")
        print(f"Q: {q['q']}")
        for i, o in enumerate(q["opts"]):
            mark = "*" if i == q["ans"] else " "
            print(f" {mark} {o}")
        print(f"   exp: {q['exp']}\n")


def cmd_stats(_args: argparse.Namespace) -> None:
    from collections import Counter

    total = Counter()
    explicit = 0
    for number in range(1, 25):
        for q in load(number)["questions"]:
            total[q.get("fmt", "untagged")] += 1
            explicit += "fmt" in q
    n = sum(total.values())
    print(f"{n} questions · {explicit} carry an explicit fmt tag\n")
    for k, v in total.most_common():
        print(f"  {k:<12} {v:>5}  {v / n * 100:5.1f}%")


# -------------------------------------------------------------------- patch
def apply_patch(ch: int, ops: list[dict], dry: bool = False) -> dict:
    chapter = load(ch)
    questions = chapter["questions"]
    by_id = {q["id"]: q for q in questions}
    units = {u["id"]: u for u in chapter["units"]}

    for op in ops:
        kind = op.get("op")
        if kind == "edit":
            q = by_id[op["id"]]
            for field in ("q", "sec", "page", "opts", "ans", "exp", "fmt"):
                if field in op:
                    q[field] = op[field]
        elif kind == "add":
            uid = op["unit"]
            if uid not in units:
                raise ValueError(f"unknown unit {uid}")
            page = int(op["page"])
            unit = units[uid]
            q = {
                "id": f"__new__{len(questions)}",
                "sec": op.get("sec") or unit["title"],
                "page": page,
                "q": op["q"].strip(),
                "opts": [o.strip() for o in op["opts"]],
                "ans": int(op["ans"]),
                "exp": op["exp"].strip(),
            }
            if "fmt" in op:
                q["fmt"] = op["fmt"]
            # Insert keeping non-decreasing page order inside the unit.
            position = len(unit["qs"])
            for index, qid in enumerate(unit["qs"]):
                if by_id[qid]["page"] > page:
                    position = index
                    break
            unit["qs"].insert(position, q["id"])
            questions.append(q)
            by_id[q["id"]] = q
        else:
            raise ValueError(f"unknown op {kind!r}")

    # Renumber sequentially in unit order, then normalise every item.
    ordered: list[dict] = []
    seq = 0
    for unit in chapter["units"]:
        fresh = []
        for qid in unit["qs"]:
            q = by_id[qid]
            seq += 1
            q["id"] = f"OBG-C{ch}-{seq:03d}"
            fresh.append(q["id"])
            ordered.append(q)
        unit["qs"] = fresh

    seen: set[str] = set()
    for q in ordered:
        if len(q["opts"]) != 4:
            raise ValueError(f"{q['id']}: needs 4 options")
        if len({o.strip().casefold() for o in q["opts"]}) != 4:
            raise ValueError(f"{q['id']}: duplicate options {q['opts']}")
        if not 0 <= q["ans"] <= 3:
            raise ValueError(f"{q['id']}: bad answer index")
        if q["id"] in seen:
            raise ValueError(f"duplicate id {q['id']}")
        seen.add(q["id"])
        q["exp"] = re.sub(r"\s*\(Book p\d+\)\s*$", "", q["exp"].strip()) + f" (Book p{q['page']})"

    chapter["questions"] = ordered
    if not dry:
        save(ch, chapter)
        bump_expected_counts(ch, len(ordered), len(chapter["units"]))
    return chapter


def bump_expected_counts(ch: int, questions: int, units: int) -> None:
    """Keep the hard-coded expectations in check_integrity.py in sync."""
    text = INTEGRITY.read_text(encoding="utf-8")
    pattern = re.compile(rf"(\n    {ch}: \(.*?, \d+, )(\d+)(, )(\d+)(\),)")
    match = pattern.search(text)
    if not match:
        raise ValueError(f"could not locate chapter {ch} row in check_integrity.py")
    text = text[: match.start()] + f"{match.group(1)}{questions}{match.group(3)}{units}{match.group(5)}" + text[match.end():]
    INTEGRITY.write_text(text, encoding="utf-8")


def chapter_of(op: dict) -> int:
    """Resolve the chapter an operation belongs to from its target."""
    target = op.get("id") or op.get("unit")
    match = re.match(r"OBG-[UC](\d+)-", str(target))
    if match:
        return int(match.group(1))
    raise ValueError(f"cannot resolve chapter for operation on {target!r}")


def cmd_apply(args: argparse.Namespace) -> None:
    for path in args.patches:
        ops = json.loads(Path(path).read_text(encoding="utf-8"))
        # A patch file may span chapters: group operations by their target.
        grouped: dict[int, list[dict]] = {}
        for op in ops:
            grouped.setdefault(chapter_of(op), []).append(op)
        for ch, chops in sorted(grouped.items()):
            chapter = apply_patch(ch, chops, dry=args.dry)
            print(f"ch{ch:02d}: {len(chapter['questions'])} questions, {len(chapter['units'])} units")
    if not args.dry:
        subprocess.run([sys.executable, "build_content.py"], check=True, cwd=ROOT)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("map").set_defaults(func=cmd_map)
    sub.add_parser("stats").set_defaults(func=cmd_stats)

    p_flag = sub.add_parser("flag")
    p_flag.add_argument("ch", nargs="?", type=int)
    p_flag.add_argument("--ratio", type=float, default=3.0)
    p_flag.add_argument("--limit", type=int, default=20)
    p_flag.set_defaults(func=cmd_flag)

    p_apply = sub.add_parser("apply")
    p_apply.add_argument("patches", nargs="+")
    p_apply.add_argument("--dry", action="store_true")
    p_apply.set_defaults(func=cmd_apply)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

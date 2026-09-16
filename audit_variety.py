#!/usr/bin/env python3
"""Audit question-format variety and option predictability for PULSE OBG.

Reads the chapter source artifacts in data/ (the single source of truth) and
reports, per chapter and overall:

  * the mix of question formats actually shipped (recall, numeric, fill-up,
    match-the-following, true/false statement sets, clinical scenarios,
    odd-one-out / negative stems, best-next-step management)
  * predictability signals that let a learner guess without knowing the fact:
      - longest option is the answer
      - the answer is the only hedged / qualified / parenthesised option
      - filler distractors ("All of the above", "None", "Not significant" ...)
      - templated stems repeated back-to-back inside a unit
      - option sets reused verbatim between questions
      - the answer term leaked into the stem

Usage:
    python3 audit_variety.py            # human-readable report
    python3 audit_variety.py --json     # machine-readable summary
"""
from __future__ import annotations

import json
import re
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"

# ---------------------------------------------------------------- format rules
# Each rule returns True when a stem matches.  Order matters: the first match
# wins, so the more specific patterns are tested first.
BLANK_RE = re.compile(r"_{3,}|_{2,}|\bblank\b|\(\s*\.\.\.\s*\)", re.I)
MATCH_RE = re.compile(r"\bmatch the following\b|\bmatch list\b|\bcorrectly matched\b|\bmatch the pair", re.I)
TF_RE = re.compile(
    r"\btrue\b|\bfalse\b|statement[s]? (is|are) (correct|incorrect|true|false)"
    r"|which of the following statement",
    re.I,
)
SCENARIO_RE = re.compile(
    r"\b\d{1,2}\s*[- ]?(year[- ]old|y/o|years old|yr old|yr)\b"
    r"|\bG\d\s*P\d|\bP\d\+\d|\bprimigravida\b|\bmultigravida\b|\bgravida \d\b"
    r"|\bpresents (with|to|in)\b|\badmitted\b|\bher (BP|blood pressure|pulse|vitals)\b"
    r"|\bcomplains of\b|\bbrought (to|in)\b|\ba woman\b|\ba patient\b|\bshe (is|has|gives)\b",
    re.I,
)
NEGATIVE_RE = re.compile(
    r"\bexcept\b|\bnot (a|an|the)\b|\bdoes not\b|\bis not\b|\bare not\b"
    r"|\bleast likely\b|\bodd one\b|\ball of the following .{0,40}\bexcept\b"
    r"|\bwhich is (incorrect|false)\b|\bincorrect\b|\binappropriate\b"
    r"|\bcontraindicat\w*\b|\bavoid\b|\bnever\b",
    re.I,
)
NEXT_STEP_RE = re.compile(
    r"\bnext (step|best step|line|management)\b|\bbest (next )?(step|management|treatment|option)\b"
    r"|\bmanagement (of|is|should)\b|\btreatment of choice\b|\bdrug of choice\b"
    r"|\binvestigation of choice\b|\bmost appropriate\b",
    re.I,
)
NUMERIC_RE = re.compile(
    r"\bhow many\b|\bwhat is the (?:.*?)(?:value|dose|dose|number|count|level|incidence|rate|duration|length|weight|interval)\b"
    r"|\bat what\b|\bup to what\b|\bduration\b|\bdose\b|\bdosage\b|\bpercentage\b|\bratio\b|\bweeks?\b",
    re.I,
)

FILLER_DISTRACTORS = {
    "all of the above",
    "none of the above",
    "all of these",
    "none of these",
    "none",
    "no specific value",
    "not significant",
    "not clinically significant",
    "no clinical significance",
    "unknown",
    "cannot be determined",
    "data inadequate",
    "none of the mentioned",
    "all are correct",
    "none is correct",
    "both a and b",
    "both b and c",
    "a and b",
    "a and c",
    "b and c",
}

HEDGE_RE = re.compile(r"\b(may|might|usually|typically|often|generally|most commonly|predominantly|rarely)\b", re.I)


def classify(stem: str, options: list[str]) -> str:
    s = stem.strip()
    if MATCH_RE.search(s):
        return "match"
    if BLANK_RE.search(s):
        return "fillup"
    if TF_RE.search(s):
        return "truefalse"
    if SCENARIO_RE.search(s):
        return "scenario"
    if NEGATIVE_RE.search(s):
        return "oddoneout"
    if NEXT_STEP_RE.search(s):
        return "management"
    if NUMERIC_RE.search(s):
        return "numeric"
    return "recall"


def stem_template(stem: str) -> str:
    """Coarse template signature used to detect back-to-back repetition."""
    words = re.sub(r"[^A-Za-z ]", " ", stem).split()
    return " ".join(words[:4]).casefold()


def content_words(text: str) -> set[str]:
    stop = {
        "the", "a", "an", "of", "in", "is", "are", "to", "and", "or", "for",
        "which", "what", "following", "by", "with", "on", "at", "as", "that",
        "from", "it", "its", "be", "been", "this", "these", "those", "into",
        "during", "after", "before", "when", "not", "does", "do", "has", "have",
    }
    return {w for w in re.findall(r"[a-z]{3,}", text.casefold()) if w not in stop}


def audit_chapter(path: Path) -> dict:
    chapter = json.loads(path.read_text(encoding="utf-8"))
    number = chapter["chapter"]
    questions = chapter["questions"]
    units = {u["id"]: u for u in chapter["units"]}

    fmt = Counter()
    longest_is_correct = 0
    hedge_only_correct = 0
    filler_present = 0
    filler_is_correct = 0
    parens_only_correct = 0
    leaked_term = 0
    ans_position = Counter()
    len_correct, len_distractor = [], []
    option_sets = Counter()
    scored = 0

    for q in questions:
        stem, opts, ans = q["q"], q["opts"], q["ans"]
        fmt[q.get("fmt") or classify(stem, opts)] += 1
        ans_position[ans] += 1

        lengths = [len(o) for o in opts]
        correct_len = lengths[ans]
        dist_lens = [l for i, l in enumerate(lengths) if i != ans]
        len_correct.append(correct_len)
        len_distractor.extend(dist_lens)
        if correct_len == max(lengths) and correct_len > max(dist_lens):
            longest_is_correct += 1
        scored += 1

        hedges = [bool(HEDGE_RE.search(o)) for o in opts]
        if hedges[ans] and not any(hedges[i] for i in range(4) if i != ans):
            hedge_only_correct += 1

        parens = ["(" in o for o in opts]
        if parens[ans] and not any(parens[i] for i in range(4) if i != ans):
            parens_only_correct += 1

        filler_idx = [i for i, o in enumerate(opts) if o.strip().casefold() in FILLER_DISTRACTORS]
        if filler_idx:
            filler_present += 1
            if ans in filler_idx:
                filler_is_correct += 1

        # Answer term leaked: every content word of the correct option already
        # appears in the stem, so the option is a paraphrase giveaway.
        stem_words = content_words(stem)
        cw = content_words(opts[ans])
        if cw and cw <= stem_words and len(cw) >= 2:
            leaked_term += 1

        option_sets[tuple(sorted(o.strip().casefold() for o in opts))] += 1

    # Back-to-back identical stem templates inside one unit.
    repeats = 0
    max_run = 0
    for unit in chapter["units"]:
        run = 1
        prev = None
        for qid in unit["qs"]:
            q = next((x for x in questions if x["id"] == qid), None)
            if q is None:
                continue
            t = stem_template(q["q"])
            if t == prev:
                run += 1
            else:
                run = 1
                prev = t
            max_run = max(max_run, run)
        if run > 1:
            repeats += run - 1

    total = max(scored, 1)
    top_templates = Counter()
    for q in questions:
        if "fmt" not in q:
            top_templates[stem_template(q["q"])] += 1

    reused_option_sets = sum(v - 1 for v in option_sets.values() if v > 1)

    return {
        "chapter": number,
        "title": chapter["title"],
        "questions": len(questions),
        "units": len(units),
        "formats": dict(fmt),
        "format_share": {k: round(v / total * 100, 1) for k, v in fmt.items()},
        "longest_is_correct_pct": round(longest_is_correct / total * 100, 1),
        "hedge_only_correct_pct": round(hedge_only_correct / total * 100, 1),
        "parens_only_correct_pct": round(parens_only_correct / total * 100, 1),
        "filler_distractor_pct": round(filler_present / total * 100, 1),
        "filler_is_answer": filler_is_correct,
        "answer_term_leaked_pct": round(leaked_term / total * 100, 1),
        "avg_len_correct": round(statistics.mean(len_correct), 1) if len_correct else 0,
        "avg_len_distractor": round(statistics.mean(len_distractor), 1) if len_distractor else 0,
        "answer_position": dict(ans_position),
        "repeated_stem_template_runs": repeats,
        "longest_repeat_run": max_run,
        "reused_option_sets": reused_option_sets,
        "top_stem_openers": top_templates.most_common(6),
    }


def main() -> None:
    results = [audit_chapter(p) for p in sorted(DATA_DIR.glob("ch*.json"))]

    if "--json" in sys.argv:
        print(json.dumps(results, ensure_ascii=False, indent=1))
        return

    total_q = sum(r["questions"] for r in results)
    agg = Counter()
    for r in results:
        agg.update(r["formats"])

    print("=" * 78)
    print("PULSE OBG — QUESTION VARIETY & PREDICTABILITY AUDIT")
    print("=" * 78)
    print(f"{total_q} questions · {sum(r['units'] for r in results)} units · 24 chapters\n")

    print("FORMAT MIX (whole bank)")
    for name, count in agg.most_common():
        print(f"  {name:<12} {count:>5}  {count / total_q * 100:5.1f}%")
    print()

    header = f"{'Ch':>3} {'Qs':>4} {'scen':>5} {'fill':>5} {'match':>6} {'T/F':>5} {'odd':>5} {'longest':>8} {'leak':>6} {'reuse':>6}"
    print(header)
    print("-" * len(header))
    for r in results:
        f = r["formats"]
        print(
            f"{r['chapter']:>3} {r['questions']:>4} "
            f"{f.get('scenario', 0):>5} {f.get('fillup', 0):>5} {f.get('match', 0):>6} "
            f"{f.get('truefalse', 0):>5} {f.get('oddoneout', 0):>5} "
            f"{r['longest_is_correct_pct']:>7}% {r['answer_term_leaked_pct']:>5}% "
            f"{r['reused_option_sets']:>6}"
        )
    print()

    def mean(key: str) -> float:
        return round(statistics.mean(r[key] for r in results), 1)

    print("PREDICTABILITY SIGNALS (bank-wide means)")
    print(f"  longest option is the answer        : {mean('longest_is_correct_pct')}%")
    print(f"  answer is the only hedged option    : {mean('hedge_only_correct_pct')}%")
    print(f"  answer is the only bracketed option : {mean('parens_only_correct_pct')}%")
    print(f"  question contains filler distractor : {mean('filler_distractor_pct')}%")
    print(f"  answer term restated in the stem    : {mean('answer_term_leaked_pct')}%")
    print(f"  avg answer length / distractor      : {mean('avg_len_correct')} / {mean('avg_len_distractor')}")
    print(f"  repeated back-to-back stem templates: {sum(r['repeated_stem_template_runs'] for r in results)}")
    print(f"  longest uninterrupted repeat run    : {max(r['longest_repeat_run'] for r in results)}")
    print(f"  option sets reused across questions : {sum(r['reused_option_sets'] for r in results)}")
    print()
    print("MOST REPEATED STEM OPENERS")
    opener = Counter()
    for r in results:
        opener.update(dict(r["top_stem_openers"]))
    for template, count in opener.most_common(12):
        print(f"  {count:>4}×  '{template} …'")
    print()


if __name__ == "__main__":
    main()

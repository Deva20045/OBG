# Question-quality re-audit — variety and predictability

Re-run after the complaint that the bank had drifted into "easily predictable
options" and had fallen back on one repeated question shape.

## What the audit measured

`python3 audit_variety.py` reads `data/ch*.json` and reports, per chapter and
for the whole bank:

* the mix of question **formats** actually shipped
* **predictability signals** that let a learner answer without knowing the fact:
  * the correct option is the longest one
  * the correct option is the only hedged / bracketed option
  * filler distractors ("All of the above", "None", …)
  * the answer term is restated in the stem
  * stem templates repeated back-to-back inside a unit
  * option sets reused verbatim between questions

## Findings before the fix (2,368 questions)

| Signal | Value | What it means |
| --- | --- | --- |
| Plain recall | **77.0%** | four of every five items were the same shape |
| Match-the-following | **0%** | the format was simply absent |
| True/false statement sets | **0.7%** | 17 items in the whole bank |
| Clinical scenarios | **2.0%** | almost no vignettes |
| Fill-ups | 5.2% | present only from chapter 11 onwards |
| Odd-one-out | 4.3% | |
| **Correct option is the longest** | **67.8%** | picking the longest option scored ~68% for free |
| Worst chapters | ch 21 **92.3%**, ch 22 91.7%, ch 24 91.7%, ch 4 90.8% | in those chapters length alone gave the answer |
| Answer length vs distractor | **59.9 / 29.2** characters | the answer was literally twice as long |
| Items where the answer was ≥4× the longest distractor | **78** | unmissable giveaways |
| Items where the answer was ≥3.5× | **118** | |

Two recurring failure patterns accounted for most of the damage:

1. **Paired "X : Y" items** — the correct option was a full two-part answer
   ("During labour … respiratory depression … : DIC with excessive bleeding",
   183 characters) while the distractors were two-word stubs ("Bleeding :
   shock", "Fever : DIC"). Choosing the long option was trivially correct.
2. **List items** — the correct option enumerated five risk factors while the
   distractors were single entities ("Maternal anaemia", "Smoking",
   "Primigravity"), so the answer announced itself.

## What was changed (2,710 questions after the pass)

**1. Format variety — one new item in every one of the 342 units (342 new items)**

| Format | Before | After |
| --- | --- | --- |
| Fill-ups | 124 (5.2%) | **237 (8.7%)** |
| Match-the-following | 0 (0%) | **71 (2.6%)** |
| True/false statement sets | 17 (0.7%) | **67 (2.5%)** |
| Clinical scenarios | 47 (2.0%) | **101 (3.7%)** |
| Odd-one-out | 101 (4.3%) | **155 (5.7%)** |
| Plain recall | 1,824 (77.0%) | 1,824 (67.3%) |

Every unit now contains at least one non-recall item. Fill-ups appear in 113
units, matching in 71, scenarios in 54, odd-one-out in 54 and true/false in 50.
New items are tagged with a `fmt` field so the mix is measured, not guessed.

**2. Predictability — de-biased 514 items whose answer gave itself away**

* All **78** items where the answer was ≥4× the longest distractor rewritten.
* All items ≥3.5× rewritten, then all ≥3.0×, then all ≥2.5×, then all ≥2.0× —
  **zero remain above 2.0×**, which was 887 items before this work.
* Distractors were rebuilt to be the same *kind* of thing and the same *length*
  as the key: paired items now offer four paired options (including the classic
  reversed-order trap), and list items now offer four lists.

| Signal | Before | After |
| --- | --- | --- |
| Items ≥4× longest distractor | 78 | **0** |
| Items ≥3.5× | 118 | **0** |
| Items ≥3.0× | 194 | **0** |
| Items ≥2.5× | 309 | **0** |
| Items ≥2.0× | 887 | **0** |
| Answer length vs distractor | 59.9 / 29.2 chars | **49.1 / 42.7 chars** |
| Correct option is the longest, bank-wide | 67.8% | **57.8%** chapter mean |
| Worst chapter (24) | 91.7% | **79.1%** |
| Best chapter (6) | 36.1% | **37.1%** |

## Honest status of what is left

Every gross length tell is gone: the answer is never twice as long as its
longest distractor, and the average answer is now 49.1 characters against 42.7
for the longest distractor, rather than 59.9 against 29.2. The chapter-mean
"longest option is the answer" figure is down to **57.8%** from 67.8%, and no
chapter is still above 80% (chapter 24 was 91.7%).

What remains is *mild*: **742** items still have the key as the longest option
by 1.3× or more, and the median item now sits at a ratio of 1.12 rather than
1.23. Those are the next tranche. Chapters 24, 22, 20, 4 and 21 are the worst
remaining, all between 73% and 79%.

Bulk trimming was deliberately *not* automated. A script that shortens the
correct option by cutting its parenthetical or its trailing clause would have
touched hundreds of good items and stripped exactly the detail that makes an
option unambiguous ("1 mature ovum (female pronucleus)", "70–74 days (~72
days)"). The remaining work is being done by hand, worst-first.

## Guard rails added

`check_integrity.py` now fails the build when:

* any option set lets the answer be spotted by length alone (≥3.0× the longest
  distractor) — this is the regression that caused the complaint, and the
  ceiling has been tightened from 3.5× to 3.0× as the bank improved
* any unit has no varied-format question at all
* a question carries an unrecognised `fmt` tag

Both were verified to fire on deliberately broken input before being committed.

`check_app_smoke.js` no longer hard-codes the question and unit totals, which
previously broke on every content addition; it now derives its expectations from
`data/ch*.json`, so adding content cannot desynchronise the tests.

## Tooling

```bash
python3 audit_variety.py              # format mix + predictability report
python3 audit_variety.py --json       # machine-readable version
python3 itemlab.py map                # every unit: id, pages, question count
python3 itemlab.py flag 22 --ratio 3  # list the predictable items in a chapter
python3 itemlab.py stats              # format mix from the fmt tags
python3 itemlab.py apply patches/ch22.json
```

`itemlab.py` is the only route for content edits. It keeps ID sequences
contiguous, preserves non-decreasing book-page order inside each unit, appends
the `(Book pN)` citation, and keeps the hard-coded expectations in
`check_integrity.py` in sync. Curated patches live in `patches/`.

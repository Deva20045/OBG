# PULSE OBG

A standalone, offline-friendly PULSE quiz companion for the Marrow Edition 8
Obstetrics & Gynaecology notes.

## Content workflow

- `data/chNN.json` is the structured source of truth for each completed chapter.
- `pulse-obg.html` is the single-file browser application shipped to learners.
- Run `python3 build_content.py` after changing chapter JSON to embed the live
  chapter data and metadata into the standalone app.

## Authoring and editing

`itemlab.py` is the only supported route for content edits — it renumbers IDs
sequentially, keeps each unit's questions in non-decreasing book-page order,
appends the `(Book pN)` citation, and syncs the expectations in
`check_integrity.py`.

```bash
python3 itemlab.py map                      # every unit: id, pages, question count
python3 itemlab.py flag 22 --ratio 3        # the predictable items in a chapter
python3 itemlab.py stats                    # format mix from the fmt tags
python3 itemlab.py apply patches/ch22.json  # apply curated edits, then rebuild
```

Curated patches live in `patches/`. Every question may carry a `fmt` tag
(`fillup`, `match`, `truefalse`, `scenario`, `oddoneout`, `recall`, `numeric`,
`management`) so the question mix is measured rather than guessed.

## Validation

```bash
python3 check_integrity.py
node check_app_smoke.js
python3 audit_variety.py
```

The integrity check verifies IDs, question structure, page citations/ranges,
unit coverage and order, the source-to-app match, UI hooks, and JavaScript
syntax — plus two content-quality guards: no question may let the answer be
guessed from option length alone, and every unit must contain at least one
varied-format question. The smoke test executes the app against a minimal DOM
shim and checks the rendered roadmap and quiz flow without external
dependencies. The audit reports the question-format mix and the predictability
signals; see `AUDIT.md` for the current numbers.

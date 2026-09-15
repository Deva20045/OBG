# PULSE OBG

A standalone, offline-friendly PULSE quiz companion for the Marrow Edition 8
Obstetrics & Gynaecology notes.

## Content workflow

- `data/chNN.json` is the structured source of truth for each completed chapter.
- `pulse-obg.html` is the single-file browser application shipped to learners.
- Run `python3 build_content.py` after changing chapter JSON to embed the live
  chapter data and metadata into the standalone app.

## Validation

```bash
python3 check_integrity.py
node check_app_smoke.js
```

The integrity check verifies IDs, question structure, page citations/ranges,
unit coverage and order, the source-to-app match, UI hooks, and JavaScript
syntax. The smoke test executes the app against a minimal DOM shim and checks
the rendered roadmap and quiz flow without external dependencies.

# PULSE OBG — single source of truth

## Goal
Build a line-by-line PULSE quiz companion for the OBG source scans in the `Uploads` branch. Every source line becomes a question in strict book order; chapter data is append-only and validated before merge.

## Source and page map
- `Uploads/OBG_Vol_2_Part_1_pages_1-62.pdf`: PDF page `p` maps to book page `p`.
- `Uploads/OBG_Vol_2_Part_2_pages_63-123.pdf`: book page = PDF page + 62.
- `Uploads/OBG_Vol_2_Part_3_pages_124-185.pdf`: book page = PDF page + 123.
- `Uploads/OBG_Vol_2_Part_4_pages_186-246.pdf`: book page = PDF page + 185.
- `Uploads/OBG_Vol_2_Part_5_pages_247-308.pdf`: book page = PDF page + 246.

## Schema (same as ORTHO)
`Question = {id, sec, page, q, opts[4], ans, exp}`. `Unit = {id, ch, n, title, sec, qs[], guide}`. `Chapter = {n,t,p,live}`. Question IDs are `OBG-C{chapter}-{nnn}` and units contain contiguous question IDs exactly once.

## Per-chapter pipeline
1. Read/render the source PDF pages; preserve every line and book order.
2. Write `data/chNN.json`; validate contiguous IDs, four options, answer indexes, page references, and unit coverage.
3. Merge data into `pulse-obg.html`; run syntax/integrity checks.
4. Commit and push the chapter; update this file with counts and live link.

## Status
- DONE: none (chapter 1 scaffold is present and awaiting full source transcription verification).
- NEXT: Chapter 1 — source pages 1 onward, line-by-line.
- Soon: Chapters 2–24 are listed in-app from day one and remain locked until transcribed.

## Chapter map
1–24: OBG Volume 2 chapters — titles to be confirmed against the source table of contents during transcription. All are visible in the app as Soon; only a chapter with validated data is Live.

## Live link
`https://deva20045.github.io/OBG/` (GitHub Pages; `index.html` redirects to `pulse-obg.html`).

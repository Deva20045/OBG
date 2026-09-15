# PULSE OBG — Single Source of Truth

## Goal
Build a line-by-line PULSE quiz companion for the Marrow Edition 8 Obstetrics & Gynaecology scanned notes in the `Uploads` branch. Every source line, table, diagram, clinical aspect, and note becomes an ordered, understandable question; chapter data is append-only and validated before merge.

## App Architecture (Exact match with ORTHO)
- Single-page Duolingo-style game UI (`pulse-obg.html`).
- Home screen with stats: Total XP, Day streak, Units completed, "Unlock all units", and "Continue learning".
- Chapter roadmap with all 24 chapters visible from day one: live chapters unlocked, upcoming chapters marked "Soon".
- Path view with Duolingo-style unit nodes, progress checkmarks, locked icons, animated current unit, and section dividers.
- Guide screen with 2–3 sentence vivid summary of each unit before beginning.
- Quiz interface with progress bar, question counter, section tag, question text, 4 options (shuffled per run to eliminate position bias), immediate green/red feedback with concise explanation, floating XP animations, and keyboard shortcuts (1–4, Enter).
- Unit completion screen celebrating score, XP earned, accuracy %, missed-question review flow, and redo options.
- State persistence via `localStorage` for XP, streak, and completed units.
- `index.html` provides seamless redirect to `pulse-obg.html`.

## Source and Page Map
- Source PDF branch: `Uploads`
- Chapter 1 PDF source: `Uploads/OBG_Vol_2_Part_1_pages_1-62.pdf`
- Page-offset formula: `Book Page = PDF Page + 264` (e.g., PDF page 1 corresponds to printed book page 265; PDF page 37 corresponds to printed book page 301).
- Subsequent volume parts:
  - `Uploads/OBG_Vol_2_Part_1_pages_1-62.pdf`: PDF pages 1–62 → Book pages 265–326 (Book page = PDF page + 264).
  - `Uploads/OBG_Vol_2_Part_2_pages_63-123.pdf`: PDF pages 1–61 → Book pages 327–387 (Book page = PDF page + 326).
  - `Uploads/OBG_Vol_2_Part_3_pages_124-185.pdf`: PDF pages 1–62 → Book pages 388–449 (Book page = PDF page + 387).
  - `Uploads/OBG_Vol_2_Part_4_pages_186-246.pdf`: PDF pages 1–61 → Book pages 450–510 (Book page = PDF page + 449).
  - `Uploads/OBG_Vol_2_Part_5_pages_247-308.pdf`: PDF pages 1–62 → Book pages 511–572 (Book page = PDF page + 510).

## Chapter 1 Specifications
- Chapter title: **Fundamentals of Reproduction**
- Page range: **Book pages 265–301** (PDF pages 1–37 of Part 1)
- Total questions: **232** (`OBG-C1-001` through `OBG-C1-232`)
- Total units: **28** (`OBG-U1-1` through `OBG-U1-28`)
- Units outline:
  1. Unit 1: Primordial Germ Cells & Sex Determination (p265) — 5 questions
  2. Unit 2: Spermatogenesis & Seminiferous Tubules (p265-266) — 11 questions
  3. Unit 3: Sperm Structure, Maturation & Lifespan (p266) — 10 questions
  4. Unit 4: Oogenesis & Follicular Dynamics (p266-267) — 17 questions
  5. Unit 5: Germ Cell Potency & Teratoma Origin (p267) — 4 questions
  6. Unit 6: Capacitation & Acrosome Reaction (p268) — 9 questions
  7. Unit 7: Fertilization, Cleavage & Tubal Transport (p268-269) — 8 questions
  8. Unit 8: Implantation Stages & Decidualisation (p270-271) — 11 questions
  9. Unit 9: Blastocyst Differentiation & Trophoblast (p272) — 6 questions
  10. Unit 10: Fetal Membranes & Yolk Sac (p272-273) — 6 questions
  11. Unit 11: Preimplantation Genetic Testing & ART (p273) — 5 questions
  12. Unit 12: Teratogenic Exposure & Radiation in Pregnancy (p274) — 7 questions
  13. Unit 13: Teratogenic Drugs: Category X & Specific Malformations (p275-276) — 13 questions
  14. Unit 14: Teratogenic Infections: TORCH & Congenital Syndromes (p277-278) — 12 questions
  15. Unit 15: Gross Placental Architecture & Placentomegaly (p279-280) — 7 questions
  16. Unit 16: Placental Villi Development & Trophoblastic Invasion (p281) — 6 questions
  17. Unit 17: Placental Circulation & Cotyledon Anatomy (p282) — 6 questions
  18. Unit 18: Placental Respiration & Corpus Luteum Maintenance (p283-284) — 7 questions
  19. Unit 19: Placental Steroidogenesis & Labor Onset (p284-285) — 8 questions
  20. Unit 20: Human Placental Lactogen & hCG Endocrinology (p285-288) — 11 questions
  21. Unit 21: Placental Morphological Anomalies & PAS (p289-290) — 8 questions
  22. Unit 22: Cord Insertion Anomalies, Vasa Previa & Apt Test (p291-293) — 8 questions
  23. Unit 23: Fetal Hematopoiesis & Placental Separation (p293-294) — 6 questions
  24. Unit 24: Amniotic Fluid Dynamics & Color Signatures (p295-296) — 9 questions
  25. Unit 25: Amniotic Fluid Assessment (AFI & SDP) (p296-297) — 7 questions
  26. Unit 26: Polyhydramnios & Oligohydramnios Etiology (p297-298) — 8 questions
  27. Unit 27: Fetal Monitoring, Oligohydramnios & Amniotic Bands (p299-301) — 10 questions
  28. Unit 28: Polyhydramnios Management & Classic Imaging Signs (p301) — 7 questions

## Validation Status
- Contiguous question IDs (`OBG-C1-001` to `OBG-C1-232`): **PASS**
- Exactly 4 options per question: **PASS**
- Valid answer index (0–3): **PASS**
- 100% question coverage by units exactly once: **PASS**
- Strict book order preservation: **PASS**
- All question explanations end with `(Book pX)`: **PASS**
- JavaScript syntax and DOM integrity: **PASS**

## Status
- **DONE**: Chapter 1 (Fundamentals of Reproduction, 232 questions, 28 units, Book pages 265–301). Complete and verified from the first page of the chapter to the final page.
- **NEXT**: Chapter 2: Normal Pregnancy and Antenatal Care (Book pages 302–326, starting at PDF page 38 of `OBG_Vol_2_Part_1_pages_1-62.pdf`).
- **Soon**: Chapters 2–24 are all visible in-app with titles from day one, marked as "Soon" until transcribed.

## Live Links
- GitHub Pages live link: `https://deva20045.github.io/OBG/` (redirects to `pulse-obg.html`).
- Direct app URL: `https://deva20045.github.io/OBG/pulse-obg.html`.

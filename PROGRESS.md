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
- Subsequent volume parts:
  - `Uploads/OBG_Vol_2_Part_1_pages_1-62.pdf`: PDF pages 1–62 → Book pages 265–326 (Book page = PDF page + 264).
    - Chapter 1: Book pages 265–301 (PDF pages 1–37)
    - Chapter 2: Book pages 302–326 (PDF pages 38–62)
  - `Uploads/OBG_Vol_2_Part_2_pages_63-123.pdf`: PDF pages 1–61 → Book pages 327–387 (Book page = PDF page + 326).
    - Chapter 3: Book pages 327–339 (PDF pages 1–13)
    - Chapter 4: Book pages 340–357 (PDF pages 14–31)
    - Chapter 5: Book pages 358–374 (PDF pages 32–48)
  - `Uploads/OBG_Vol_2_Part_3_pages_124-185.pdf`: PDF pages 1–62 → Book pages 388–449 (Book page = PDF page + 387).
  - `Uploads/OBG_Vol_2_Part_4_pages_186-246.pdf`: PDF pages 1–61 → Book pages 450–510 (Book page = PDF page + 449).
  - `Uploads/OBG_Vol_2_Part_5_pages_247-308.pdf`: PDF pages 1–62 → Book pages 511–572 (Book page = PDF page + 510).

---

## Completed Chapters Summary

### Chapter 1: Fundamentals of Reproduction
- **Page range**: Book pages 265–301 (PDF pages 1–37 of Part 1)
- **Total questions**: **235** (`OBG-C1-001` through `OBG-C1-235`)
- **Total units**: **28** (`OBG-U1-1` through `OBG-U1-28`)
- **Corrections applied**: Added missing high-yield points including seminiferous tubule adluminal compartment cell populations, Sertoli cell blood-testis barrier tight junctions, and ovarian reserve testing for the resting follicle pool.

### Chapter 2: Normal Pregnancy and Antenatal Care
- **Page range**: Book pages 302–326 (PDF pages 38–62 of Part 1)
- **Total questions**: **107** (`OBG-C2-001` through `OBG-C2-107`)
- **Total units**: **18** (`OBG-U2-1` through `OBG-U2-18`)
- **Units outline**:
  1. Unit 1: Gestational Age, Trimesters & Naegele's Rule (p302-303) — 8 questions
  2. Unit 2: ART Dating, Preterm Categories & Fetal Death / IUD (p304-305) — 8 questions
  3. Unit 3: Obstetrical Score (GTPAL) & Gravidity / Parity (p306-307) — 6 questions
  4. Unit 4: Symptoms, Pelvic Signs & Diagnostic Signs of Pregnancy (p307-309) — 8 questions
  5. Unit 5: Uterine Growth, Fundal Height & Discrepancies (p308, 310) — 7 questions
  6. Unit 6: Umbilical Cord Architecture & Doppler Waveforms (p311-312) — 6 questions
  7. Unit 7: Abnormal Doppler: UPI, AEDF, REDF & MCA Doppler (p312-314) — 6 questions
  8. Unit 8: Single Umbilical Artery & Fetal Surveillance (p314) — 5 questions
  9. Unit 9: Antenatal Care Schedules, Mandatory & Optional Labs (p315-316) — 6 questions
  10. Unit 10: Td/Tdap Vaccines, Risk Coding & Alert Signs (p316-317) — 6 questions
  11. Unit 11: Folic Acid Prophylaxis & IFA / Anemia Mukt Bharat (p317) — 5 questions
  12. Unit 12: Antenatal Monitoring, Caloric & Nutrient Demands (p318-319) — 5 questions
  13. Unit 13: Vaccines, Air Travel & Exercise in Pregnancy (p319) — 4 questions
  14. Unit 14: Morning Sickness, Hyperemesis Gravidarum & PUQE (p320-321) — 5 questions
  15. Unit 15: Minor Ailments: Supine Hypotension, Varices & Neuropathies (p321-323) — 6 questions
  16. Unit 16: Early Ultrasound Landmarks & Gestational Structures (p324-325) — 5 questions
  17. Unit 17: Fetal Pole, Cardiac Activity & Missed Abortion Criteria (p325-326) — 6 questions
  18. Unit 18: Discriminatory hCG Titer & True vs Pseudogestational Sac (p326) — 5 questions

### Chapter 3: Fetal Assessment and Ultrasound
- **Page range**: Book pages 327–339 (PDF pages 1–13 of Part 2)
- **Total questions**: **61** (`OBG-C3-001` through `OBG-C3-061`)
- **Total units**: **12** (`OBG-U3-1` through `OBG-U3-12`)
- **Units outline**:
  1. Unit 1: Early Ultrasound Signs & Biometry Dating (p327-328) — 7 questions
  2. Unit 2: Second Trimester Biometry, Cervical Length & Fetal Echo (p328-329) — 6 questions
  3. Unit 3: Anomaly Scan (TIFFA) & Cranial NTDs: Anencephaly & Acrania (p330-331) — 6 questions
  4. Unit 4: Spina Bifida, Arnold-Chiari II Signs & Craniorachischisis (p332-333) — 6 questions
  5. Unit 5: Abdominal Wall Defects: Omphalocele vs Gastroschisis (p333-334) — 5 questions
  6. Unit 6: Alpha-Fetoprotein (AFP) Biology & Diagnostic Deviations (p334) — 5 questions
  7. Unit 7: Aneuploidy Principles & Down Syndrome Genetics (p335-336) — 5 questions
  8. Unit 8: First Trimester Screening: Dual Test & Combined Test (p336) — 4 questions
  9. Unit 9: Nuchal Translucency & Cystic Hygroma Differentiation (p337-338) — 5 questions
  10. Unit 10: Second Trimester Markers: Triple, Quad & Soft Sonographic Signs (p338) — 4 questions
  11. Unit 11: Non-Invasive Prenatal Testing (NIPT / cffDNA) & Integrated Screening (p339) — 4 questions
  12. Unit 12: Aneuploidy Risk Interpretation & Diagnostic Algorithm (p339) — 4 questions

### Chapter 4: Fetal Surveillance and Maternal Adaptations
- **Page range**: Book pages 340–357 (PDF pages 14–31 of Part 2)
- **Total questions**: **65** (`OBG-C4-001` through `OBG-C4-065`)
- **Total units**: **15** (`OBG-U4-1` through `OBG-U4-15`)
- **Units outline**:
  1. Unit 1: Invasive Prenatal Diagnostic Procedures: CVS vs Amniocentesis (p340) — 6 questions
  2. Unit 2: Amniocentesis Technique, Cordocentesis & Fetal Blood (p341) — 5 questions
  3. Unit 3: Antepartum Fetal Surveillance Principles & Movement Counts (p342) — 4 questions
  4. Unit 4: Non-Stress Test (NST): Setup, Baseline & Accelerations (p343-344) — 5 questions
  5. Unit 5: Sinusoidal FHR, Non-Reactive Tracings & Algorithm (p344-345) — 4 questions
  6. Unit 6: Biophysical Profile (BPP / Manning Score) & Modified BPS (p345-346) — 5 questions
  7. Unit 7: Intrapartum Surveillance Principles & Intermittent Auscultation (p347-348) — 4 questions
  8. Unit 8: Cardiotocography: Baseline, Variability & Prolonged Decelerations (p348-349) — 4 questions
  9. Unit 9: Deceleration Morphologies: Early, Late & Variable Decelerations (p350-351) — 4 questions
  10. Unit 10: CTG Categorization (ACOG/FIGO) & Intrauterine Resuscitation (p351) — 3 questions
  11. Unit 11: Fetal Scalp Blood Sampling, Scalp Stimulation & Pulse Oximetry (p352) — 4 questions
  12. Unit 12: Maternal Adaptations: Cutaneous, Uterine & Cervical Shifts (p353-354) — 4 questions
  13. Unit 13: Vaginal Ecosystem, Endocrine Shifts & Fluid Retention (p354-355) — 4 questions
  14. Unit 14: Maternal Hematological Adaptations & Hemodilution (p356) — 5 questions
  15. Unit 15: Maternal Renal, Urinary & Gastrointestinal Adaptations (p356-357) — 4 questions

### Chapter 5: Medical Disorders: Anemia, Drugs and Heart Disease
- **Page range**: Book pages 358–374 (PDF pages 32–48 of Part 2)
- **Total questions**: **70** (`OBG-C5-001` through `OBG-C5-070`)
- **Total units**: **18** (`OBG-U5-1` through `OBG-U5-18`)
- **Units outline**:
  1. Unit 1: Maternal Respiratory Adaptations & Thoracic Anatomy (p358) — 5 questions
  2. Unit 2: Maternal Oxygen Dynamics, Endocrine & Visceral Changes (p358) — 3 questions
  3. Unit 3: Iron Requirements, Metabolism & Anemia Mukt Bharat / I-NIPI (p359-360) — 4 questions
  4. Unit 4: IFA Supplementation Rules & Anemia Definitions (p360-361) — 4 questions
  5. Unit 5: Maternal & Fetal Complications of Anemia in Pregnancy (p361-362) — 4 questions
  6. Unit 6: Clinical Evaluation & Physical Workup of Gestational Anemia (p362-363) — 4 questions
  7. Unit 7: Diagnostic RBC Indices & Iron Profile Interpretation (p363-364) — 4 questions
  8. Unit 8: Oral Iron Therapy & Assessing Treatment Response (p365) — 4 questions
  9. Unit 9: Parenteral Iron Therapy, Ganzoni Formula & Blood Transfusion (p366-367) — 4 questions
  10. Unit 10: Trimester-Wise Gestational Management Protocol for Anemia (p367) — 3 questions
  11. Unit 11: Antimicrobial Safety & Teratogenic Hazards in Pregnancy (p368) — 4 questions
  12. Unit 12: Anticoagulation: LMWH, Warfarin & Mechanical Valves (p368-369) — 4 questions
  13. Unit 13: Warfarin Embryopathy (DiSaia Syndrome) & Antiepileptics (p369) — 3 questions
  14. Unit 14: Maternal Cardiovascular Hemodynamics & Peak Stress Periods (p370) — 4 questions
  15. Unit 15: Heart Failure vs Pregnancy Signs, RHD & Congenital Lesions (p370-371) — 4 questions
  16. Unit 16: Lesion Prognosis & WHO Class IV Contraindications (p371) — 4 questions
  17. Unit 17: Intrapartum & Postpartum Management of Heart Disease (p372) — 4 questions
  18. Unit 18: Peripartum Cardiomyopathy & Mitral Stenosis Management (p373-374) — 4 questions

---

## Validation Status
- Total live chapters: **5** (Chapters 1 to 5)
- Total questions: **538**
- Total units: **91**
- Contiguous question IDs for all chapters: **PASS**
- Exactly 4 options per question: **PASS**
- Valid answer index (0–3): **PASS**
- 100% question coverage by units exactly once: **PASS**
- Strict book order preservation: **PASS**
- All question explanations end with `(Book pX)`: **PASS**
- JavaScript syntax and DOM integrity: **PASS**

## Status
- **DONE**:
  - Chapter 1: Fundamentals of Reproduction (235 questions, 28 units, Book p265–301)
  - Chapter 2: Normal Pregnancy and Antenatal Care (107 questions, 18 units, Book p302–326)
  - Chapter 3: Fetal Assessment and Ultrasound (61 questions, 12 units, Book p327–339)
  - Chapter 4: Fetal Surveillance and Maternal Adaptations (65 questions, 15 units, Book p340–357)
  - Chapter 5: Medical Disorders: Anemia, Drugs and Heart Disease (70 questions, 18 units, Book p358–374)
- **NEXT**: Chapter 6: Operative Obstetrics and Induction of Labor (Book p375+)
- **Roadmap**: Chapters 1–5 are Live; Chapters 6–24 marked as "Soon" until transcribed.

## Live Links
- GitHub Pages live link: `https://deva20045.github.io/OBG/` (redirects to `pulse-obg.html`).
- Direct app URL: `https://deva20045.github.io/OBG/pulse-obg.html`.

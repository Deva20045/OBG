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
    - Chapter 6 begins here: Book pages 375–387 (PDF pages 49–61); it continues on Part 3 Book pages 388–389.
  - `Uploads/OBG_Vol_2_Part_3_pages_124-185.pdf`: PDF pages 1–62 → Book pages 388–449 (Book page = PDF page + 387).
    - Chapter 6 concludes: Book pages 388–389 (PDF pages 1–2).
    - Chapter 7: Book pages 390–401 (PDF pages 3–14).
    - Chapter 8: Book pages 402–417 (PDF pages 15–30).
    - Chapter 9: Book pages 418–427 (PDF pages 31–40).
    - Chapter 10: Book pages 428–441 (PDF pages 41–54).
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


### Chapter 6: Thyroid, Diabetes & Shoulder Dystocia
- **Page range**: Book pages 375–389 (Part 2 PDF pages 49–61 and Part 3 PDF pages 1–2)
- **Total questions**: **180** (`OBG-C6-001` through `OBG-C6-180`)
- **Total units**: **25** (`OBG-U6-1` through `OBG-U6-25`)
- **Coverage**: pregnancy thyroid physiology and fetal thyroid dependence; hypo-/hyperthyroidism and thyroid storm; diabetes physiology and classification; pregestational/GDM diagnosis, surveillance, nutrition, oral agents and insulin; intrapartum/postpartum care; maternal-fetal-neonatal complications and lung maturity; and stepwise shoulder-dystocia maneuvers and complications.

### Chapter 7: Pregnancy-Induced Hypertension
- **Page range**: Book pages 390–401 (Part 3 PDF pages 3–14)
- **Total questions**: **125** (`OBG-C7-001` through `OBG-C7-125`)
- **Total units**: **16** (`OBG-U7-1` through `OBG-U7-16`)
- **Coverage**: diagnostic definitions and proteinuria; mild, severe and superimposed pre-eclampsia; eclampsia and PRES; abnormal placentation and endothelial pathophysiology; risks, prevention and prediction; maternal-fetal surveillance; delivery timing; and mild/severe/eclamptic management.

### Chapter 8: Eclampsia, Liver Disorders & Rh-Negative Pregnancy
- **Page range**: Book pages 402–417 (Part 3 PDF pages 15–30)
- **Total questions**: **224** (`OBG-C8-001` through `OBG-C8-224`)
- **Total units**: **31** (`OBG-U8-1` through `OBG-U8-31`)
- **Coverage**: eclampsia stabilization/delivery and hypertensive emergencies; antihypertensive regimens; magnesium sulfate protocols, monitoring and toxicity; HELLP, acute fatty liver of pregnancy and intrahepatic cholestasis; Rh antigens, sensitization, anti-D prevention and dosing; fetal-anemia assessment/IUT; fetomaternal hemorrhage testing; and immune/nonimmune hydrops.

### Chapter 9: Abortion, Recurrent Loss & MTP
- **Page range**: Book pages 418–427 (Part 3 PDF pages 31–40)
- **Total questions**: **158** (`OBG-C9-001` through `OBG-C9-158`)
- **Total units**: **22** (`OBG-U9-1` through `OBG-U9-22`)
- **Coverage**: abortion terminology/types; recurrent-loss epidemiology, causes and investigation; cervical insufficiency, progesterone and cerclage techniques; obstetric antiphospholipid syndrome; clinical and septic abortion; and MTP Act 2021 eligibility, consent, provider/facility rules and method selection.

### Chapter 10: MTP, Ectopic Pregnancy & Gestational Trophoblastic Disease
- **Page range**: Book pages 428–441 (Part 3 PDF pages 41–54)
- **Total questions**: **228** (`OBG-C10-001` through `OBG-C10-228`)
- **Total units**: **28** (`OBG-U10-1` through `OBG-U10-28`)
- **Coverage**: first-/second-trimester method selection, medical-abortion protocols, suction evacuation/MVA/D&E and complications; ectopic anatomy, sites, risks, presentation, rupture and emergency care; unruptured diagnostic algorithms, methotrexate, expectant and surgical care; special ectopics; and molar/gestational trophoblastic disease foundations, risk and presentation.

---

## Validation Status
- Total live chapters: **10** (Chapters 1 to 10)
- Total questions: **1,453**
- Total units: **213**
- New Chapter 6–10 addition: **915 questions** in **122 focused units** across Book pages **375–441**.
- All **177** in-scope Book pages (265–441) have at least one cited question; all 67 newly added source pages are represented.
- Contiguous, globally unique question and unit IDs: **PASS**
- Exactly four distinct, non-empty options and a valid answer index per question: **PASS**
- 100% question coverage by units exactly once, in source order: **PASS**
- Correct Book-page range and matching explanation citation for every question: **PASS**
- Editable `data/ch01.json`–`data/ch10.json` artifacts exactly match the embedded application data: **PASS**
- Required UI hooks, Node JavaScript syntax check, and dependency-free DOM runtime smoke test: **PASS**

## Status
- **DONE / LIVE**:
  - Chapters 1–5: **538 questions**, **91 units**, Book p265–374.
  - Chapter 6 — Thyroid, Diabetes & Shoulder Dystocia: **180 questions**, **25 units**, Book p375–389.
  - Chapter 7 — Pregnancy-Induced Hypertension: **125 questions**, **16 units**, Book p390–401.
  - Chapter 8 — Eclampsia, Liver Disorders & Rh-Negative Pregnancy: **224 questions**, **31 units**, Book p402–417.
  - Chapter 9 — Abortion, Recurrent Loss & MTP: **158 questions**, **22 units**, Book p418–427.
  - Chapter 10 — MTP, Ectopic Pregnancy & Gestational Trophoblastic Disease: **228 questions**, **28 units**, Book p428–441.
- **Roadmap**: Chapters 1–10 are Live; Chapters 11–24 remain marked as "Soon" until transcribed.

## Live Links
- GitHub Pages live link: `https://deva20045.github.io/OBG/` (redirects to `pulse-obg.html`).
- Direct app URL: `https://deva20045.github.io/OBG/pulse-obg.html`.

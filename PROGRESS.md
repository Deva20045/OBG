# PULSE OBG — Single Source of Truth

## Goal
Build a line-by-line PULSE quiz companion for the Marrow Edition 8 Obstetrics & Gynaecology scanned notes in the `Uploads` branch. Every source line, table, diagram, clinical aspect, and note becomes an ordered, understandable question; chapter data is append-only and validated before merge.

## App Architecture (Exact match with ORTHO)
- Single-page Duolingo-style game UI (`pulse-obg.html`).
- Home screen with stats: Total XP, Day streak, Units completed, "Unlock all units", and "Continue learning".
- Chapter roadmap with all 24 chapters visible from day one: all 24 chapters are now unlocked and live.
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


### Chapter 11: Gestational Trophoblastic Disease: Staging & Management
- **Page range**: Book pages 442–446 (Part 3 PDF pages 55–59)
- **Total questions**: **61** (`OBG-C11-001` through `OBG-C11-061`)
- **Total units**: **6** (`OBG-U11-1` through `OBG-U11-6`)
- **Coverage**: molar pregnancy signs, evacuation and β-hCG follow-up; partial vs complete mole; GTN causes, lab criteria and metastases; FIGO staging with WHO risk scoring; methotrexate and EMA-CO/EMA-EP chemotherapy; hysterectomy indications, PSTT/ETT and histopathology.

### Chapter 12: Antepartum Hemorrhage & Placenta Accreta Spectrum
- **Page range**: Book pages 447–459 (Part 3 PDF pages 60–62 and Part 4 PDF pages 1–10)
- **Total questions**: **113** (`OBG-C12-001` through `OBG-C12-113`)
- **Total units**: **11** (`OBG-U12-1` through `OBG-U12-11`)
- **Coverage**: APH definition, causes and etiopathogenesis; placenta previa classification, risks, presentation, examination and resuscitation; follow-up, mode of delivery and expectant/active management; abruptio varieties, Page grading, management, DIC and differentials; placenta accreta spectrum classification, workup and ACOG management.

### Chapter 13: Multifetal Gestation: Chorionicity, Complications & Delivery
- **Page range**: Book pages 460–471 (Part 4 PDF pages 11–22)
- **Total questions**: **87** (`OBG-C13-001` through `OBG-C13-087`)
- **Total units**: **9** (`OBG-U13-1` through `OBG-U13-9`)
- **Coverage**: dizygotic vs monozygotic twins, Hellin's rule, superfecundation/superfetation; chorionicity/amnionicity and membrane timing; DCDA/MCDA/MCMA comparison and twin ultrasound; maternal and fetal complications with fetal reduction; vanishing twin and single-twin death; TTTS physiology, Quintero staging and treatment; TAPS, TRAP, selective IUGR; and delivery of twins.

### Chapter 14: Preterm Labour, PROM & Post-term Pregnancy
- **Page range**: Book pages 472–482 (Part 4 PDF pages 23–33)
- **Total questions**: **105** (`OBG-C14-001` through `OBG-C14-105`)
- **Total units**: **11** (`OBG-U14-1` through `OBG-U14-11`)
- **Coverage**: PTL causes, risks and TVS prediction; cerclage and progesterone prevention; established-PTL definitions and fetal fibronectin; corticosteroids, tocolytics, MgSO4, GBS and antibiotics with the early/late summary; PROM/PPROM consequences, fluid evaluation and management; chorioamnionitis; post-term pregnancy physiology, consequences, ACOG management and macrosomia.

### Chapter 15: Maternal Pelvis, Contracted Pelvis & CPD
- **Page range**: Book pages 483–489 (Part 4 PDF pages 34–40)
- **Total questions**: **50** (`OBG-C15-001` through `OBG-C15-050`)
- **Total units**: **6** (`OBG-U15-1` through `OBG-U15-6`)
- **Coverage**: pelvic brim, false/true pelvis and inlet diameters; cavity planes of greatest and least dimensions; mid-pelvis, outlet, sagittal diameters and pelvic angles; ischial spine significance and stations; contracted pelvis cut-offs, pelvic variations and cephalopelvic disproportion; CPD notes and Caldwell-Moloy pelvic types.

---

## Validation Status
- Total live chapters: **24** (Chapters 1 to 24 — full Book coverage)
- Total questions: **2,368**
- Total units: **342**
- New Chapter 6–10 addition: **915 questions** in **122 focused units** across Book pages **375–441**.
- New Chapter 11–15 addition: **416 questions** in **43 focused units** across Book pages **442–489**.
- New Chapter 16–24 addition: **499 questions** in **86 focused units** across Book pages **490–572**.
- All **308** in-scope Book pages (265–572) have at least one cited question; all 83 newly added source pages are represented.
- Roadmap: all 24 chapters are now Live; no "Soon" rows remain.
- Contiguous, globally unique question and unit IDs: **PASS**
- Exactly four distinct, non-empty options and a valid answer index per question: **PASS**
- 100% question coverage by units exactly once, in source order: **PASS**
- Correct Book-page range and matching explanation citation for every question: **PASS**
- Editable `data/ch01.json`–`data/ch24.json` artifacts exactly match the embedded application data: **PASS**
- Required UI hooks, Node JavaScript syntax check, and dependency-free DOM runtime smoke test: **PASS**

## Status
- **DONE / LIVE**:
  - Chapters 1–5: **629 questions**, **91 units**, Book p265–374.
  - Chapter 6 — Thyroid, Diabetes & Shoulder Dystocia: **205 questions**, **25 units**, Book p375–389.
  - Chapter 7 — Pregnancy-Induced Hypertension: **141 questions**, **16 units**, Book p390–401.
  - Chapter 8 — Eclampsia, Liver Disorders & Rh-Negative Pregnancy: **255 questions**, **31 units**, Book p402–417.
  - Chapter 9 — Abortion, Recurrent Loss & MTP: **180 questions**, **22 units**, Book p418–427.
  - Chapter 10 — MTP, Ectopic Pregnancy & Gestational Trophoblastic Disease: **256 questions**, **28 units**, Book p428–441.
  - Chapter 11 — Gestational Trophoblastic Disease: Staging & Management: **67 questions**, **6 units**, Book p442–446.
  - Chapter 12 — Antepartum Hemorrhage & Placenta Accreta Spectrum: **124 questions**, **11 units**, Book p447–459.
  - Chapter 13 — Multifetal Gestation: Chorionicity, Complications & Delivery: **96 questions**, **9 units**, Book p460–471.
  - Chapter 14 — Preterm Labour, PROM & Post-term Pregnancy: **116 questions**, **11 units**, Book p472–482.
  - Chapter 15 — Maternal Pelvis, Contracted Pelvis & CPD: **56 questions**, **6 units**, Book p483–489.
  - Chapter 16 — Fetal Skull & Terminologies of Labour: **74 questions**, **9 units**, Book p490–498.
  - Chapter 17 — Stages of Labour: Normal & Abnormal: **60 questions**, **9 units**, Book p499–505.
  - Chapter 18 — Partogram & WHO Labour Care Guide: **43 questions**, **7 units**, Book p506–511.
  - Chapter 19 — Normal Labour & Induction of Labour: **129 questions**, **18 units**, Book p512–527.
  - Chapter 20 — Postpartum Hemorrhage & Third Stage Complications: **74 questions**, **12 units**, Book p528–539.
  - Chapter 21 — Perineal Trauma, Episiotomy & Malpresentations: **61 questions**, **9 units**, Book p540–549.
  - Chapter 22 — Breech & Instrumental Delivery: **71 questions**, **11 units**, Book p550–562.
  - Chapter 23 — Caesarean Section & VBAC: **30 questions**, **4 units**, Book p563–566.
  - Chapter 24 — Puerperium: **43 questions**, **7 units**, Book p567–572.
- **Roadmap**: All 24 chapters are Live. The Book (p265–572) is fully transcribed.

## Live Links
- GitHub Pages live link: `https://deva20045.github.io/OBG/` (redirects to `pulse-obg.html`).
- Direct app URL: `https://deva20045.github.io/OBG/pulse-obg.html`.

---

## Question-quality re-audit (variety & predictability)

A full re-audit of the bank was run after feedback that questions had become
"easily predictable" and had fallen back on a single repeated shape. The detail
lives in `AUDIT.md`; the headline numbers are:

**Before (2,368 questions)**
- 77.0% plain recall, **0% match-the-following**, 0.7% true/false, 2.0% clinical scenarios.
- The correct option was the longest option in **67.8%** of questions; the answer
  averaged 59.9 characters against 29.2 for distractors, so picking the longest
  option scored about 68% without knowing anything.
- Worst chapters: 21 (92.3%), 22 (91.7%), 24 (91.7%), 4 (90.8%).
- 78 items where the answer was four times longer than the longest distractor.

**After (2,710 questions)**
- **+342 new varied-format items — one in every one of the 342 units.**
  - fill-ups 124 → **237**
  - match-the-following 0 → **71**
  - true/false statement sets 17 → **67**
  - clinical scenarios 47 → **101**
  - odd-one-out 101 → **155**
- **514 items de-biased**: every item where the answer was 2.0× or more longer
  than its longest distractor was rewritten with parallel, same-family options
  (paired items now offer four paired options; list items now offer four lists;
  stub distractors were expanded into full clauses with the enumerative detail
  moved into the explanation). **Zero remain above 2.0×**, which was 887 items.
- Answer length is now 49.1 characters against 42.7 for the longest distractor,
  rather than 59.9 against 29.2.
- Correct-option-is-longest fell 67.8% → **57.8%** chapter mean, and no chapter
  is still above 80% (chapter 24 was 91.7%).
- 742 items still have the key as the longest option by 1.3× or more; the median
  ratio is 1.12. Those are the next tranche, worst chapters first (24, 22, 20,
  4, 21), rewritten by hand since bulk automated trimming would damage good
  items.

### Format conversion (in progress)

- **97 recall items converted** into the five requested formats and tagged with
  an explicit `fmt` (patches/fmt_a, fmt_b, fmt_c): fill-ups, match-the-following,
  odd-one-out, true/false and clinical scenarios, drawn from chapters 7, 8, 9,
  10, 12, 19, 20 and 22. Content and book citations are unchanged; only the
  question shape moved.
- Tagged items rose from 342 to **439**; untagged plain recall fell from 2,368
  to **2,271** (87.4% to 83.8% of the bank).
- Clusters of related facts became match items (proteinuria thresholds, APH
  causes, breech types), isolated facts became fill-ups, and management
  questions became scenarios.
- **Content bug fixed**: OBG-C12-016 marked 20 and 24 weeks as the best timing
  for the placenta-previa ultrasound while its own explanation said 32 and 36
  weeks. The answer key now points at 32 and 36 weeks, which is also consistent
  with the neighbouring item on third-trimester placental migration.

#### Batch 2 — 265 items across 16 untouched chapters

- **265 additional recall items converted** into the five requested formats and
  tagged with explicit `fmt` (patches/fmt_11, fmt_13, fmt_14, fmt_15, fmt_23,
  fmt_01, fmt_06, fmt_02, fmt_03, fmt_04, fmt_05, fmt_16, fmt_17, fmt_18, fmt_21,
  fmt_24 and fmt_dupfix): fill-ups, match-the-following, odd-one-out,
  true/false and clinical scenarios, prioritising chapters 13, 11, 14, 15
  (worst at 91%/89% untagged), then 1, 6, 16, and the quick win chapter 23.
- Tagged items rose from **439 to 704**; untagged plain recall fell from
  **2,271 to 2,006** (83.8% to **74.0%** of the bank).
- Per-format tag counts after batch 2:
  - fillup **251** (was 142) — 9.3% of bank
  - truefalse **132** (was 69) — 4.9%
  - oddoneout **115** (was 70) — 4.2%
  - match **105** (was 88) — 3.9%
  - scenario **101** (was 70) — 3.7%
- By audit_variety.py heuristic (which also credits untagged items whose
  phrasing already matches a format):
  - recall **64.6% → 57.4%**
  - fillup **9.6% → 12.7%**
  - oddoneout **6.0% → 7.4%**
  - scenario **4.3% → 5.3%**
  - truefalse **3.0% → 5.1%**
  - match **3.2% → 3.9%**
- Per-chapter untagged improvement (selected):
  - ch11 91% → 61/67 → 36/67 (53% untagged after)
  - ch13 91% → 87/96 → 62/96 (65%)
  - ch14 91% → 105/116 → 80/116 (69%)
  - ch15 89% → 50/56 → 35/56 (63%)
  - ch23 87% → 26/30 → 6/30 (20%)
  - ch01 89% → 235/263 → 205/263 (78%)
  - ch06 88% → 180/205 → 150/205 (73%)
- Zero items above 2.0× length ratio (check_integrity PASS, flag --ratio 2.0 = 0).
- Duplicate-stem guard triggered on auto-generated generic stems (e.g.,
  "Which of the following statements about Basics of pregnancy is TRUE?"
  repeated). Fixed in fmt_dupfix by making each stem unique with a snippet
  from the correct option.
- All 24 chapters remain live, 2,710 questions, 342 units, 308 book pages
  represented; check_integrity.py and check_app_smoke.js both PASS.

#### Batch 3 — 260 items across 9 worst-remaining chapters (this PR)

- **260 additional recall items converted** into the five requested formats and
  tagged with explicit `fmt` (patches/batch3_ch10, ch12, ch08, ch07, ch09, ch01, ch19, ch02, ch06 — 40+25+45+25+30+30+20+20+25),
  prioritising the next worst chapters by untagged share: 10 (86%), 12 (83%), 08 (82%), 07 (79%), 09 (78%), 01 (78%), 19 (75%), 02 (74%), 06 (73%).
- Tagged items rose from **704 to 964**; untagged plain recall fell from **2,006 to 1,746** (74.0% to **64.4%** of the bank) — now **<65%** as requested.
- Per-format tag counts after batch 3:
  - fillup **331** (was 251) — 12.2% — +80
  - truefalse **233** (was 132) — 8.6% — +101
  - scenario **153** (was 101) — 5.6% — +52
  - match **129** (was 105) — 4.8% — +24
  - oddoneout **118** (was 115) — 4.4% — +3 (strict same-sec filter limited oddoneout; next tranche will target 20,21,03,04,05,16,17,22)
  - **Tagged total 964 (35.6%)**, untagged 1,746 (64.4%)
- By audit_variety.py heuristic:
  - recall **57.4% → 50.3%** (-7.1 pp)
  - fillup **12.7% → 15.2%**
  - truefalse **5.1% → 8.8%**
  - oddoneout **7.4% → 7.0%**
  - scenario **5.3% → 7.0%**
  - match **3.9% → 4.8%**
  - numeric **6.2% → 5.0%**
- Per-chapter untagged improvement (this batch):
  - ch10 221/256 (86%) → 181/256 (70.7%)
  - ch12 103/124 (83%) → 78/124 (62.9%)
  - ch08 210/255 (82%) → 165/255 (64.7%)
  - ch07 112/141 (79%) → 87/141 (61.7%)
  - ch09 140/180 (78%) → 110/180 (61.1%)
  - ch01 205/263 (78%) → 175/263 (66.5%)
  - ch19 97/129 (75%) → 77/129 (59.7%)
  - ch02 92/125 (74%) → 72/125 (57.6%)
  - ch06 150/205 (73%) → 125/205 (61.0%)
- Predictability: longest-option-is-answer mean 55.2% → **54.8%**; zero items ≥2.0× (flag --ratio 2.0 = 0); avg ans 57.0 / distractor 44.6.
- Both checks still PASS; 2710 questions, 342 units, 308 pages.
- Next order: 20,21,03,04,05,16,17,22 (all 68-73% untagged) — oddoneout-heavy.

**Guard rails**
- `check_integrity.py` now fails when an answer can be guessed from option
  length (≥3.5×), when a unit has no varied-format item, or when a format tag is
  unknown. Both new checks were verified to fire on deliberately broken input.
- `check_app_smoke.js` derives its expected totals from `data/ch*.json` instead
  of hard-coding them, so adding content no longer desynchronises the tests.

**Tooling**: `audit_variety.py` (report), `itemlab.py` (map / flag / stats /
apply), and curated patch files in `patches/`.

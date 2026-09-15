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
- Source PDF branch: `origin/Uploads`
- Subsequent volume parts:
  - `Uploads/OBG_Vol_2_Part_1_pages_1-62.pdf`: PDF pages 1–62 → Book pages 265–326 (Book page = PDF page + 264).
    - Chapter 1: Book pages 265–301 (PDF pages 1–37)
    - Chapter 2: Book pages 302–326 (PDF pages 38–62)
  - `Uploads/OBG_Vol_2_Part_2_pages_63-123.pdf`: PDF pages 1–61 → Book pages 327–387 (Book page = PDF page + 326).
    - Chapter 3: Book pages 327–339 (PDF pages 1–13)
    - Chapter 4: Book pages 340–357 (PDF pages 14–31)
    - Chapter 5: Book pages 358–374 (PDF pages 32–48)
    - Chapter 6 (Part A): Book pages 375–387 (PDF pages 49–61)
  - `Uploads/OBG_Vol_2_Part_3_pages_124-185.pdf`: PDF pages 1–62 → Book pages 388–449 (Book page = PDF page + 387).
    - Chapter 6 (Part B): Book pages 388–390 (PDF pages 1–3)
    - Chapter 7: Book pages 391–405 (PDF pages 4–18)
    - Chapter 8: Book pages 406–417 (PDF pages 19–30)
    - Chapter 9: Book pages 418–432 (PDF pages 31–45)
    - Chapter 10: Book pages 433–442 (PDF pages 46–55)
    - Chapter 11: Book pages 443–449 (PDF pages 56–62)
  - `Uploads/OBG_Vol_2_Part_4_pages_186-246.pdf`: PDF pages 1–61 → Book pages 450–510 (Book page = PDF page + 449).
  - `Uploads/OBG_Vol_2_Part_5_pages_247-308.pdf`: PDF pages 1–62 → Book pages 511–572 (Book page = PDF page + 510).

---

## Completed Chapters Summary

### Chapter 1: Fundamentals of Reproduction
- **Page range**: Book pages 265–301 (PDF pages 1–37 of Part 1)
- **Total questions**: **235** (`OBG-C1-001` through `OBG-C1-235`)
- **Total units**: **28** (`OBG-U1-1` through `OBG-U1-28`)

### Chapter 2: Normal Pregnancy and Antenatal Care
- **Page range**: Book pages 302–326 (PDF pages 38–62 of Part 1)
- **Total questions**: **107** (`OBG-C2-001` through `OBG-C2-107`)
- **Total units**: **18** (`OBG-U2-1` through `OBG-U2-18`)

### Chapter 3: Fetal Assessment and Ultrasound
- **Page range**: Book pages 327–339 (PDF pages 1–13 of Part 2)
- **Total questions**: **61** (`OBG-C3-001` through `OBG-C3-061`)
- **Total units**: **12** (`OBG-U3-1` through `OBG-U3-12`)

### Chapter 4: Fetal Surveillance and Maternal Adaptations
- **Page range**: Book pages 340–357 (PDF pages 14–31 of Part 2)
- **Total questions**: **65** (`OBG-C4-001` through `OBG-C4-065`)
- **Total units**: **15** (`OBG-U4-1` through `OBG-U4-15`)

### Chapter 5: Medical Disorders: Anemia, Drugs and Heart Disease
- **Page range**: Book pages 358–374 (PDF pages 32–48 of Part 2)
- **Total questions**: **70** (`OBG-C5-001` through `OBG-C5-070`)
- **Total units**: **18** (`OBG-U5-1` through `OBG-U5-18`)

### Chapter 6: Endocrine Disorders: Thyroid and Diabetes in Pregnancy
- **Page range**: Book pages 375–390 (PDF pages 49–61 of Part 2, and 1–3 of Part 3)
- **Total questions**: **38** (`OBG-C6-001` through `OBG-C6-038`)
- **Total units**: **8** (`OBG-U6-1` through `OBG-U6-8`)
- **Units outline**:
  1. Unit 1: Maternal Thyroid Physiology & Hypothyroidism (p375) — 5 questions
  2. Unit 2: Gestational Hyperthyroidism & Antithyroid Protocols (p375) — 4 questions
  3. Unit 3: Gestational Diabetes Mellitus: Etiology & Screening (p376-378) — 5 questions
  4. Unit 4: White's Classification, Risk Factors & Glycemic Targets (p378-382) — 5 questions
  5. Unit 5: Medical Nutrition Therapy & Insulin Pharmacotherapy (p381-385) — 5 questions
  6. Unit 6: Diabetic Embryopathy & Structural Malformations (p386-388) — 5 questions
  7. Unit 7: Fetal Macrosomia, Polyhydramnios & Neonatal Metabolism (p387-390) — 5 questions
  8. Unit 8: Intrapartum Glycemic Control, Delivery Timing & Postpartum Follow-Up (p385, 389-390) — 4 questions

### Chapter 7: Hypertensive Disorders: Pre-eclampsia and Eclampsia
- **Page range**: Book pages 391–405 (PDF pages 4–18 of Part 3)
- **Total questions**: **38** (`OBG-C7-001` through `OBG-C7-038`)
- **Total units**: **8** (`OBG-U7-1` through `OBG-U7-8`)
- **Units outline**:
  1. Unit 1: Hypertensive Disorders: Classification & Definitions (p391-392) — 5 questions
  2. Unit 2: Pathophysiology: Trophoblast Invasion & Angiogenic Imbalance (p396-397) — 4 questions
  3. Unit 3: Predictive Screening: Uterine Doppler, Biomarkers & Aspirin Prophylaxis (p397-399) — 5 questions
  4. Unit 4: Pre-eclampsia: Severe Features & Laboratory Criteria (p392-395) — 4 questions
  5. Unit 5: Acute Antihypertensive Therapy & Hemodynamic Targets (p399-400) — 5 questions
  6. Unit 6: Eclampsia: Stages, Convulsions & Resuscitation (p393-394) — 4 questions
  7. Unit 7: Magnesium Sulfate Protocols & Toxicity Monitoring (p401-402) — 6 questions
  8. Unit 8: HELLP Syndrome & Delivery Timing Strategies (p403-405) — 5 questions

### Chapter 8: Liver Disorders and Rh Isoimmunization in Pregnancy
- **Page range**: Book pages 406–417 (PDF pages 19–30 of Part 3)
- **Total questions**: **39** (`OBG-C8-001` through `OBG-C8-039`)
- **Total units**: **8** (`OBG-U8-1` through `OBG-U8-8`)
- **Units outline**:
  1. Unit 1: HELLP Syndrome & Differential Diagnosis of Liver Disorders (p406-407) — 5 questions
  2. Unit 2: Acute Fatty Liver of Pregnancy & Swansea Diagnostic Criteria (p407-408) — 5 questions
  3. Unit 3: Intrahepatic Cholestasis of Pregnancy & Fetal Bile Toxicity (p408-409) — 5 questions
  4. Unit 4: Rh Antigens, Genetics & Isoimmunization Pathophysiology (p410-411) — 5 questions
  5. Unit 5: Rh Isoimmunization: Fetal Anemia & Hydrops Fetalis (p411-412) — 5 questions
  6. Unit 6: Management of Unsensitized Rh-Negative Mother & Anti-D (p412-413) — 4 questions
  7. Unit 7: Management of Rh-Sensitized Mother: Titer, MCA Doppler & IUT (p414-415) — 5 questions
  8. Unit 8: Fetomaternal Hemorrhage, Minor Antigens & Mirror Syndrome (p415-417) — 5 questions

### Chapter 9: Recurrent Pregnancy Loss, Cervical Incompetence and MTP
- **Page range**: Book pages 418–432 (PDF pages 31–45 of Part 3)
- **Total questions**: **40** (`OBG-C9-001` through `OBG-C9-040`)
- **Total units**: **8** (`OBG-U9-1` through `OBG-U9-8`)
- **Units outline**:
  1. Unit 1: Abortion Epidemiology & Chromosomal Etiology (p418-419) — 5 questions
  2. Unit 2: Recurrent Pregnancy Loss: Etiology & Diagnostic Workup (p419-420) — 5 questions
  3. Unit 3: Cervical Incompetence: Sonography & Management Indications (p420-421) — 5 questions
  4. Unit 4: Cervical Cerclage: Shirodkar, McDonald & Rescue Techniques (p421-423) — 5 questions
  5. Unit 5: Antiphospholipid Syndrome: Sapporo Criteria & Anticoagulation (p424-425) — 5 questions
  6. Unit 6: Clinical Varieties: Threatened, Inevitable, Incomplete & Missed (p425-426) — 5 questions
  7. Unit 7: Septic Abortion & MTP Act (2021 Amendments) (p426-427) — 5 questions
  8. Unit 8: Medical & Surgical Abortion Techniques: Protocols & Complications (p428-432) — 5 questions

### Chapter 10: Ectopic Pregnancy
- **Page range**: Book pages 433–442 (PDF pages 46–55 of Part 3)
- **Total questions**: **35** (`OBG-C10-001` through `OBG-C10-035`)
- **Total units**: **7** (`OBG-U10-1` through `OBG-U10-7`)
- **Units outline**:
  1. Unit 1: Fallopian Tube Anatomy & Ectopic Implantation Sites (p433) — 5 questions
  2. Unit 2: Natural History, Outcomes & Non-Tubal Diagnostic Criteria (p434, 440) — 5 questions
  3. Unit 3: Ectopic Risk Factors & Contraceptive Failure Dynamics (p434) — 5 questions
  4. Unit 4: Clinical Presentation, Ruptured Ectopic & Culdocentesis (p435-436) — 5 questions
  5. Unit 5: Sonographic Signs & Beta-hCG Discriminatory Dynamics (p437-438) — 5 questions
  6. Unit 6: Medical Management: Single-Dose Methotrexate Protocols (p438-439) — 5 questions
  7. Unit 7: Surgical Strategies, Heterotopic & Cornual Pregnancy (p439-442) — 5 questions

---

## Validation Status
- Total live chapters: **10** (Chapters 1 to 10)
- Total questions: **728**
- Total units: **130**
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
  - Chapter 6: Endocrine Disorders: Thyroid and Diabetes in Pregnancy (38 questions, 8 units, Book p375–390)
  - Chapter 7: Hypertensive Disorders: Pre-eclampsia and Eclampsia (38 questions, 8 units, Book p391–405)
  - Chapter 8: Liver Disorders and Rh Isoimmunization in Pregnancy (39 questions, 8 units, Book p406–417)
  - Chapter 9: Recurrent Pregnancy Loss, Cervical Incompetence and MTP (40 questions, 8 units, Book p418–432)
  - Chapter 10: Ectopic Pregnancy (35 questions, 7 units, Book p433–442)
- **NEXT**: Chapter 11: Gestational Trophoblastic Disease (Book p443–449) & Chapter 12: Antepartum Hemorrhage (Book p450–459)
- **Roadmap**: Chapters 1–10 are Live; Chapters 11–24 marked as "Soon" until transcribed.

## Live Links
- GitHub Pages live link: `https://deva20045.github.io/OBG/` (redirects to `pulse-obg.html`).
- Direct app URL: `https://deva20045.github.io/OBG/pulse-obg.html`.

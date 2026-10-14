from typing import List, Optional, Dict, Any

VERIFIED_MEDICINES: List[Dict[str, Any]] = [
    {
        "id": "paracetamol",
        "name": "Paracetamol (Acetaminophen)",
        "generic_name": "Paracetamol / Acetaminophen",
        "drug_class": "Analgesic and Antipyretic",
        "common_uses": [
            "Temporary relief of mild to moderate pain (headaches, muscular aches, toothaches)",
            "Reduction of fever associated with common viral colds and infections"
        ],
        "standard_precautions": [
            "Always follow package directions or a doctor's advice. Do not exceed the maximum daily limit (typically 3,000 mg to 4,000 mg in 24 hours for healthy adults).",
            "Be vigilant: many multi-symptom cold products also contain acetaminophen; combining them can cause accidental toxic overdose.",
            "Avoid consuming alcohol while taking this medicine due to heightened liver stress."
        ],
        "possible_side_effects": [
            "Rare at therapeutic doses. Mild nausea, allergic skin reaction, or stomach upset can occasionally occur.",
            "Serious: signs of liver toxicity (dark urine, jaundice, extreme fatigue, upper right abdominal pain) occur with overdose."
        ],
        "contraindications_and_warnings": [
            "Do not use if you have severe active liver disease or known severe hypersensitivity.",
            "Consult a physician or pharmacist before taking if you have chronic liver or kidney impairment."
        ],
        "storage_info": "Store at controlled room temperature (20°C to 25°C / 68°F to 77°F) away from excessive heat and moisture.",
        "is_prescription_only": False,
        "verified_source": "NIH MedlinePlus & WHO Model List of Essential Medicines",
        "source_url": "https://medlineplus.gov/druginfo/meds/a681004.html"
    },
    {
        "id": "ibuprofen",
        "name": "Ibuprofen",
        "generic_name": "Ibuprofen",
        "drug_class": "Nonsteroidal Anti-inflammatory Drug (NSAID)",
        "common_uses": [
            "Relief of pain, inflammation, and swelling (arthritis, menstrual cramps, dental pain)",
            "Temporary reduction of fever"
        ],
        "standard_precautions": [
            "Take with food, milk, or a full glass of water to minimize stomach irritation.",
            "Use the lowest effective dose for the shortest duration necessary.",
            "Do not combine with other NSAIDs (e.g., naproxen, high-dose aspirin) without medical supervision."
        ],
        "possible_side_effects": [
            "Common: Indigestion, heartburn, stomach discomfort, nausea, dizziness.",
            "Serious: Gastrointestinal bleeding or ulceration, fluid retention, worsening high blood pressure, kidney impairment."
        ],
        "contraindications_and_warnings": [
            "Contraindicated immediately before or after heart bypass surgery (CABG).",
            "Avoid if you have an active stomach ulcer, severe kidney failure, severe heart failure, or history of aspirin-induced asthma."
        ],
        "storage_info": "Store in a tightly closed container away from heat, direct light, and children.",
        "is_prescription_only": False,
        "verified_source": "NHS Medicines A-Z & FDA Drug Information",
        "source_url": "https://www.nhs.uk/medicines/ibuprofen-for-adults/"
    },
    {
        "id": "cetirizine",
        "name": "Cetirizine",
        "generic_name": "Cetirizine Hydrochloride",
        "drug_class": "Second-Generation Antihistamine",
        "common_uses": [
            "Relief of seasonal allergy symptoms (hay fever, allergic rhinitis) including sneezing, runny nose, itchy and watery eyes",
            "Relief of itching and hives caused by chronic urticaria"
        ],
        "standard_precautions": [
            "While less sedating than first-generation antihistamines, it can still cause drowsiness in some individuals.",
            "Exercise caution when driving or operating machinery until you know how you respond.",
            "Avoid alcohol and other central nervous system depressants while taking this medication."
        ],
        "possible_side_effects": [
            "Drowsiness, fatigue, dry mouth, headache, sore throat.",
            "Rare: Rapid heartbeat, dizziness, urinary retention."
        ],
        "contraindications_and_warnings": [
            "Avoid if you have known allergy to cetirizine, hydroxyzine, or levocetirizine.",
            "Dose adjustment may be required for individuals with moderate-to-severe renal impairment."
        ],
        "storage_info": "Store at 20°C to 25°C away from moisture and direct sunlight.",
        "is_prescription_only": False,
        "verified_source": "NIH MedlinePlus Drug Information",
        "source_url": "https://medlineplus.gov/druginfo/meds/a698026.html"
    },
    {
        "id": "ors",
        "name": "Oral Rehydration Salts (ORS)",
        "generic_name": "Sodium Chloride, Potassium Chloride, Sodium Citrate, and Dextrose",
        "drug_class": "Electrolyte and Fluid Replacement",
        "common_uses": [
            "Prevention and treatment of dehydration caused by acute diarrhea or vomiting in children and adults",
            "Replenishment of essential electrolytes during intense heat exposure or heavy perspiration"
        ],
        "standard_precautions": [
            "Always dissolve the exact sachet in the precise volume of clean drinking water specified on the packet (usually 1 liter). Do not add sugar or excess salt.",
            "Sip slowly in small, frequent amounts. Once prepared, consume within 24 hours (or 12 hours if kept at room temperature in warm climates)."
        ],
        "possible_side_effects": [
            "Extremely safe when mixed properly. Mild nausea or vomiting if consumed too rapidly.",
            "Over-concentration (using too little water) can lead to hypernatremia (high sodium levels)."
        ],
        "contraindications_and_warnings": [
            "Severe persistent vomiting where oral intake is completely impossible requires immediate intravenous fluid resuscitation at a hospital.",
            "Use with clinical guidance in severe kidney disease."
        ],
        "storage_info": "Store unmixed dry packets in a cool, dry place. Discard any reconstituted fluid remaining after 24 hours.",
        "is_prescription_only": False,
        "verified_source": "WHO Guidelines on Clinical Management of Acute Diarrhoea",
        "source_url": "https://www.who.int/publications/i/item/9789241594981"
    },
    {
        "id": "omeprazole",
        "name": "Omeprazole",
        "generic_name": "Omeprazole",
        "drug_class": "Proton Pump Inhibitor (PPI)",
        "common_uses": [
            "Treatment of gastroesophageal reflux disease (GERD) and frequent heartburn",
            "Healing of gastric and duodenal ulcers, and prevention of NSAID-induced ulcers"
        ],
        "standard_precautions": [
            "Usually taken once daily in the morning, 30 to 60 minutes before a meal.",
            "Swallow capsules or tablets whole; do not crush, chew, or open delayed-release formulations.",
            "Over-the-counter courses should generally not exceed 14 consecutive days without medical supervision."
        ],
        "possible_side_effects": [
            "Headache, stomach pain, nausea, diarrhea, constipation, flatulence.",
            "Long-term use warnings: potential decrease in magnesium levels, reduced calcium absorption, increased risk of bone fractures and intestinal infections (C. difficile)."
        ],
        "contraindications_and_warnings": [
            "Do not use if allergic to omeprazole or other PPIs (pantoprazole, esomeprazole).",
            "Can interact with clopidogrel, diazepam, methotrexate, and certain antifungal drugs."
        ],
        "storage_info": "Store at room temperature (15°C to 30°C) protected from light and moisture.",
        "is_prescription_only": False,
        "verified_source": "FDA Drug Label & NHS Medicines A-Z",
        "source_url": "https://www.nhs.uk/medicines/omeprazole/"
    },
    {
        "id": "amoxicillin",
        "name": "Amoxicillin",
        "generic_name": "Amoxicillin",
        "drug_class": "Penicillin-type Antibiotic (Beta-lactam)",
        "common_uses": [
            "Treatment of confirmed bacterial infections (middle ear infections, bacterial sinusitis, pneumonia, strep throat, urinary tract infections)",
            "Part of combination therapy for Helicobacter pylori eradication"
        ],
        "standard_precautions": [
            "PRESCRIPTION ONLY. Must only be taken when prescribed by a licensed healthcare provider.",
            "Complete the entire prescribed course, even if feeling better after 2 days, to prevent antibiotic resistance.",
            "Ineffective against viral infections such as colds, COVID-19, or influenza."
        ],
        "possible_side_effects": [
            "Nausea, vomiting, mild diarrhea, mild skin rash.",
            "Severe: Anaphylactic allergic reactions (hives, difficulty breathing, throat swelling) require immediate emergency intervention. Clostridioides difficile-associated severe diarrhea."
        ],
        "contraindications_and_warnings": [
            "Strictly contraindicated in individuals with a history of severe allergic reactions (anaphylaxis) to penicillin or cephalosporins."
        ],
        "storage_info": "Tablets/capsules: store at room temperature. Liquid suspensions usually require refrigeration after mixing and expire after 14 days.",
        "is_prescription_only": True,
        "verified_source": "WHO Essential Medicines & FDA Prescribing Information",
        "source_url": "https://medlineplus.gov/druginfo/meds/a685001.html"
    },
    {
        "id": "metformin",
        "name": "Metformin",
        "generic_name": "Metformin Hydrochloride",
        "drug_class": "Biguanide Antihyperglycemic Agent",
        "common_uses": [
            "First-line prescription medication for glycemic management in Type 2 Diabetes Mellitus",
            "Improves insulin sensitivity and reduces hepatic glucose production"
        ],
        "standard_precautions": [
            "PRESCRIPTION ONLY. Take strictly as directed by your physician.",
            "Take with meals to reduce gastrointestinal side effects such as nausea and diarrhea.",
            "Drink plenty of fluids while taking metformin."
        ],
        "possible_side_effects": [
            "Common: Nausea, diarrhea, stomach cramping, metallic taste, decreased appetite.",
            "Serious but rare: Lactic acidosis (muscle pain, trouble breathing, stomach discomfort, dizziness, coldness)."
        ],
        "contraindications_and_warnings": [
            "Contraindicated in severe renal impairment (eGFR < 30 mL/min/1.73 m²), acute metabolic acidosis, or severe hypoxemia.",
            "Must be temporarily paused before certain radiological imaging procedures involving iodinated contrast dye."
        ],
        "storage_info": "Store at 20°C to 25°C away from excessive moisture.",
        "is_prescription_only": True,
        "verified_source": "American Diabetes Association Standards of Medical Care & FDA",
        "source_url": "https://medlineplus.gov/druginfo/meds/a684240.html"
    },
    {
        "id": "amlodipine",
        "name": "Amlodipine",
        "generic_name": "Amlodipine Besylate",
        "drug_class": "Dihydropyridine Calcium Channel Blocker",
        "common_uses": [
            "Treatment of hypertension (high blood pressure) to reduce risk of cardiovascular events",
            "Management of chronic stable angina and vasospastic (Prinzmetal's) angina"
        ],
        "standard_precautions": [
            "PRESCRIPTION ONLY. Do not stop taking abruptly without consulting your physician.",
            "May be taken with or without food, at the same time each day.",
            "Monitor blood pressure regularly."
        ],
        "possible_side_effects": [
            "Peripheral edema (swelling of lower legs, ankles, or feet)",
            "Dizziness, lightheadedness upon standing, flushing, fatigue, palpitations"
        ],
        "contraindications_and_warnings": [
            "Use with caution in patients with severe aortic stenosis or severe hepatic impairment.",
            "Avoid heavy alcohol consumption as it can compound blood-pressure lowering effects."
        ],
        "storage_info": "Store between 15°C and 30°C in a tightly closed, light-resistant container.",
        "is_prescription_only": True,
        "verified_source": "NIH MedlinePlus & NHS Medicines Guide",
        "source_url": "https://www.nhs.uk/medicines/amlodipine/"
    },
    {
        "id": "salbutamol",
        "name": "Salbutamol (Albuterol)",
        "generic_name": "Salbutamol / Albuterol Sulfate",
        "drug_class": "Short-Acting Beta-2 Agonist (Bronchodilator)",
        "common_uses": [
            "Quick-relief bronchodilator for acute bronchospasm in asthma and COPD",
            "Prevention of exercise-induced bronchoconstriction"
        ],
        "standard_precautions": [
            "PRESCRIPTION ONLY. Use an appropriate spacer device if recommended for optimal lung delivery.",
            "If your rescue inhaler is needed more than twice a week for symptom relief, consult your doctor for preventative controller review."
        ],
        "possible_side_effects": [
            "Mild hand tremors, fast or pounding heart rate (tachycardia), nervousness, headache.",
            "Rare: Paradoxical bronchospasm (sudden worsening of breathing immediately after inhalation - requires emergency care)."
        ],
        "contraindications_and_warnings": [
            "Caution in cardiovascular disorders, arrhythmias, and hyperthyroidism."
        ],
        "storage_info": "Store inhaler between 15°C and 25°C away from direct sunlight, freezing, and open flames.",
        "is_prescription_only": True,
        "verified_source": "Global Initiative for Asthma (GINA) & FDA",
        "source_url": "https://medlineplus.gov/druginfo/meds/a682145.html"
    }
]

def search_medicines(query: Optional[str] = None) -> List[Dict[str, Any]]:
    if not query or not query.strip():
        return VERIFIED_MEDICINES
    q = query.lower().strip()
    return [
        m for m in VERIFIED_MEDICINES
        if q in m["name"].lower()
        or q in m["generic_name"].lower()
        or q in m["drug_class"].lower()
        or any(q in u.lower() for u in m["common_uses"])
        or any(q in s.lower() for s in m["possible_side_effects"])
    ]

def get_medicine_by_id(med_id: str) -> Optional[Dict[str, Any]]:
    for m in VERIFIED_MEDICINES:
        if m["id"] == med_id:
            return m
    return None


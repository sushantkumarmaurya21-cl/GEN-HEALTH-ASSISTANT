from typing import List, Optional, Dict, Any

EDUCATION_TOPICS: List[Dict[str, Any]] = [
    {
        "id": "fever",
        "title": "Fever Awareness & Care",
        "hindi_title": "बुखार जागरूकता और देखभाल",
        "category": "General Symptoms",
        "summary": "A fever is a temporary increase in your body temperature, often due to an illness. Having a fever is a sign that something out of the ordinary is going on inside your body.",
        "common_signs": [
            "Body temperature above 100.4°F (38°C)",
            "Sweating, chills, and shivering",
            "Headache and muscle aches",
            "Loss of appetite and mild dehydration",
            "General weakness and fatigue"
        ],
        "prevention_tips": [
            "Practice regular handwashing with soap and clean water.",
            "Avoid touching your nose, mouth, or eyes with unwashed hands.",
            "Cover your mouth and nose when coughing or sneezing.",
            "Stay up-to-date with recommended immunizations."
        ],
        "when_to_seek_care": [
            "Temperature exceeding 103°F (39.4°C) or lasting more than 3 consecutive days.",
            "Fever accompanied by a stiff neck, mental confusion, or extreme lethargy.",
            "Difficulty breathing or chest pain.",
            "In infants under 3 months with a rectal temperature of 100.4°F (38°C) or higher."
        ],
        "emergency_warning_signs": [
            "Seizures or convulsions",
            "Severe shortness of breath or blue lips",
            "Sudden rash with rapid spreading",
            "Inability to stay awake or severe disorientation"
        ],
        "reliable_references": [
            {"title": "CDC - Fever Guidance", "url": "https://www.cdc.gov"},
            {"title": "WHO - Managing Fever in Children and Adults", "url": "https://www.who.int"},
            {"title": "Mayo Clinic - Fever Overview", "url": "https://www.mayoclinic.org/diseases-conditions/fever/symptoms-causes/syc-20352759"}
        ]
    },
    {
        "id": "cold_cough",
        "title": "Common Cold & Cough",
        "hindi_title": "सामान्य सर्दी और खांसी",
        "category": "Respiratory",
        "summary": "The common cold is a viral infection of your nose and throat (upper respiratory tract). It's usually harmless, although it might not feel that way.",
        "common_signs": [
            "Runny or stuffy nose",
            "Sore or scratchy throat",
            "Cough and mild sneezing",
            "Mild body aches or a dull headache",
            "Low-grade fever and general malaise"
        ],
        "prevention_tips": [
            "Wash hands frequently with soap and warm water for at least 20 seconds.",
            "Disinfect high-touch surfaces like doorknobs, light switches, and mobile devices.",
            "Stay hydrated with warm broths, herbal teas, and water.",
            "Avoid close contact with individuals who have active colds."
        ],
        "when_to_seek_care": [
            "Symptoms that worsen or fail to improve after 10 days.",
            "High fever or fever returning after a fever-free period.",
            "Shortness of breath, wheezing, or chest tightness.",
            "Severe sinus pain around the eyes and forehead."
        ],
        "emergency_warning_signs": [
            "Severe struggle to breathe or gasping for air",
            "Coughing up significant amounts of blood",
            "Persistent chest pressure or severe dizziness"
        ],
        "reliable_references": [
            {"title": "CDC - Common Colds: Protect Yourself and Others", "url": "https://www.cdc.gov/features/rhinoviruses/index.html"},
            {"title": "NHS - Common Cold Advice", "url": "https://www.nhs.uk/conditions/common-cold/"}
        ]
    },
    {
        "id": "headache",
        "title": "Headache Types & Relief",
        "hindi_title": "सिरदर्द: प्रकार और प्राथमिक देखभाल",
        "category": "Neurological",
        "summary": "Headaches are among the most common nervous system disorders. They range from tension headaches caused by stress or poor posture to migraines and cluster headaches.",
        "common_signs": [
            "Dull, aching head pain or sensation of a tight band around the head (Tension)",
            "Throbbing or pulsing pain, often on one side (Migraine)",
            "Sensitivity to light, sound, or certain odors",
            "Nausea or visual disturbances (aura)"
        ],
        "prevention_tips": [
            "Maintain regular sleep hours and consistent meal schedules.",
            "Stay adequately hydrated throughout the day.",
            "Take frequent screen breaks using the 20-20-20 rule.",
            "Manage stress through deep breathing, yoga, or gentle stretching."
        ],
        "when_to_seek_care": [
            "Headaches that become progressively more frequent or severe.",
            "A headache that disrupts daily activities or wakes you from sleep.",
            "Headaches beginning after age 50 without prior history.",
            "Headaches following a recent head injury."
        ],
        "emergency_warning_signs": [
            "Sudden, severe 'thunderclap' headache (worst headache of your life)",
            "Headache with sudden weakness, numbness, speech difficulty, or facial drooping (possible stroke)",
            "Headache with high fever, stiff neck, and confusion (possible meningitis)"
        ],
        "reliable_references": [
            {"title": "WHO - Headache Disorders Factsheet", "url": "https://www.who.int/news-room/fact-sheets/detail/headache-disorders"},
            {"title": "American Migraine Foundation", "url": "https://americanmigrainefoundation.org"}
        ]
    },
    {
        "id": "dehydration",
        "title": "Dehydration Prevention & Care",
        "hindi_title": "निर्जलीकरण (पानी की कमी) जागरूकता",
        "category": "Hydration & Metabolism",
        "summary": "Dehydration occurs when your body loses more fluids than you take in, disrupting the normal balance of minerals and water necessary for organ function.",
        "common_signs": [
            "Persistent thirst and dry, sticky mouth",
            "Dark yellow or amber-colored urine with reduced frequency",
            "Fatigue, dizziness, or lightheadedness upon standing",
            "Dry skin and sunken eyes",
            "Headache and muscle cramps"
        ],
        "prevention_tips": [
            "Drink 2 to 3 liters of fluids daily, adjusting for climate and physical activity.",
            "Use Oral Rehydration Salts (ORS) during episodes of diarrhea or vomiting.",
            "Consume water-rich fruits and vegetables like cucumbers, watermelon, and oranges.",
            "Drink extra water before, during, and after exercise."
        ],
        "when_to_seek_care": [
            "Inability to keep liquids down for more than 24 hours.",
            "Diarrhea or vomiting persisting for more than 2 days.",
            "Noticeable decrease in urine output or no urination for over 8 hours.",
            "Persistent dizziness or fainting."
        ],
        "emergency_warning_signs": [
            "Extreme confusion, lethargy, or loss of consciousness",
            "Rapid heart rate and shallow, rapid breathing",
            "Cold, clammy hands and feet with weak pulse (hypovolemic shock)"
        ],
        "reliable_references": [
            {"title": "WHO - Diarrhoea and Dehydration Treatment", "url": "https://www.who.int/news-room/fact-sheets/detail/diarrhoeal-disease"},
            {"title": "CDC - Water and Healthier Drinks", "url": "https://www.cdc.gov/healthyweight/healthy_eating/water-and-healthier-drinks.html"}
        ]
    },
    {
        "id": "diabetes_awareness",
        "title": "Diabetes Awareness & Management",
        "hindi_title": "मधुमेह (डायबिटीज) जागरूकता",
        "category": "Chronic Conditions",
        "summary": "Diabetes is a chronic metabolic disease characterized by elevated levels of blood glucose (blood sugar), which over time leads to serious damage to the heart, blood vessels, eyes, kidneys and nerves.",
        "common_signs": [
            "Increased thirst (polydipsia) and frequent urination (polyuria)",
            "Unexplained weight loss despite normal or increased hunger",
            "Chronic fatigue and blurred vision",
            "Slow-healing cuts, sores, or frequent infections",
            "Tingling, pain, or numbness in the hands or feet"
        ],
        "prevention_tips": [
            "Adopt a balanced diet rich in whole grains, fiber, and lean proteins while minimizing refined sugars.",
            "Engage in at least 150 minutes of moderate-intensity aerobic exercise per week.",
            "Maintain a healthy body weight through sustainable lifestyle habits.",
            "Get routine fasting blood glucose or HbA1c screenings, especially if over 35 or with family history."
        ],
        "when_to_seek_care": [
            "Fasting blood glucose readings consistently exceeding 126 mg/dL (7.0 mmol/L).",
            "Persistent signs of hypoglycemia (shakiness, sweating, confusion) or hyperglycemia.",
            "Non-healing ulcers or cuts on the feet.",
            "Sudden vision changes or persistent numbness."
        ],
        "emergency_warning_signs": [
            "Fruity breath odor, nausea, rapid breathing, and severe abdominal pain (Diabetic Ketoacidosis - DKA)",
            "Severe low blood sugar leading to confusion, seizures, or unresponsiveness",
            "Loss of consciousness"
        ],
        "reliable_references": [
            {"title": "WHO - Diabetes Key Facts", "url": "https://www.who.int/news-room/fact-sheets/detail/diabetes"},
            {"title": "American Diabetes Association (ADA)", "url": "https://diabetes.org"},
            {"title": "CDC - Basics About Diabetes", "url": "https://www.cdc.gov/diabetes/basics/index.html"}
        ]
    },
    {
        "id": "blood_pressure",
        "title": "Blood Pressure Awareness",
        "hindi_title": "रक्तचाप (ब्लड प्रेशर) जागरूकता",
        "category": "Cardiovascular",
        "summary": "Hypertension (high blood pressure) is often referred to as the 'silent killer' because it typically causes no noticeable symptoms until significant cardiovascular damage has already occurred.",
        "common_signs": [
            "Most people with high blood pressure have NO obvious symptoms.",
            "In very high or crisis levels: morning headaches, nosebleeds, irregular heart rhythms, and vision changes.",
            "Optimal blood pressure is generally under 120/80 mmHg."
        ],
        "prevention_tips": [
            "Reduce dietary sodium intake (aim for less than 2,000 mg of sodium per day).",
            "Eat a DASH-style diet rich in vegetables, fruits, nuts, and low-fat dairy.",
            "Limit alcohol intake and avoid tobacco products entirely.",
            "Maintain healthy stress management techniques and physical activity."
        ],
        "when_to_seek_care": [
            "Blood pressure readings consistently measuring 130/80 mmHg or higher on multiple occasions.",
            "Experiencing side effects from prescribed antihypertensive medications.",
            "Frequent dizziness, lightheadedness, or palpitations."
        ],
        "emergency_warning_signs": [
            "Hypertensive Crisis: BP reading greater than 180/120 mmHg",
            "Severe chest pain or shortness of breath",
            "Back pain, numbness/weakness, change in vision, or difficulty speaking"
        ],
        "reliable_references": [
            {"title": "WHO - Hypertension Factsheet", "url": "https://www.who.int/news-room/fact-sheets/detail/hypertension"},
            {"title": "American Heart Association - Understanding Blood Pressure Readings", "url": "https://www.heart.org"}
        ]
    },
    {
        "id": "heart_health",
        "title": "Heart Health & Warning Signs",
        "hindi_title": "हृदय स्वास्थ्य और चेतावनी संकेत",
        "category": "Cardiovascular",
        "summary": "Cardiovascular diseases (CVDs) are the leading cause of death globally. Maintaining heart health requires regular screening, mindful nutrition, stress control, and prompt recognition of cardiac warning signs.",
        "common_signs": [
            "Chest discomfort, pressure, fullness, or squeezing sensation in the center of the chest",
            "Pain radiating to one or both arms, the back, neck, jaw, or stomach",
            "Shortness of breath with or without chest discomfort",
            "Cold sweat, nausea, vomiting, or sudden lightheadedness"
        ],
        "prevention_tips": [
            "Avoid all forms of smoking and secondhand smoke exposure.",
            "Eat foods low in saturated and trans fats, emphasizing omega-3 fatty acids and soluble fiber.",
            "Maintain moderate physical activity: 30 minutes a day, 5 days a week.",
            "Routinely monitor cholesterol, blood sugar, and blood pressure levels."
        ],
        "when_to_seek_care": [
            "Unexplained shortness of breath during routine daily activities.",
            "Episodes of rapid, fluttering, or pounding heartbeats (palpitations).",
            "Swelling in your ankles, feet, or abdomen (edema)."
        ],
        "emergency_warning_signs": [
            "Crushing chest pressure or squeezing pain lasting more than a few minutes (SUSPECTED HEART ATTACK)",
            "Chest pain radiating to the left shoulder, neck, or jaw",
            "Sudden collapse or unresponsiveness - CALL EMERGENCY SERVICES IMMEDIATELY"
        ],
        "reliable_references": [
            {"title": "American Heart Association - Warning Signs of a Heart Attack", "url": "https://www.heart.org/en/health-topics/heart-attack/warning-signs-of-a-heart-attack"},
            {"title": "WHO - Cardiovascular Diseases", "url": "https://www.who.int/health-topics/cardiovascular-diseases"}
        ]
    },
    {
        "id": "nutrition_hydration",
        "title": "Balanced Nutrition & Hydration",
        "hindi_title": "संतुलित पोषण और जलयोजन",
        "category": "Wellness & Lifestyle",
        "summary": "Proper nutrition and adequate hydration are fundamental building blocks of immune defense, cognitive clarity, digestive health, and longevity.",
        "common_signs": [
            "Signs of good nutritional status: sustained daily energy, clear skin, healthy hair, regular bowel habits",
            "Deficiency signs: chronic fatigue, brittle nails, mouth sores, poor wound healing, brain fog"
        ],
        "prevention_tips": [
            "Fill half your plate with colorful vegetables and whole fruits at main meals.",
            "Choose whole grains (brown rice, oats, whole wheat) over refined flours.",
            "Incorporate plant-based proteins (lentils, chickpeas, tofu) and lean poultry/fish.",
            "Drink clean water regularly before feeling intense thirst."
        ],
        "when_to_seek_care": [
            "Unintended, significant weight loss or weight gain over a short period.",
            "Chronic digestive issues such as persistent bloating, abdominal pain, or changes in bowel habits.",
            "Suspected nutrient deficiencies (e.g., severe fatigue indicating possible iron or B12 deficiency)."
        ],
        "emergency_warning_signs": [
            "Severe inability to swallow liquids or solids (dysphagia)",
            "Signs of severe acute allergic reaction to food (facial swelling, wheezing, hives)"
        ],
        "reliable_references": [
            {"title": "WHO - Healthy Diet Guidelines", "url": "https://www.who.int/news-room/fact-sheets/detail/healthy-diet"},
            {"title": "Harvard T.H. Chan - The Healthy Eating Plate", "url": "https://www.hsph.harvard.edu/nutritionsource/healthy-eating-plate/"}
        ]
    },
    {
        "id": "sleep_activity",
        "title": "Restorative Sleep & Physical Activity",
        "hindi_title": "पुनर्योजी नींद और शारीरिक गतिविधि",
        "category": "Wellness & Lifestyle",
        "summary": "Sleep and physical activity operate in a mutually reinforcing cycle: regular daytime movement enhances deep restorative sleep, while restorative sleep repairs muscle tissue and balances metabolic hormones.",
        "common_signs": [
            "Adequate rest: waking refreshed without needing excessive stimulants, consistent focus throughout the day.",
            "Chronic sleep deprivation: daytime grogginess, irritability, weakened immune resilience, food cravings."
        ],
        "prevention_tips": [
            "Aim for 7 to 9 hours of uninterrupted sleep each night for adults.",
            "Establish a consistent wind-down routine and avoid screen exposure 60 minutes before bedtime.",
            "Keep the bedroom cool, dark, and quiet.",
            "Break prolonged sitting every 45-60 minutes with short standing or walking intervals."
        ],
        "when_to_seek_care": [
            "Chronic insomnia lasting more than a month despite sleep hygiene improvements.",
            "Loud, chronic snoring accompanied by daytime fatigue and choking/gasping sounds (possible Sleep Apnea).",
            "Severe, unexplained daytime sleep attacks (narcolepsy signs)."
        ],
        "emergency_warning_signs": [
            "Falling asleep involuntarily while driving or operating machinery",
            "Chest pain or extreme shortness of breath during light physical exertion"
        ],
        "reliable_references": [
            {"title": "CDC - Sleep and Sleep Disorders", "url": "https://www.cdc.gov/sleep/index.html"},
            {"title": "National Sleep Foundation", "url": "https://www.thensf.org"},
            {"title": "WHO - Physical Activity Guidelines", "url": "https://www.who.int/news-room/fact-sheets/detail/physical-activity"}
        ]
    },
    {
        "id": "first_aid_cpr",
        "title": "First Aid & CPR Essentials",
        "hindi_title": "प्राथमिक चिकित्सा और सीपीआर अनिवार्यता",
        "category": "Emergency & Safety",
        "summary": "Immediate high-quality CPR and basic first-aid can double or triple a person's chance of survival following sudden cardiac arrest, severe trauma, or choking emergencies.",
        "common_signs": [
            "Cardiac Arrest: Victim collapses suddenly, is unresponsive, and has absent or abnormal/agonal gasping breathing.",
            "Choking: Inability to speak, cough, or breathe; clutching hands to throat (universal choking sign)."
        ],
        "prevention_tips": [
            "Learn and practice Hands-Only CPR and basic AED operation.",
            "Keep a well-stocked first aid kit in your home, vehicle, and workplace.",
            "Chew food thoroughly and keep small choke-hazard objects away from toddlers.",
            "Know your local emergency ambulance numbers (e.g., 112 in India / Europe, 911 in North America)."
        ],
        "when_to_seek_care": [
            "Deep wounds requiring stitches, punctures from rusty objects (tetanus risk), or animal bites.",
            "Second or third-degree burns larger than 3 inches across or involving joints, hands, or face.",
            "Suspected bone fractures or severe sprains with inability to bear weight."
        ],
        "emergency_warning_signs": [
            "CARDIAC ARREST: Immediately call local emergency services and start Hands-Only chest compressions at 100-120 beats per minute.",
            "SEVERE ARTERIAL BLEEDING: Apply direct firm pressure with sterile gauze/cloth and do not release until paramedics arrive.",
            "COMPLETE AIRWAY OBSTRUCTION: Perform abdominal thrusts (Heimlich maneuver) immediately."
        ],
        "reliable_references": [
            {"title": "American Heart Association - CPR Guidelines", "url": "https://cpr.heart.org"},
            {"title": "Red Cross - First Aid & CPR Guidelines", "url": "https://www.redcross.org/take-a-class/first-aid"},
            {"title": "NHS - First Aid Overview", "url": "https://www.nhs.uk/conditions/first-aid/"}
        ]
    }
]

def get_all_education_topics(query: Optional[str] = None, category: Optional[str] = None) -> List[Dict[str, Any]]:
    results = EDUCATION_TOPICS
    if category and category != "All":
        results = [t for t in results if t["category"].lower() == category.lower()]
    if query:
        q = query.lower().strip()
        results = [
            t for t in results
            if q in t["title"].lower() 
            or q in t["hindi_title"].lower() 
            or q in t["summary"].lower() 
            or any(q in s.lower() for s in t["common_signs"])
            or any(q in p.lower() for p in t["prevention_tips"])
        ]
    return results

def get_education_topic_by_id(topic_id: str) -> Optional[Dict[str, Any]]:
    for t in EDUCATION_TOPICS:
        if t["id"] == topic_id:
            return t
    return None


import re
from typing import List, Dict, Any, Tuple

# Red-flag emergency indicators
EMERGENCY_KEYWORDS = [
    r"chest pain", r"crushing chest", r"chest pressure", r"heart attack",
    r"radiating to (arm|jaw|neck|back)", r"can't breathe", r"cannot breathe",
    r"severe shortness of breath", r"gasping for air", r"blue lips",
    r"slurred speech", r"facial droop", r"drooping face", r"sudden weakness on one side",
    r"sudden paralysis", r"stroke", r"worst headache of my life", r"thunderclap headache",
    r"coughing (up )?blood", r"vomiting blood", r"black tarry stools",
    r"unconscious", r"passed out", r"loss of consciousness", r"seizure", r"convulsion",
    r"throat closing", r"swelling of tongue", r"anaphylaxis",
    r"suicide", r"kill myself", r"self harm",
    # Hindi phrases
    r"सीने में दर्द", r"सांस नहीं आ रही", r"बेहोश", r"खून की उल्टी", r"दौरा", r"मुंह टेढ़ा"
]

SYMPTOM_KNOWLEDGE_BASE = [
    {
        "keywords": ["fever", "temperature", "chills", "sweats", "बुखार", "तापमान"],
        "possible_educational_causes": [
            {"condition": "Viral Upper Respiratory Infection", "likelihood": "Common", "details": "Body's immune response combating standard viruses like influenza or rhinoviruses."},
            {"condition": "Bacterial Infection", "likelihood": "Moderate", "details": "Potential localized bacterial issue such as strep pharyngitis, urinary tract infection, or tonsillitis."},
            {"condition": "Heat Exhaustion", "likelihood": "Context dependent", "details": "Elevated core body temperature after prolonged sun exposure or vigorous physical exertion."}
        ],
        "follow_ups": [
            "How high has the temperature been, and how many days has it lasted?",
            "Are there accompanying symptoms like sore throat, cough, urinary burning, or skin rash?",
            "Can you comfortably bend your neck forward without sharp pain or stiffness?"
        ],
        "self_care": [
            "Rest adequately to assist your immune defense.",
            "Stay well-hydrated with water, electrolyte drinks, clear broths, or herbal teas.",
            "Wear lightweight, breathable clothing and avoid overheating with heavy blankets."
        ],
        "seek_care": [
            "Temperature remains above 102°F (38.9°C) for more than 48-72 hours despite fluids and rest.",
            "Difficulty staying hydrated or inability to keep liquids down.",
            "Severe sore throat, ear pain, or productive cough."
        ]
    },
    {
        "keywords": ["headache", "head pain", "migraine", "temple", "सिरदर्द"],
        "possible_educational_causes": [
            {"condition": "Tension-Type Headache", "likelihood": "Very Common", "details": "Muscle contractions in neck/scalp triggered by screen fatigue, poor ergonomics, or psychological stress."},
            {"condition": "Dehydration Headache", "likelihood": "Common", "details": "Temporary brain tissue fluid contraction resulting from insufficient fluid intake or excess caffeine/alcohol."},
            {"condition": "Migraine Episode", "likelihood": "Common", "details": "Neurovascular changes causing pulsing one-sided discomfort, sensitivity to light/sound, and nausea."}
        ],
        "follow_ups": [
            "Is the pain throbbing, sharp, or does it feel like a constant tight pressure band?",
            "Did the pain develop gradually, or did it reach peak intensity within seconds?",
            "Do you notice sensitivity to bright screens, loud sounds, or nausea?"
        ],
        "self_care": [
            "Drink a tall glass of cool water or electrolyte solution.",
            "Rest in a quiet, dimly lit, well-ventilated room with eyes closed.",
            "Apply a cool damp cloth or warm compress to forehead and back of neck."
        ],
        "seek_care": [
            "Headaches becoming more frequent or severe over multiple weeks.",
            "Headaches accompanied by stiff neck, confusion, or recent head trauma."
        ]
    },
    {
        "keywords": ["cough", "throat", "congestion", "runny nose", "cold", "खांसी", "गला खराब"],
        "possible_educational_causes": [
            {"condition": "Acute Viral Rhinosinusitis / Common Cold", "likelihood": "Very Common", "details": "Self-limiting viral invasion of mucosal lining of upper airways."},
            {"condition": "Allergic Rhinitis / Post-Nasal Drip", "likelihood": "Common", "details": "Environmental histamine reaction triggering continuous nasal drainage down the back of the throat."},
            {"condition": "Acid Reflux (LPR / GERD)", "likelihood": "Moderate", "details": "Micro-aspiration of stomach acid causing persistent dry throat tickle, worse when lying down."}
        ],
        "follow_ups": [
            "Is the cough dry and tickly, or are you coughing up colored phlegm?",
            "How long have you had this cough (less than 3 weeks or longer)?",
            "Are you experiencing any shortness of breath, wheezing, or chest tightness?"
        ],
        "self_care": [
            "Sip warm fluids such as ginger-honey tea or warm water with lemon.",
            "Inhale steam from a bowl of hot water or use a cool-mist room humidifier.",
            "Gargle with warm salt water (1/2 tsp salt in 1 glass warm water) for sore throat."
        ],
        "seek_care": [
            "Cough persisting beyond 3 weeks without improvement.",
            "Fever above 101°F that persists or recurs.",
            "Wheezing, shortness of breath, or noticeable chest soreness."
        ]
    },
    {
        "keywords": ["stomach", "abdominal", "nausea", "vomiting", "diarrhea", "पेट दर्द", "उल्टी", "दस्त"],
        "possible_educational_causes": [
            {"condition": "Viral Gastroenteritis (Stomach Flu)", "likelihood": "Common", "details": "Intestinal viral inflammation causing cramps, watery diarrhea, and mild nausea."},
            {"condition": "Dietary Indiscretion / Food Sensitivity", "likelihood": "Common", "details": "Reactions to high-fat, spicy foods, lactose, or mild foodborne bacteria."},
            {"condition": "Gastritis / Acid Dyspepsia", "likelihood": "Moderate", "details": "Irritation of gastric mucosa by excess stomach acid, stress, or NSAID pain relievers."}
        ],
        "follow_ups": [
            "Where precisely is the discomfort located (upper stomach, around navel, lower right quadrant)?",
            "Are you able to keep sips of oral fluids down without vomiting?",
            "Have you noticed any blood in bowel movements or vomit?"
        ],
        "self_care": [
            "Sip small amounts of Oral Rehydration Solution (ORS) or electrolyte water frequently.",
            "Follow the BRAT diet (Bananas, Rice, Applesauce, Toast) once vomiting subsides.",
            "Avoid dairy, greasy foods, caffeine, and spicy seasonings for several days."
        ],
        "seek_care": [
            "Inability to keep liquids down for over 24 hours.",
            "Severe sharp localized pain, especially in the lower right side of the abdomen.",
            "Signs of dehydration: dark urine, lightheadedness upon standing, extreme dry mouth."
        ]
    }
]

def check_emergency_symptoms(text: str) -> Tuple[bool, str]:
    text_lower = text.lower()
    for pattern in EMERGENCY_KEYWORDS:
        if re.search(pattern, text_lower):
            return True, (
                "CRITICAL SAFETY ALERT: The symptoms you described may indicate a medical emergency "
                "(such as potential cardiac event, respiratory distress, acute stroke, or severe trauma). "
                "Do NOT rely on an AI or web assistant in an emergency. Please immediately call your "
                "local emergency medical services (such as 112 in India/Europe or 911 in the US/Canada) "
                "or proceed immediately to the nearest hospital emergency department."
            )
    return False, ""

def analyze_symptoms_educational(
    symptoms: str,
    duration: str = "Not specified",
    severity: str = "Moderate",
    fever_present: bool = False,
    age_group: str = "Adult",
    language: str = "en"
) -> Dict[str, Any]:
    is_emergency, emergency_msg = check_emergency_symptoms(symptoms)
    
    # Match against knowledge base
    matched_causes = []
    follow_ups = []
    self_care = []
    seek_care = []
    
    text_lower = symptoms.lower()
    for topic in SYMPTOM_KNOWLEDGE_BASE:
        if any(k.lower() in text_lower for k in topic["keywords"]):
            matched_causes.extend(topic["possible_educational_causes"])
            follow_ups.extend(topic["follow_ups"][:2])
            self_care.extend(topic["self_care"][:2])
            seek_care.extend(topic["seek_care"][:2])
            
    if not matched_causes:
        # Generic educational fallback
        matched_causes = [
            {"condition": "General Non-Specific Symptom Presentation", "likelihood": "Requires medical review", "details": "The entered symptoms can stem from diverse benign or systemic origins requiring clinical evaluation."},
            {"condition": "Stress or Lifestyle-Related Physiological Response", "likelihood": "Possible", "details": "Fatigue, mild dehydration, muscular strain, or stress often manifest physically."}
        ]
        follow_ups = [
            "How long have you noticed these sensations, and are they continuous or intermittent?",
            "What activities, foods, or positions seem to make the symptom better or worse?",
            "Have you started any new medications, supplements, or experienced major routine changes?"
        ]
        self_care = [
            "Ensure adequate hydration and consistent, balanced sleep.",
            "Monitor whether the symptoms escalate in intensity over the next 24 to 48 hours.",
            "Keep a brief log of when the symptoms occur and what you were doing at the time."
        ]
        seek_care = [
            "Symptoms worsen in intensity or interfere with daily basic tasks.",
            "New symptoms emerge, such as persistent fever, unexplained dizziness, or localized severe pain."
        ]

    # De-duplicate
    follow_ups = list(dict.fromkeys(follow_ups))
    self_care = list(dict.fromkeys(self_care))
    seek_care = list(dict.fromkeys(seek_care))
    
    summary = (
        f"Educational analysis for reported symptoms: '{symptoms[:120]}...' (Reported severity: {severity}, Duration: {duration}). "
        "This tool provides general health education and cannot diagnose medical conditions or substitute for professional medical assessment."
    )
    
    strict_disclaimer = (
        "IMPORTANT MEDICAL DISCLAIMER: This symptom checker is strictly an educational tool. "
        "It does NOT provide a medical diagnosis, clinical prognosis, or personalized treatment plan. "
        "Symptoms can be complex and caused by numerous factors. Always consult a licensed healthcare "
        "provider or doctor for proper diagnostic examination and medical advice."
    )
    
    return {
        "summary": summary,
        "is_emergency": is_emergency,
        "emergency_guidance": emergency_msg if is_emergency else None,
        "possible_educational_causes": matched_causes[:4],
        "follow_up_questions": follow_ups[:4],
        "general_self_care_tips": self_care[:4],
        "when_to_see_doctor": seek_care[:4],
        "strict_disclaimer": strict_disclaimer,
        "is_demo": True
    }


from fastapi import APIRouter
from typing import List, Dict, Any

router = APIRouter(prefix="/api/emergency", tags=["Emergency Help"])

EMERGENCY_GUIDES: List[Dict[str, Any]] = [
    {
        "id": "cpr",
        "title": "Hands-Only Adult CPR",
        "subtitle": "For an unresponsive adult with absent or abnormal breathing",
        "category": "Cardiac Emergency",
        "urgent_action": "CALL EMERGENCY SERVICES (112 / 911) IMMEDIATELY AND RETRIEVE AN AED IF AVAILABLE.",
        "steps": [
            "CHECK FOR RESPONSIVENESS: Tap shoulders firmly and shout 'Are you okay?'. Check if breathing is normal (gasping is NOT normal breathing).",
            "CALL FOR HELP: Shout for nearby bystanders to dial local emergency services (112 / 911) and locate an Automated External Defibrillator (AED).",
            "POSITION HANDS: Place the heel of one hand in the center of the chest (between nipples). Place your other hand on top and interlock fingers.",
            "PUSH HARD AND FAST: Lock your elbows straight and press down at least 2 inches (5 cm) deep. Maintain a tempo of 100 to 120 beats per minute (e.g., to the rhythm of 'Stayin' Alive').",
            "ALLOW FULL CHEST RECOIL: Let the chest return completely to its normal position between each compression.",
            "DO NOT INTERRUPT: Continue continuous chest compressions until professional paramedics arrive, an AED prompts you to stop, or the person clearly wakes up."
        ],
        "do_not_do": [
            "DO NOT delay compressions to check for a faint pulse if you are an untrained rescuer.",
            "DO NOT stop compressions for more than 10 seconds.",
            "DO NOT give mouth-to-mouth rescue breaths if untrained or uncomfortable — Hands-Only CPR is highly effective!"
        ],
        "reference": "American Heart Association (AHA) CPR & ECC Guidelines & International Liaison Committee on Resuscitation (ILCOR)"
    },
    {
        "id": "choking",
        "title": "Choking & Airway Obstruction (Heimlich Maneuver)",
        "subtitle": "For conscious adults or children over 1 year who cannot speak or cough",
        "category": "Airway Emergency",
        "urgent_action": "Ask 'Are you choking?'. If they nod and cannot speak, act immediately.",
        "steps": [
            "STAND BEHIND: Stand directly behind the person and place one foot slightly forward for balance.",
            "MAKE A FIST: Wrap your arms around their waist. Make a fist with one hand and place the thumb side just above their navel (well below the ribcage).",
            "GRASP AND THRUST: Grasp your fist with your other hand. Perform rapid, inward and upward thrusts into their abdomen.",
            "REPEAT: Continue inward and upward thrusts until the lodged object is forcibly expelled or the victim becomes unresponsive.",
            "IF UNRESPONSIVE: Gently lower them to the floor, call 112/911, and begin chest compressions immediately."
        ],
        "do_not_do": [
            "DO NOT perform abdominal thrusts on infants under 1 year (use alternating 5 back blows and 5 chest thrusts instead).",
            "DO NOT perform blind finger sweeps in the mouth, which can push foreign objects deeper into the larynx."
        ],
        "reference": "American Red Cross First Aid Advisory Board"
    },
    {
        "id": "severe_bleeding",
        "title": "Severe External Bleeding",
        "subtitle": "Rapid blood loss from deep lacerations or trauma",
        "category": "Trauma",
        "urgent_action": "APPLY IMMEDIATE DIRECT PRESSURE AND CALL FOR EMERGENCY MEDICAL HELP.",
        "steps": [
            "DIRECT PRESSURE: Place sterile gauze or a clean cloth directly over the wound. Press down firmly with both hands.",
            "MAINTAIN CONTINUOUS PRESSURE: Do NOT lift the cloth to check if bleeding has stopped. If blood soaks through, add another layer on top and keep pressing.",
            "ELEVATION (IF NO FRACTURE): Elevate the injured limb above heart level while maintaining firm direct pressure.",
            "PRESSURE BANDAGE: Secure gauze tightly with a bandage or cloth strip without cutting off circulation completely."
        ],
        "do_not_do": [
            "DO NOT remove deeply embedded objects (such as knives or metal shards) — stabilize them in place with rolled dressings.",
            "DO NOT release pressure until medical professionals take over."
        ],
        "reference": "WHO Basic Emergency Care & Red Cross First Aid"
    },
    {
        "id": "burns",
        "title": "Thermal Burns First Aid",
        "subtitle": "Immediate management of heat or scald burns",
        "category": "Trauma & Skin",
        "urgent_action": "REMOVE HEAT SOURCE AND COOL THE BURN IMMEDIATELY.",
        "steps": [
            "COOL RUNNING WATER: Immediately hold the burned area under cool (not cold or freezing) gently running tap water for 10 to 20 minutes.",
            "REMOVE RESTRICTIONS: Gently remove rings, watches, or tight clothing around the burned area before swelling develops.",
            "COVER LOOSELY: Cover the burn loosely with sterile non-stick dressing or clean plastic food wrap.",
            "PAIN RELIEF: Over-the-counter pain relievers can be considered once medical attention is arranged if needed."
        ],
        "do_not_do": [
            "DO NOT apply ice, ice water, butter, toothpaste, oil, or home remedies — these cause tissue necrosis and infection.",
            "DO NOT pop or puncture intact blisters.",
            "DO NOT pull away clothing that is melted or stuck to burned flesh."
        ],
        "reference": "British Burn Association & NHS First Aid"
    },
    {
        "id": "seizures",
        "title": "Seizure Response & Safety",
        "subtitle": "Protecting a person during an active convulsive seizure",
        "category": "Neurological",
        "urgent_action": "KEEP THE PERSON SAFE FROM HARD OBJECTS AND TIME THE SEIZURE.",
        "steps": [
            "PROTECT HEAD: Cushion their head with a folded jacket, pillow, or soft cloth.",
            "CLEAR THE AREA: Move hard, sharp, or hot objects away from the person.",
            "TIME IT: Note the start time. If the seizure lasts longer than 5 minutes, call emergency services immediately.",
            "RECOVERY POSITION: Once convulsions stop, gently roll the person onto their side (recovery position) to keep airway open and clear fluids."
        ],
        "do_not_do": [
            "DO NOT hold the person down or attempt to restrain their movements.",
            "DO NOT put anything in their mouth (they cannot swallow their tongue!).",
            "DO NOT give food, water, or pills until they are fully awake and alert."
        ],
        "reference": "CDC Epilepsy Program & Epilepsy Foundation"
    }
]

EMERGENCY_NUMBERS: List[Dict[str, str]] = [
    {"region": "India", "service": "National Emergency All-in-One", "number": "112"},
    {"region": "India", "service": "Medical Ambulance", "number": "108 / 102"},
    {"region": "United States & Canada", "service": "Emergency Services", "number": "911"},
    {"region": "United Kingdom", "service": "Emergency Services", "number": "999 (111 non-emergency)"},
    {"region": "European Union", "service": "Pan-European Emergency", "number": "112"},
    {"region": "Australia", "service": "Emergency Services", "number": "000"},
    {"region": "Global Crisis Helpline", "service": "International Suicide Prevention", "number": "findahelpline.com"}
]

@router.get("/guides")
def get_emergency_guides():
    return {
        "warning": (
            "CRITICAL WARNING: If you or someone with you is experiencing severe trauma, difficulty breathing, "
            "unconsciousness, or chest pain, DO NOT WAIT or delay treatment while reading this app. "
            "Call local emergency services immediately!"
        ),
        "guides": EMERGENCY_GUIDES
    }

@router.get("/contacts")
def get_emergency_contacts():
    return {
        "note": "Verify these numbers for your exact municipality or location. In an emergency, dial your local emergency access number.",
        "contacts": EMERGENCY_NUMBERS
    }


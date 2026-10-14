import logging
import httpx
from typing import List, Dict, Any, Optional
from backend.app.config import settings
from backend.app.services.symptom_service import check_emergency_symptoms

logger = logging.getLogger("healthcare_ai")

SYSTEM_PROMPT = """You are HealthCare AI, a knowledgeable, empathetic, and strictly educational health assistant.
Your goal is to help users understand general health topics, learn about common symptoms, maintain healthy habits, and access basic health education.

CRITICAL MEDICAL SAFETY RULES:
1. You are NOT a qualified medical doctor. You NEVER provide a definitive medical diagnosis or replace a doctor's examination.
2. You NEVER prescribe prescription drugs, suggest unverified combinations, or recommend altering a prescribed treatment plan.
3. If the user mentions emergency signs (e.g., chest pain, shortness of breath, sudden numbness, stroke symptoms, coughing blood, severe trauma, suicidal thoughts), immediately advise contacting local emergency services (112 / 911 / emergency room) and do NOT delay them.
4. Structure your response clearly using readable paragraphs and bullet points.
5. If the user asks in Hindi or requests Hindi, reply naturally in clear, supportive Hindi (Devanagari script). Otherwise, reply in English.
6. Always include a brief educational disclaimer at the end of every response.
"""

# Realistic responses for Demo Mode when no API key is provided
DEMO_RESPONSES = {
    "fever": {
        "en": (
            "### Understanding Fever\n\n"
            "A fever (typically a body temperature above 100.4°F or 38°C) is an indicator that your body's immune system is active and fighting an infection.\n\n"
            "**Helpful General Self-Care Measures:**\n"
            "- **Fluid Intake:** Drink plenty of water, electrolyte drinks, or warm broths to prevent dehydration.\n"
            "- **Rest:** Give your body ample downtime to recover.\n"
            "- **Comfort:** Wear light, breathable clothing and avoid overly thick blankets.\n\n"
            "**When to Seek Immediate Medical Evaluation:**\n"
            "- A fever lasting longer than 3 consecutive days or exceeding 103°F (39.4°C).\n"
            "- Accompanying signs like stiff neck, confusion, difficulty breathing, or severe abdominal pain.\n\n"
            "*Disclaimer: This response is generated in Offline Demo Mode for educational purposes and is not a medical diagnosis.*"
        ),
        "hi": (
            "### बुखार (Fever) के बारे में जानकारी\n\n"
            "बुखार (शरीर का तापमान 100.4°F या 38°C से अधिक होना) यह दर्शाता है कि आपकी प्रतिरक्षा प्रणाली (immune system) किसी संक्रमण से लड़ रही है।\n\n"
            "**सामान्य प्राथमिक देखभाल सुझाव:**\n"
            "- **जलयोजन (Hydration):** खूब सारा पानी, ओआरएस या हल्का सूप पिएं ताकि शरीर में पानी की कमी न हो।\n"
            "- **विश्राम:** शरीर को ठीक होने के लिए पर्याप्त आराम दें।\n"
            "- **हल्के कपड़े:** सूती और आरामदायक कपड़े पहनें।\n\n"
            "**डॉक्टर से कब संपर्क करें:**\n"
            "- यदि बुखार 3 दिन से अधिक रहे या 103°F से अधिक हो जाए।\n"
            "- यदि सांस लेने में कठिनाई, गर्दन में अकड़न या अत्यधिक कमजोरी हो।\n\n"
            "*अस्वीकरण: यह उत्तर ऑफलाइन डेमो मोड में शैक्षिक जानकारी के लिए उत्पन्न किया गया है। यह चिकित्सीय निदान नहीं है।* "
        ),
        "follow_ups": [
            "How high is your recorded temperature?",
            "How many days has the fever been present?",
            "Are there symptoms like cough, sore throat, or chills?"
        ]
    },
    "water": {
        "en": (
            "### Daily Hydration Guidelines\n\n"
            "Adequate water intake is essential for maintaining blood volume, regulating body temperature, lubricating joints, and flushing metabolic waste.\n\n"
            "**Recommended Daily Intake:**\n"
            "- For most healthy adults, **2 to 3 liters (about 8-12 cups)** of fluids per day is recommended.\n"
            "- Increase intake during hot weather or strenuous physical activity.\n\n"
            "**Tips to Maintain Hydration:**\n"
            "- Keep a reusable water bottle near your workspace.\n"
            "- Check urine color: a pale, straw-like yellow indicates healthy hydration.\n"
            "- Consume hydrating foods like cucumbers, melons, and oranges.\n\n"
            "*Disclaimer: Demo Mode. Individual fluid needs may vary based on kidney or cardiac conditions.*"
        ),
        "hi": (
            "### दैनिक जलयोजन (Hydration) की आवश्यकता\n\n"
            "पर्याप्त पानी पीना रक्त परिसंचरण, शरीर के तापमान नियंत्रण और पाचन स्वास्थ्य के लिए अत्यंत आवश्यक है।\n\n"
            "**सामान्य दिशा-निर्देश:**\n"
            "- एक स्वस्थ वयस्क को प्रतिदिन लगभग **2 से 3 लीटर (8 से 12 गिलास)** तरल पदार्थ पीने चाहिए।\n"
            "- गर्मी के मौसम और व्यायाम के समय पानी की मात्रा बढ़ाएं।\n\n"
            "**सुझाव:**\n"
            "- हमेशा अपने पास पानी की बोतल रखें।\n"
            "- हल्के पीले रंग का मूत्र पर्याप्त जलयोजन का संकेत है।\n\n"
            "*अस्वीकरण: डेमो मोड। यह चिकित्सीय सलाह का विकल्प नहीं है।*"
        ),
        "follow_ups": [
            "What is your target daily water intake?",
            "Are you experiencing signs of dehydration like dry mouth or dizziness?"
        ]
    },
    "sleep": {
        "en": (
            "### The Importance of Restorative Sleep\n\n"
            "Quality sleep is vital for cellular repair, immune functionality, hormone regulation, and cognitive memory consolidation.\n\n"
            "**Recommended Sleep Duration:**\n"
            "- **Adults (18-64 yrs):** 7 to 9 hours nightly.\n"
            "- **Older Adults (65+ yrs):** 7 to 8 hours nightly.\n\n"
            "**Healthy Sleep Hygiene Tips:**\n"
            "- Maintain consistent sleep and wake times, including on weekends.\n"
            "- Eliminate screen exposure (smartphones, TVs) at least 45 minutes before sleep.\n"
            "- Keep your sleeping environment dark, quiet, and slightly cool.\n\n"
            "*Disclaimer: Generated in Demo Mode for educational awareness.*"
        ),
        "hi": (
            "### अच्छी नींद का महत्व\n\n"
            "गुणवत्तापूर्ण नींद शरीर की कोशिकाओं की मरम्मत, रोग प्रतिरोधक क्षमता और मानसिक स्वास्थ्य के लिए जरूरी है।\n\n"
            "**सुझाई गई नींद की अवधि:**\n"
            "- वयस्कों के लिए प्रति रात **7 से 9 घंटे** की निर्बाध नींद आवश्यक है।\n\n"
            "**स्वस्थ नींद के उपाय:**\n"
            "- सोने और जागने का एक निश्चित समय निर्धारित करें।\n"
            "- सोने से 45 मिनट पहले मोबाइल और स्क्रीन से दूरी बनाएं।\n"
            "- शयनकक्ष को शांत, अंधेरा और ठंडा रखें।\n\n"
            "*अस्वीकरण: डेमो मोड। शैक्षिक उद्देश्य के लिए।* "
        ),
        "follow_ups": [
            "How many hours do you usually sleep per night?",
            "Do you wake up feeling refreshed or fatigued?"
        ]
    },
    "generic": {
        "en": (
            "### Health Education Summary\n\n"
            "Thank you for your question. Maintaining proactive wellness habits and understanding how your body functions are key components of preventive health.\n\n"
            "**Core Pillars of Daily Wellness:**\n"
            "- **Balanced Nutrition:** Prioritize unprocessed whole grains, vegetables, and lean proteins.\n"
            "- **Physical Activity:** Aim for at least 150 minutes of moderate aerobic activity weekly.\n"
            "- **Hydration & Sleep:** 2-3 liters of clean water and 7-9 hours of consistent sleep nightly.\n"
            "- **Routine Check-ups:** Regular health screenings with your doctor help detect concerns early.\n\n"
            "*Disclaimer: This reply is generated by HealthCare AI in **Demo Mode (Offline Mock Simulation)** because no external AI API key is configured. It is for educational purposes and is not a medical diagnosis.*"
        ),
        "hi": (
            "### स्वास्थ्य शिक्षा सारांश\n\n"
            "आपके प्रश्न के लिए धन्यवाद। दैनिक जीवन में स्वस्थ आदतों का पालन करना और अपने शरीर के संकेतों को समझना स्वास्थ्य सुरक्षा का पहला कदम है।\n\n"
            "**दैनिक स्वास्थ्य के मुख्य स्तंभ:**\n"
            "- **संतुलित आहार:** ताजी सब्जियां, फल और साबुत अनाज को प्राथमिकता दें।\n"
            "- **नियमित व्यायाम:** सप्ताह में कम से कम 150 मिनट मध्यम व्यायाम करें।\n"
            "- **जलयोजन और नींद:** रोजाना 2-3 लीटर पानी और 7-9 घंटे की नींद लें।\n"
            "- **नियमित स्वास्थ्य जांच:** समय-समय पर डॉक्टर से सामान्य जांच कराएं।\n\n"
            "*अस्वीकरण: यह उत्तर **डेमो मोड (ऑफलाइन मॉक सिमुलेशन)** में तैयार किया गया है क्योंकि कोई बाहरी AI API Key कॉन्फ़िगर नहीं है। यह चिकित्सीय सलाह नहीं है।*"
        ),
        "follow_ups": [
            "Would you like information on hydration, sleep, or nutrition?",
            "Do you have a specific symptom you would like educational guidance about?"
        ]
    }
}

async def generate_gemini_response(prompt: str, language: str, history: List[Dict[str, str]]) -> str:
    """Direct API call to Google Gemini endpoint via httpx using GEMINI_API_KEY"""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{settings.AI_MODEL}:generateContent?key={settings.GEMINI_API_KEY}"
    
    # Format messages
    contents = []
    # System instruction
    contents.append({
        "role": "user",
        "parts": [{"text": f"System Directive: {SYSTEM_PROMPT}\nTarget Output Language: {'Hindi' if language == 'hi' else 'English'}"}]
    })
    contents.append({
        "role": "model",
        "parts": [{"text": "Understood. I will provide strictly educational, structured health information with clear disclaimers, never diagnosing or prescribing."}]
    })
    
    # Add recent history
    for item in history[-6:]:
        role = "user" if item.get("role") == "user" else "model"
        contents.append({
            "role": role,
            "parts": [{"text": item.get("content", "")}]
        })
        
    contents.append({
        "role": "user",
        "parts": [{"text": prompt}]
    })
    
    payload = {
        "contents": contents,
        "generationConfig": {
            "temperature": 0.4,
            "topP": 0.9,
            "maxOutputTokens": 1024
        }
    }
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        
        candidates = data.get("candidates", [])
        if candidates and "content" in candidates[0]:
            parts = candidates[0]["content"].get("parts", [])
            if parts:
                return parts[0].get("text", "")
        return "I apologize, but I could not formulate a clear educational response at this moment."

async def generate_openai_response(prompt: str, language: str, history: List[Dict[str, str]]) -> str:
    """Call OpenAI compatible endpoint using OPENAI_API_KEY"""
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {settings.OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    messages = [
        {"role": "system", "content": f"{SYSTEM_PROMPT}\nTarget Output Language: {'Hindi' if language == 'hi' else 'English'}"}
    ]
    for item in history[-6:]:
        messages.append({
            "role": item.get("role", "user"),
            "content": item.get("content", "")
        })
    messages.append({"role": "user", "content": prompt})
    
    payload = {
        "model": "gpt-4o-mini",
        "messages": messages,
        "temperature": 0.4,
        "max_tokens": 1000
    }
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]

def get_demo_response(query: str, language: str) -> Dict[str, Any]:
    q_lower = query.lower()
    selected = "generic"
    if "fever" in q_lower or "बुखार" in q_lower or "temp" in q_lower:
        selected = "fever"
    elif "water" in q_lower or "पानी" in q_lower or "hydrat" in q_lower or "drink" in q_lower:
        selected = "water"
    elif "sleep" in q_lower or "नींद" in q_lower or "tired" in q_lower or "rest" in q_lower:
        selected = "sleep"
        
    topic = DEMO_RESPONSES[selected]
    lang_key = "hi" if language == "hi" else "en"
    text = topic[lang_key]
    follow_ups = topic.get("follow_ups", [])
    
    return {
        "reply": text,
        "is_demo": True,
        "provider": "Demo Mode (Mock Simulation)",
        "follow_ups": follow_ups
    }

async def process_chat_query(
    message: str,
    language: str = "en",
    history: Optional[List[Dict[str, str]]] = None
) -> Dict[str, Any]:
    history = history or []
    is_emergency, emergency_msg = check_emergency_symptoms(message)
    
    # If API key configured, use real LLM
    if settings.has_ai_credentials:
        try:
            if settings.GEMINI_API_KEY:
                reply_text = await generate_gemini_response(message, language, history)
                provider = "Google Gemini"
            else:
                reply_text = await generate_openai_response(message, language, history)
                provider = "OpenAI"
                
            return {
                "reply": reply_text,
                "language": language,
                "is_demo": False,
                "provider": provider,
                "suggested_follow_ups": [
                    "Can you elaborate on self-care measures?",
                    "What warning signs should prompt an emergency visit?",
                    "What questions should I ask my doctor about this?"
                ],
                "emergency_warning": emergency_msg if is_emergency else None,
                "disclaimer": "Educational information only. Not a medical diagnosis or substitute for professional healthcare advice."
            }
        except Exception as e:
            logger.error(f"Error calling AI provider: {e}", exc_info=True)
            # Fall back gracefully to demo mode with notice
            demo_data = get_demo_response(message, language)
            fallback_notice = (
                f"\n\n> [!NOTE]\n> *Note: AI provider API call was unavailable ({str(e)[:60]}...). Displaying safe educational content in Demo Mode.*"
            )
            return {
                "reply": demo_data["reply"] + fallback_notice,
                "language": language,
                "is_demo": True,
                "provider": "Demo Mode (API Fallback)",
                "suggested_follow_ups": demo_data["follow_ups"],
                "emergency_warning": emergency_msg if is_emergency else None,
                "disclaimer": "Educational information only. Not a medical diagnosis or substitute for professional healthcare advice."
            }
    else:
        # Transparent Offline Demo Mode
        demo_data = get_demo_response(message, language)
        return {
            "reply": demo_data["reply"],
            "language": language,
            "is_demo": True,
            "provider": "Demo Mode (Mock Simulation - No API Key Set)",
            "suggested_follow_ups": demo_data["follow_ups"],
            "emergency_warning": emergency_msg if is_emergency else None,
            "disclaimer": "Educational information only. Not a medical diagnosis or substitute for professional healthcare advice."
        }


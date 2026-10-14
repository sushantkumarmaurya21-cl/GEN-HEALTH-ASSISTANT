from fastapi import APIRouter
from backend.app.config import settings

router = APIRouter(prefix="/api/system", tags=["System"])

@router.get("/status")
def get_system_status():
    return {
        "status": "healthy",
        "app_name": "HealthCare AI – Your Smart Health Assistant",
        "version": "1.0.0",
        "ai_configured": settings.has_ai_credentials,
        "active_provider": settings.active_provider,
        "model": settings.AI_MODEL if settings.has_ai_credentials else "Local Mock Engine",
        "supported_languages": ["en", "hi"],
        "disclaimer": (
            "HealthCare AI is an educational technology prototype. It is strictly not a medical device "
            "and does not provide medical diagnoses, treatment decisions, or personalized pharmaceutical advice."
        ),
        "setup_instructions": (
            "To enable live AI generation, set GEMINI_API_KEY or OPENAI_API_KEY in backend/.env "
            "and restart the backend server."
        )
    }


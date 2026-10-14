import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file from backend root or parent
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

class Settings:
    HOST: str = os.getenv("HOST", "127.0.0.1")
    PORT: int = int(os.getenv("PORT", "8000"))
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    CORS_ORIGINS: list[str] = [
        origin.strip() 
        for origin in os.getenv("CORS_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173").split(",")
        if origin.strip()
    ]
    
    # API Keys
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "").strip()
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "").strip()
    AI_MODEL: str = os.getenv("AI_MODEL", "gemini-1.5-flash")
    
    # Database
    DATABASE_PATH: Path = Path(__file__).resolve().parent.parent / "healthcare_ai.db"
    
    # Safety & Rate Limits
    RATE_LIMIT_PER_MINUTE: int = int(os.getenv("RATE_LIMIT_PER_MINUTE", "60"))
    
    @property
    def has_ai_credentials(self) -> bool:
        return bool(self.GEMINI_API_KEY or self.OPENAI_API_KEY)

    @property
    def active_provider(self) -> str:
        if self.GEMINI_API_KEY:
            return "Google Gemini"
        if self.OPENAI_API_KEY:
            return "OpenAI"
        return "Demo Mode (Mock Simulation)"

settings = Settings()


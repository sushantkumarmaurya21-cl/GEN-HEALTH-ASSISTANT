import uvicorn
import os
import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

if __name__ == "__main__":
    from backend.app.config import settings
    print(f"Starting HealthCare AI Backend on http://{settings.HOST}:{settings.PORT}")
    print(f"Active AI Provider: {settings.active_provider}")
    uvicorn.run("backend.app.main:app", host=settings.HOST, port=settings.PORT, reload=True)


import time
from collections import defaultdict
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from backend.app.config import settings
from backend.app.database import init_db
from backend.app.routers import chat, symptoms, education, medicines, wellness, emergency, system

# Simple in-memory sliding window rate limiter
# Limits requests per minute per client IP to protect the server and AI endpoints
request_history = defaultdict(list)

def check_rate_limit(client_ip: str, limit: int = 60, window_seconds: int = 60) -> bool:
    now = time.time()
    timestamps = request_history[client_ip]
    # Remove older timestamps outside the window
    request_history[client_ip] = [t for t in timestamps if now - t < window_seconds]
    if len(request_history[client_ip]) >= limit:
        return False
    request_history[client_ip].append(now)
    return True

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize database on startup
    init_db()
    yield
    # Cleanup if needed

app = FastAPI(
    title="HealthCare AI API",
    description="Your Smart Health Assistant – Safe, responsive educational health platform API",
    version="1.0.0",
    lifespan=lifespan
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For prototype ease of access across vite dev ports
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rate Limiter Middleware
@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    # Exempt swagger docs, health check and options requests
    if request.url.path in ["/docs", "/openapi.json", "/api/system/status", "/"] or request.method == "OPTIONS":
        return await call_next(request)
        
    client_ip = request.client.host if request.client else "127.0.0.1"
    if not check_rate_limit(client_ip, limit=settings.RATE_LIMIT_PER_MINUTE):
        return JSONResponse(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            content={
                "detail": "Rate limit exceeded. Please wait a moment before sending more requests.",
                "retry_after_seconds": 30
            }
        )
    return await call_next(request)

# Include Routers
app.include_router(chat.router)
app.include_router(symptoms.router)
app.include_router(education.router)
app.include_router(medicines.router)
app.include_router(wellness.router)
app.include_router(emergency.router)
app.include_router(system.router)

@app.get("/")
def root_endpoint():
    return {
        "message": "Welcome to HealthCare AI – Your Smart Health Assistant API",
        "documentation": "/docs",
        "system_status": "/api/system/status",
        "disclaimer": "This service is strictly for general health education and wellness awareness. It is NOT a medical diagnosis tool."
    }


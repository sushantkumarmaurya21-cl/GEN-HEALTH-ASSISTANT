from fastapi import APIRouter, HTTPException
from backend.app.schemas import SymptomCheckRequest, SymptomCheckResponse
from backend.app.services.symptom_service import analyze_symptoms_educational

router = APIRouter(prefix="/api/symptoms", tags=["Symptoms"])

@router.post("/check", response_model=SymptomCheckResponse)
def check_symptoms(request: SymptomCheckRequest):
    if len(request.symptoms.strip()) < 3:
        raise HTTPException(status_code=400, detail="Please enter a more detailed symptom description.")
        
    result = analyze_symptoms_educational(
        symptoms=request.symptoms,
        duration=request.duration or "Not specified",
        severity=request.severity or "Moderate",
        fever_present=request.fever_present or False,
        age_group=request.age_group or "Adult",
        language=request.language or "en"
    )
    
    return SymptomCheckResponse(**result)


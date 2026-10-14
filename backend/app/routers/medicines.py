from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from backend.app.services.medicine_service import search_medicines, get_medicine_by_id

router = APIRouter(prefix="/api/medicines", tags=["Medicines"])

@router.get("/search")
def search_medicine_endpoint(query: Optional[str] = Query(None, description="Search term")):
    results = search_medicines(query)
    return {
        "query": query or "",
        "count": len(results),
        "results": results,
        "safety_notice": (
            "SAFETY NOTICE: This medicine library provides general information regarding uses, side effects, "
            "and precautions based on reliable public health references (WHO, NIH MedlinePlus, FDA). "
            "It does NOT prescribe medication, suggest off-label combinations, or recommend changing any prescription. "
            "Always consult your doctor or registered pharmacist before taking or discontinuing any medication."
        ),
        "is_verified": True
    }

@router.get("/{med_id}")
def get_medicine_detail(med_id: str):
    medicine = get_medicine_by_id(med_id)
    if not medicine:
        raise HTTPException(status_code=404, detail="Medicine information not found in verified registry.")
    return medicine


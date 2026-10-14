from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List
from backend.app.services.education_service import get_all_education_topics, get_education_topic_by_id

router = APIRouter(prefix="/api/education", tags=["Education"])

@router.get("/topics")
def list_topics(
    query: Optional[str] = Query(None, description="Search query across topic titles, summaries, and signs"),
    category: Optional[str] = Query(None, description="Filter by category")
):
    topics = get_all_education_topics(query=query, category=category)
    return {
        "count": len(topics),
        "topics": topics
    }

@router.get("/topics/{topic_id}")
def get_topic(topic_id: str):
    topic = get_education_topic_by_id(topic_id)
    if not topic:
        raise HTTPException(status_code=404, detail="Educational topic not found.")
    return topic


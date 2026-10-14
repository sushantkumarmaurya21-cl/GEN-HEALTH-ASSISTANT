from fastapi import APIRouter, HTTPException, Depends
from datetime import datetime, timezone
import sqlite3
from backend.app.schemas import ChatRequest, ChatResponse
from backend.app.services.ai_service import process_chat_query
from backend.app.database import get_connection

router = APIRouter(prefix="/api/chat", tags=["Chat"])

@router.post("", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty.")
        
    # Format history as dictionaries
    history_dicts = [{"role": msg.role, "content": msg.content} for msg in (request.history or [])]
    
    # Process through AI service
    ai_result = await process_chat_query(
        message=request.message,
        language=request.language or "en",
        history=history_dicts
    )
    
    # Persist interaction in SQLite
    conn = get_connection()
    try:
        cursor = conn.cursor()
        now_iso = datetime.now(timezone.utc).isoformat()
        
        # Save user message
        cursor.execute("""
            INSERT INTO chat_history (session_id, role, content, language, is_demo, created_at)
            VALUES (?, 'user', ?, ?, 0, ?)
        """, (request.session_id, request.message, request.language, now_iso))
        
        # Save assistant message
        cursor.execute("""
            INSERT INTO chat_history (session_id, role, content, language, is_demo, created_at)
            VALUES (?, 'assistant', ?, ?, ?, ?)
        """, (request.session_id, ai_result["reply"], request.language, 1 if ai_result["is_demo"] else 0, now_iso))
        
        conn.commit()
    finally:
        conn.close()
        
    return ChatResponse(
        reply=ai_result["reply"],
        language=ai_result["language"],
        is_demo=ai_result["is_demo"],
        provider=ai_result["provider"],
        suggested_follow_ups=ai_result["suggested_follow_ups"],
        emergency_warning=ai_result["emergency_warning"],
        disclaimer=ai_result["disclaimer"]
    )

@router.get("/history/{session_id}")
def get_chat_history(session_id: str):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, role, content, language, is_demo, created_at as timestamp 
            FROM chat_history 
            WHERE session_id = ? 
            ORDER BY id ASC
        """, (session_id,))
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    finally:
        conn.close()

@router.delete("/history/{session_id}")
def clear_chat_history(session_id: str):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM chat_history WHERE session_id = ?", (session_id,))
        conn.commit()
        return {"status": "success", "message": f"Chat history cleared for session {session_id}"}
    finally:
        conn.close()


from fastapi import APIRouter, HTTPException, Query
from datetime import datetime, timezone, date
import sqlite3
from typing import Optional, List
from backend.app.schemas import (
    WellnessRecordCreate, 
    WellnessRecordUpdate, 
    WellnessRecordResponse,
    UserProfile,
    UserProfileUpdate
)
from backend.app.database import get_connection

router = APIRouter(prefix="/api/wellness", tags=["Wellness Tracker"])

@router.get("/records")
def get_wellness_records(days: int = Query(7, ge=1, le=90)):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, record_date, water_ml, sleep_hours, sleep_quality, 
                   steps, active_minutes, calories_burned, notes, updated_at
            FROM wellness_records
            ORDER BY record_date DESC
            LIMIT ?
        """, (days,))
        rows = cursor.fetchall()
        records = [dict(row) for row in rows]
        
        # Calculate weekly summary stats
        total_water = sum(r["water_ml"] for r in records)
        total_steps = sum(r["steps"] for r in records)
        avg_sleep = round(sum(r["sleep_hours"] for r in records) / len(records), 1) if records else 0.0
        avg_water = round(total_water / len(records)) if records else 0
        avg_steps = round(total_steps / len(records)) if records else 0
        
        return {
            "records": records,
            "summary": {
                "days_tracked": len(records),
                "avg_water_ml": avg_water,
                "avg_sleep_hours": avg_sleep,
                "avg_steps": avg_steps,
                "total_steps": total_steps
            },
            "disclaimer": "These entries are self-reported personal wellness logs and should not be used as clinical diagnostic measurements."
        }
    finally:
        conn.close()

@router.post("/records", response_model=WellnessRecordResponse)
def save_or_update_record(record: WellnessRecordCreate):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        now_iso = datetime.now(timezone.utc).isoformat()
        
        cursor.execute("""
            INSERT INTO wellness_records (
                record_date, water_ml, sleep_hours, sleep_quality, 
                steps, active_minutes, calories_burned, notes, updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(record_date) DO UPDATE SET
                water_ml = excluded.water_ml,
                sleep_hours = excluded.sleep_hours,
                sleep_quality = excluded.sleep_quality,
                steps = excluded.steps,
                active_minutes = excluded.active_minutes,
                calories_burned = excluded.calories_burned,
                notes = excluded.notes,
                updated_at = excluded.updated_at
        """, (
            record.record_date, record.water_ml, record.sleep_hours, record.sleep_quality,
            record.steps, record.active_minutes, record.calories_burned, record.notes or "", now_iso
        ))
        conn.commit()
        
        cursor.execute("SELECT * FROM wellness_records WHERE record_date = ?", (record.record_date,))
        row = cursor.fetchone()
        return dict(row)
    finally:
        conn.close()

@router.get("/profile", response_model=UserProfile)
def get_user_profile():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user_profile WHERE id = 1")
        row = cursor.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="User profile not found")
        return dict(row)
    finally:
        conn.close()

@router.put("/profile", response_model=UserProfile)
def update_user_profile(profile_update: UserProfileUpdate):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        now_iso = datetime.now(timezone.utc).isoformat()
        
        # Read current
        cursor.execute("SELECT * FROM user_profile WHERE id = 1")
        current = dict(cursor.fetchone())
        
        new_name = profile_update.display_name if profile_update.display_name is not None else current["display_name"]
        new_water = profile_update.water_goal_ml if profile_update.water_goal_ml is not None else current["water_goal_ml"]
        new_sleep = profile_update.sleep_goal_hours if profile_update.sleep_goal_hours is not None else current["sleep_goal_hours"]
        new_steps = profile_update.steps_goal if profile_update.steps_goal is not None else current["steps_goal"]
        new_lang = profile_update.preferred_language if profile_update.preferred_language is not None else current["preferred_language"]
        
        cursor.execute("""
            UPDATE user_profile 
            SET display_name = ?, water_goal_ml = ?, sleep_goal_hours = ?, 
                steps_goal = ?, preferred_language = ?, updated_at = ?
            WHERE id = 1
        """, (new_name, new_water, new_sleep, new_steps, new_lang, now_iso))
        conn.commit()
        
        cursor.execute("SELECT * FROM user_profile WHERE id = 1")
        return dict(cursor.fetchone())
    finally:
        conn.close()


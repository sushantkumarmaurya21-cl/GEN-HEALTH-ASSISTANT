import pytest
from fastapi.testclient import TestClient
from backend.app.main import app
from backend.app.database import init_db

# Initialize database for test environment
init_db()
client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "HealthCare AI" in data["message"]
    assert "disclaimer" in data

def test_system_status():
    response = client.get("/api/system/status")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "active_provider" in data
    assert "en" in data["supported_languages"]

def test_symptom_checker_normal():
    response = client.post("/api/symptoms/check", json={
        "symptoms": "Mild headache and feeling tired for 2 days after working on laptop",
        "duration": "2 days",
        "severity": "Mild",
        "language": "en"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["is_emergency"] is False
    assert len(data["possible_educational_causes"]) > 0
    assert len(data["follow_up_questions"]) > 0
    assert "strict_disclaimer" in data

def test_symptom_checker_emergency_detection():
    # Crucial medical safety requirement: detect life-threatening emergency signs
    response = client.post("/api/symptoms/check", json={
        "symptoms": "Sudden severe chest pain radiating to left arm and cannot breathe",
        "duration": "10 minutes",
        "severity": "Severe",
        "language": "en"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["is_emergency"] is True
    assert data["emergency_guidance"] is not None
    assert "CRITICAL SAFETY ALERT" in data["emergency_guidance"]

def test_education_topics():
    response = client.get("/api/education/topics")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] >= 10
    
    # Test specific topic
    topic_resp = client.get("/api/education/topics/fever")
    assert topic_resp.status_code == 200
    assert topic_resp.json()["id"] == "fever"

def test_medicine_search():
    response = client.get("/api/medicines/search?query=paracetamol")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] >= 1
    assert data["is_verified"] is True
    assert "safety_notice" in data

def test_wellness_records():
    # Read existing records
    response = client.get("/api/wellness/records?days=7")
    assert response.status_code == 200
    data = response.json()
    assert "records" in data
    assert "summary" in data
    
    # Post a new record
    new_record = {
        "record_date": "2026-10-14",
        "water_ml": 2400,
        "sleep_hours": 7.5,
        "sleep_quality": "Good",
        "steps": 8500,
        "active_minutes": 45,
        "calories_burned": 350,
        "notes": "Testing record log"
    }
    save_resp = client.post("/api/wellness/records", json=new_record)
    assert save_resp.status_code == 200
    assert save_resp.json()["water_ml"] == 2400

def test_chat_demo_mode():
    response = client.post("/api/chat", json={
        "message": "What is the recommended daily water intake?",
        "language": "en",
        "session_id": "test_session_1"
    })
    assert response.status_code == 200
    data = response.json()
    assert len(data["reply"]) > 20
    assert "disclaimer" in data
    assert "provider" in data
    # Clear test session history
    clear_resp = client.delete("/api/chat/history/test_session_1")
    assert clear_resp.status_code == 200


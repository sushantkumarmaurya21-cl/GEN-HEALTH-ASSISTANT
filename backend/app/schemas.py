from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

# Chat Schemas
class ChatMessage(BaseModel):
    role: str = Field(..., description="'user', 'assistant', or 'system'")
    content: str = Field(..., description="Message content")
    timestamp: Optional[str] = None
    is_demo: Optional[bool] = False

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=2000, description="User query or message")
    session_id: Optional[str] = Field(default="default_session", description="Session identifier")
    language: Optional[str] = Field(default="en", description="'en' for English or 'hi' for Hindi")
    history: Optional[List[ChatMessage]] = Field(default_factory=list, description="Recent conversation turns")

class ChatResponse(BaseModel):
    reply: str
    language: str
    is_demo: bool
    provider: str
    suggested_follow_ups: List[str] = Field(default_factory=list)
    emergency_warning: Optional[str] = None
    disclaimer: str

# Symptom Checker Schemas
class SymptomCheckRequest(BaseModel):
    symptoms: str = Field(..., min_length=3, max_length=2000, description="User symptom description in free text")
    duration: Optional[str] = Field(default="Not specified", description="Duration (e.g., '2 days')")
    severity: Optional[str] = Field(default="Moderate", description="Mild, Moderate, or Severe")
    fever_present: Optional[bool] = False
    age_group: Optional[str] = Field(default="Adult", description="Child, Adult, Elderly")
    answers_to_followups: Optional[Dict[str, str]] = Field(default_factory=dict)
    language: Optional[str] = Field(default="en")

class SymptomCheckResponse(BaseModel):
    summary: str
    is_emergency: bool
    emergency_guidance: Optional[str] = None
    possible_educational_causes: List[Dict[str, Any]]
    follow_up_questions: List[str]
    general_self_care_tips: List[str]
    when_to_see_doctor: List[str]
    strict_disclaimer: str
    is_demo: bool

# Wellness Records Schemas
class WellnessRecordBase(BaseModel):
    record_date: str
    water_ml: int = Field(default=0, ge=0, le=10000)
    sleep_hours: float = Field(default=0.0, ge=0.0, le=24.0)
    sleep_quality: str = Field(default="Normal")
    steps: int = Field(default=0, ge=0, le=100000)
    active_minutes: int = Field(default=0, ge=0, le=1440)
    calories_burned: int = Field(default=0, ge=0, le=10000)
    notes: Optional[str] = ""

class WellnessRecordCreate(WellnessRecordBase):
    pass

class WellnessRecordUpdate(BaseModel):
    water_ml: Optional[int] = None
    sleep_hours: Optional[float] = None
    sleep_quality: Optional[str] = None
    steps: Optional[int] = None
    active_minutes: Optional[int] = None
    calories_burned: Optional[int] = None
    notes: Optional[str] = None

class WellnessRecordResponse(WellnessRecordBase):
    id: int
    updated_at: str

class UserProfile(BaseModel):
    display_name: str
    water_goal_ml: int
    sleep_goal_hours: float
    steps_goal: int
    preferred_language: str
    updated_at: str

class UserProfileUpdate(BaseModel):
    display_name: Optional[str] = None
    water_goal_ml: Optional[int] = None
    sleep_goal_hours: Optional[float] = None
    steps_goal: Optional[int] = None
    preferred_language: Optional[str] = None

# Medicine Information Schemas
class MedicineDetail(BaseModel):
    id: str
    name: str
    generic_name: str
    drug_class: str
    common_uses: List[str]
    standard_precautions: List[str]
    possible_side_effects: List[str]
    contraindications_and_warnings: List[str]
    storage_info: str
    is_prescription_only: bool
    verified_source: str
    source_url: str

class MedicineSearchResponse(BaseModel):
    query: str
    count: int
    results: List[MedicineDetail]
    safety_notice: str
    is_verified: bool

# Health Education Schemas
class HealthTopic(BaseModel):
    id: str
    title: str
    hindi_title: str
    category: str
    summary: str
    common_signs: List[str]
    prevention_tips: List[str]
    when_to_seek_care: List[str]
    emergency_warning_signs: List[str]
    reliable_references: List[Dict[str, str]]

# Emergency Help Schemas
class EmergencyGuideItem(BaseModel):
    id: str
    title: str
    subtitle: str
    icon: str
    priority_steps: List[str]
    do_not_do: List[str]
    when_to_call_emergency: str
    official_reference: str

# System Status
class SystemStatus(BaseModel):
    status: str
    ai_configured: bool
    active_provider: str
    supported_languages: List[str]
    disclaimer: str


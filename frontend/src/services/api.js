const API_BASE = '/api';

export async function getSystemStatus() {
  try {
    const res = await fetch(`${API_BASE}/system/status`);
    if (!res.ok) throw new Error('Failed to fetch status');
    return await res.json();
  } catch (err) {
    console.warn('Backend unavailable, using client fallback info:', err);
    return {
      status: 'offline',
      ai_configured: false,
      active_provider: 'Demo Mode (Offline Mock Simulation)',
      supported_languages: ['en', 'hi'],
      disclaimer: 'Educational prototype only. Not a substitute for a doctor.'
    };
  }
}

export async function sendChatMessage(message, language = 'en', sessionId = 'default_session', history = []) {
  const res = await fetch(`${API_BASE}/chat`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message, language, session_id: sessionId, history })
  });
  if (!res.ok) {
    const errData = await res.json().catch(() => ({}));
    throw new Error(errData.detail || 'Failed to send message');
  }
  return await res.json();
}

export async function getChatHistory(sessionId = 'default_session') {
  try {
    const res = await fetch(`${API_BASE}/chat/history/${sessionId}`);
    if (!res.ok) return [];
    return await res.json();
  } catch {
    return [];
  }
}

export async function clearChatHistory(sessionId = 'default_session') {
  const res = await fetch(`${API_BASE}/chat/history/${sessionId}`, { method: 'DELETE' });
  return await res.json();
}

export async function checkSymptoms(payload) {
  const res = await fetch(`${API_BASE}/symptoms/check`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });
  if (!res.ok) {
    const errData = await res.json().catch(() => ({}));
    throw new Error(errData.detail || 'Failed to analyze symptoms');
  }
  return await res.json();
}

export async function getEducationTopics(query = '', category = '') {
  const params = new URLSearchParams();
  if (query) params.append('query', query);
  if (category && category !== 'All') params.append('category', category);
  const res = await fetch(`${API_BASE}/education/topics?${params.toString()}`);
  if (!res.ok) throw new Error('Failed to load education topics');
  return await res.json();
}

export async function getEducationTopic(topicId) {
  const res = await fetch(`${API_BASE}/education/topics/${topicId}`);
  if (!res.ok) throw new Error('Topic not found');
  return await res.json();
}

export async function searchMedicines(query = '') {
  const params = new URLSearchParams();
  if (query) params.append('query', query);
  const res = await fetch(`${API_BASE}/medicines/search?${params.toString()}`);
  if (!res.ok) throw new Error('Failed to search medicines');
  return await res.json();
}

export async function getMedicine(id) {
  const res = await fetch(`${API_BASE}/medicines/${id}`);
  if (!res.ok) throw new Error('Medicine not found');
  return await res.json();
}

export async function getWellnessRecords(days = 7) {
  const res = await fetch(`${API_BASE}/wellness/records?days=${days}`);
  if (!res.ok) throw new Error('Failed to fetch wellness records');
  return await res.json();
}

export async function saveWellnessRecord(data) {
  const res = await fetch(`${API_BASE}/wellness/records`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  if (!res.ok) throw new Error('Failed to save wellness record');
  return await res.json();
}

export async function getUserProfile() {
  const res = await fetch(`${API_BASE}/wellness/profile`);
  if (!res.ok) throw new Error('Failed to load profile');
  return await res.json();
}

export async function updateUserProfile(data) {
  const res = await fetch(`${API_BASE}/wellness/profile`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  if (!res.ok) throw new Error('Failed to update profile');
  return await res.json();
}

export async function getEmergencyGuides() {
  const res = await fetch(`${API_BASE}/emergency/guides`);
  if (!res.ok) throw new Error('Failed to fetch emergency guides');
  return await res.json();
}

export async function getEmergencyContacts() {
  const res = await fetch(`${API_BASE}/emergency/contacts`);
  if (!res.ok) throw new Error('Failed to fetch emergency contacts');
  return await res.json();
}

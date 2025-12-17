from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from models import ChatMessage, SenderType, MessageStatus


class ChatRequest(BaseModel):
    content: str
    context_hint: Optional[str] = ""


class ChatResponse(BaseModel):
    response: str
    sources: List[str]
    context_used: List[str]
    timestamp: datetime


class SessionCreateRequest(BaseModel):
    user_id: Optional[str] = None
    initial_context: Optional[str] = ""


class SessionResponse(BaseModel):
    session_id: str
    timestamp: datetime
    message: str


class SearchRequest(BaseModel):
    query: str
    max_results: Optional[int] = 5
    filters: Optional[dict] = {}


class SearchResponse(BaseModel):
    results: List[dict]
    total_results: int


class ContentRequest(BaseModel):
    content_id: str


class ContentResponse(BaseModel):
    id: str
    title: str
    content: str
    path: str
    metadata: dict
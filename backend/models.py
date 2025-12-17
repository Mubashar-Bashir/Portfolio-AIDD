from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum


class SenderType(str, Enum):
    USER = "USER"
    ASSISTANT = "ASSISTANT"


class MessageStatus(str, Enum):
    SENT = "sent"
    DELIVERED = "delivered"
    ERROR = "error"


class BookContent(BaseModel):
    id: str
    title: str
    content: str
    path: str
    metadata: Optional[Dict[str, Any]] = {}


class ChatMessage(BaseModel):
    id: str
    sender_type: SenderType
    content: str
    timestamp: datetime
    status: MessageStatus = MessageStatus.SENT


class ChatSession(BaseModel):
    id: str
    user_id: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    is_active: bool = True
    messages: List[ChatMessage] = []


class User(BaseModel):
    id: str
    name: Optional[str] = None
    email: Optional[str] = None
    created_at: datetime


class SearchIndex(BaseModel):
    id: str
    content_id: str
    embedding: List[float]
    metadata: Dict[str, Any]
    created_at: datetime
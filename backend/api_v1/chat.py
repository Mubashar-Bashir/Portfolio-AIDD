from fastapi import APIRouter, HTTPException
from typing import List
import uuid
from datetime import datetime

from models import ChatMessage, ChatSession, SenderType, MessageStatus
from schemas import ChatRequest, ChatResponse, SessionCreateRequest, SessionResponse

router = APIRouter()

# In-memory storage for demo purposes
chat_sessions: dict = {}

@router.post("/start", response_model=SessionResponse)
async def start_chat_session(request: SessionCreateRequest):
    session_id = f"session_{uuid.uuid4()}"

    new_session = ChatSession(
        id=session_id,
        user_id=request.user_id,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        is_active=True,
        messages=[]
    )

    chat_sessions[session_id] = new_session

    return SessionResponse(
        session_id=session_id,
        timestamp=datetime.utcnow(),
        message="Session started successfully"
    )


@router.post("/{session_id}/message", response_model=ChatResponse)
async def send_message(session_id: str, request: ChatRequest):
    if session_id not in chat_sessions:
        raise HTTPException(status_code=404, detail="Session not found")

    session = chat_sessions[session_id]

    # Add user message
    user_message = ChatMessage(
        id=f"msg_{uuid.uuid4()}",
        sender_type=SenderType.USER,
        content=request.content,
        timestamp=datetime.utcnow(),
        status=MessageStatus.SENT
    )

    session.messages.append(user_message)

    # Generate a simple "Hello World" response or basic echo
    if "hello" in request.content.lower() or "hi" in request.content.lower():
        response_content = "Hello! Welcome to the book assistant. How can I help you with the book content?"
    else:
        response_content = f"I received your message: '{request.content}'. This is a sample response from the chatbot."

    # Add assistant message
    assistant_message = ChatMessage(
        id=f"msg_{uuid.uuid4()}",
        sender_type=SenderType.ASSISTANT,
        content=response_content,
        timestamp=datetime.utcnow(),
        status=MessageStatus.SENT
    )

    session.messages.append(assistant_message)
    session.updated_at = datetime.utcnow()

    # Update session in storage
    chat_sessions[session_id] = session

    return ChatResponse(
        response=response_content,
        sources=["docs/intro.md"],  # Mock source
        context_used=[request.content[:50]],  # Mock context
        timestamp=datetime.utcnow()
    )


@router.get("/{session_id}", response_model=ChatSession)
async def get_chat_session(session_id: str):
    if session_id not in chat_sessions:
        raise HTTPException(status_code=404, detail="Session not found")

    return chat_sessions[session_id]
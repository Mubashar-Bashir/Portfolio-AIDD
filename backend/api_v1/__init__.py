from fastapi import APIRouter

from . import chat, search, content

router = APIRouter()
router.include_router(chat.router, prefix="/chat", tags=["chat"])
router.include_router(search.router, prefix="/search", tags=["search"])
router.include_router(content.router, prefix="/content", tags=["content"])
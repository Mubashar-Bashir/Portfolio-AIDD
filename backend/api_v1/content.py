from fastapi import APIRouter, HTTPException
from typing import Optional
from datetime import datetime

from schemas import ContentResponse

router = APIRouter()

# Mock content data for demo purposes
mock_content_store = {
    "intro": {
        "id": "intro",
        "title": "Introduction",
        "content": "This is the introduction to the book. Welcome to our comprehensive guide.",
        "path": "/docs/intro",
        "category": "introduction",
        "updated_at": datetime.utcnow()
    },
    "getting-started": {
        "id": "getting-started",
        "title": "Getting Started",
        "content": "This section covers the basics you need to know to get started with the concepts in this book.",
        "path": "/docs/getting-started",
        "category": "basics",
        "updated_at": datetime.utcnow()
    }
}

@router.get("/{content_id}", response_model=ContentResponse)
async def get_content(content_id: str):
    if content_id not in mock_content_store:
        raise HTTPException(status_code=404, detail="Content not found")

    content = mock_content_store[content_id]
    return ContentResponse(
        id=content["id"],
        title=content["title"],
        content=content["content"],
        path=content["path"],
        metadata={"category": content.get("category", ""), "updated_at": content["updated_at"]}
    )

@router.get("/list", response_model=dict)
async def list_content(limit: int = 10, offset: int = 0, category: Optional[str] = None):
    contents = list(mock_content_store.values())

    if category:
        contents = [c for c in contents if c.get("category") == category]

    total_count = len(contents)
    paginated_contents = contents[offset:offset + limit]

    return {
        "contents": [
            {
                "id": c["id"],
                "title": c["title"],
                "path": c["path"],
                "category": c.get("category", ""),
                "updated_at": c["updated_at"]
            }
            for c in paginated_contents
        ],
        "total_count": total_count,
        "has_more": offset + limit < total_count
    }
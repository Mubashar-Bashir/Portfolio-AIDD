from fastapi import APIRouter
from schemas import SearchRequest, SearchResponse

router = APIRouter()

# Mock search data for demo purposes
mock_content_data = [
    {
        "content_id": "intro",
        "title": "Introduction",
        "path": "/docs/intro",
        "content": "This is the introduction to the book...",
        "similarity_score": 0.95
    },
    {
        "content_id": "chapter1-getting-started",
        "title": "Getting Started",
        "path": "/docs/chapter-1/getting-started",
        "content": "This chapter covers the basics...",
        "similarity_score": 0.85
    }
]

@router.post("/", response_model=SearchResponse)
async def search_content(request: SearchRequest):
    # In a real implementation, this would connect to Qdrant or another search system
    # For now, we'll return mock results

    results = []
    for item in mock_content_data:
        if request.query.lower() in item["content"].lower() or request.query.lower() in item["title"].lower():
            results.append({
                "content_id": item["content_id"],
                "title": item["title"],
                "path": item["path"],
                "snippet": item["content"][:100] + "...",
                "similarity_score": item["similarity_score"]
            })

    # If no results found based on query, return top results
    if not results:
        results = [
            {
                "content_id": item["content_id"],
                "title": item["title"],
                "path": item["path"],
                "snippet": item["content"][:100] + "...",
                "similarity_score": item["similarity_score"]
            }
            for item in mock_content_data[:request.max_results]
        ]

    return SearchResponse(
        results=results,
        total_results=len(results)
    )
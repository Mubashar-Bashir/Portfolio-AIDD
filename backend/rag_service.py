"""
RAG (Retrieval Augmented Generation) Service for context retrieval
This is a mock implementation that simulates RAG functionality
"""

from typing import List, Dict, Any
import logging

# Mock database of content for retrieval
MOCK_CONTENT_DB = {
    "intro": {
        "id": "intro",
        "title": "Introduction",
        "content": "Welcome to our comprehensive book on Docusaurus and ChatKit integration. This guide will walk you through creating a powerful documentation site with integrated chat capabilities.",
        "path": "/docs/intro",
        "embedding": [0.1, 0.2, 0.3, 0.4, 0.5]  # Mock embedding
    },
    "creating-document": {
        "id": "creating-document",
        "title": "Creating a Document",
        "content": "To create a new document, create a Markdown file in the docs/ directory with proper frontmatter. Add a title and sidebar position to make it appear in navigation.",
        "path": "/docs/tutorial-basics/creating-a-document",
        "embedding": [0.6, 0.7, 0.8, 0.9, 1.0]  # Mock embedding
    }
}

class RAGService:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    async def retrieve_context(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """
        Retrieve relevant context based on the query
        """
        self.logger.info(f"Retrieving context for query: {query}")

        # Simple keyword matching for demo purposes
        results = []
        query_lower = query.lower()

        for content_id, content_data in MOCK_CONTENT_DB.items():
            content_text = content_data['content'].lower()
            if any(keyword in content_text for keyword in query_lower.split()):
                results.append({
                    "id": content_data["id"],
                    "title": content_data["title"],
                    "content": content_data["content"],
                    "path": content_data["path"],
                    "similarity_score": 0.8  # Mock similarity score
                })

        # If no keyword matches, return top results
        if not results:
            results = [
                {
                    "id": content_data["id"],
                    "title": content_data["title"],
                    "content": content_data["content"],
                    "path": content_data["path"],
                    "similarity_score": 0.5
                }
                for content_data in list(MOCK_CONTENT_DB.values())[:top_k]
            ]

        return results[:top_k]

    async def search_content(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """
        Search for content based on query
        """
        return await self.retrieve_context(query, top_k)

    async def get_content_by_id(self, content_id: str) -> Dict[str, Any]:
        """
        Get specific content by ID
        """
        if content_id in MOCK_CONTENT_DB:
            content_data = MOCK_CONTENT_DB[content_id]
            return {
                "id": content_data["id"],
                "title": content_data["title"],
                "content": content_data["content"],
                "path": content_data["path"],
                "metadata": {}
            }
        else:
            raise ValueError(f"Content with ID {content_id} not found")

# Global RAG service instance
rag_service = RAGService()
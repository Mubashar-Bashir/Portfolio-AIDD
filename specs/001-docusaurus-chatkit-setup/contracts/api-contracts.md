# API Contracts: Docusaurus ChatKit Setup

## Chat API

### POST /api/chat/start
**Description**: Start a new chat session
**Request**:
- Headers: `Content-Type: application/json`
- Body:
  ```json
  {
    "user_id": "string (optional)",
    "initial_context": "string (optional)"
  }
  ```
**Response**:
- Status: 201 Created
- Body:
  ```json
  {
    "session_id": "string",
    "timestamp": "datetime",
    "message": "Session started successfully"
  }
  ```

### POST /api/chat/{session_id}/message
**Description**: Send a message in an existing chat session
**Request**:
- Headers: `Content-Type: application/json`
- Path params: `session_id`
- Body:
  ```json
  {
    "content": "string (user message content)",
    "context_hint": "string (optional hint about relevant content)"
  }
  ```
**Response**:
- Status: 200 OK
- Body:
  ```json
  {
    "response": "string (AI response)",
    "sources": ["string (references to book sections)"],
    "context_used": ["string (relevant content chunks)"],
    "timestamp": "datetime"
  }
  ```

### GET /api/chat/{session_id}
**Description**: Get chat session details
**Request**:
- Path params: `session_id`
**Response**:
- Status: 200 OK
- Body:
  ```json
  {
    "session_id": "string",
    "created_at": "datetime",
    "updated_at": "datetime",
    "is_active": "boolean",
    "messages": [
      {
        "id": "string",
        "sender_type": "USER | ASSISTANT",
        "content": "string",
        "timestamp": "datetime"
      }
    ]
  }
  ```

## Search API

### POST /api/search
**Description**: Search book content with semantic search
**Request**:
- Headers: `Content-Type: application/json`
- Body:
  ```json
  {
    "query": "string (search query)",
    "max_results": "integer (optional, default: 5)",
    "filters": "object (optional metadata filters)"
  }
  ```
**Response**:
- Status: 200 OK
- Body:
  ```json
  {
    "results": [
      {
        "content_id": "string",
        "title": "string",
        "path": "string",
        "snippet": "string (relevant text snippet)",
        "similarity_score": "float (0.0-1.0)"
      }
    ],
    "total_results": "integer"
  }
  ```

## Content API

### GET /api/content/{content_id}
**Description**: Get specific book content by ID
**Request**:
- Path params: `content_id`
**Response**:
- Status: 200 OK
- Body:
  ```json
  {
    "id": "string",
    "title": "string",
    "content": "string",
    "path": "string",
    "metadata": "object"
  }
  ```

### GET /api/content/list
**Description**: List available book content
**Request**:
- Query params: `limit`, `offset`, `category` (optional filters)
**Response**:
- Status: 200 OK
- Body:
  ```json
  {
    "contents": [
      {
        "id": "string",
        "title": "string",
        "path": "string",
        "category": "string",
        "updated_at": "datetime"
      }
    ],
    "total_count": "integer",
    "has_more": "boolean"
  }
  ```
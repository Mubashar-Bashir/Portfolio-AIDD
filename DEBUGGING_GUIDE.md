# Debugging Guide for Docusaurus + ChatKit Implementation

## 1. Frontend Debugging Tools and Techniques

### 1.1. Browser Developer Tools Setup
- **Network Tab**: Monitor API calls to backend
  - Check request/response headers
  - Verify request payloads
  - Monitor response times
  - Identify failed requests

- **Console**: Enable structured logging
  - Set console log level appropriately
  - Use console.group for related logs
  - Monitor for JavaScript errors
  - Check for React warnings

- **React DevTools**: Component inspection
  - Monitor component state changes
  - Check prop values
  - Identify re-render issues
  - Verify component hierarchy

### 1.2. Frontend Error Handling Enhancement
Create a comprehensive error handling system:

```javascript
// Enhanced error handling in apiClient.js
class ApiClient {
  async makeRequest(endpoint, options = {}) {
    const url = `${this.baseUrl}${endpoint}`;

    try {
      console.group('API Request', endpoint);
      console.log('Payload:', options.body);

      const response = await fetch(url, {
        headers: {
          'Content-Type': 'application/json',
          ...options.headers
        },
        ...options
      });

      console.log('Response Status:', response.status);

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        console.error('API Error:', errorData);
        throw new Error(`API Error: ${response.status} - ${errorData.detail || response.statusText}`);
      }

      const data = await response.json();
      console.log('Response Data:', data);
      console.groupEnd();

      return data;
    } catch (error) {
      console.error('Network Error:', error);
      console.groupEnd();
      throw error;
    }
  }
}
```

### 1.3. Frontend Debugging Utilities
Create debugging utilities for the ChatKit:

```javascript
// frontend/src/utils/debug.js
export const debug = {
  log: (module, message, data = null) => {
    if (process.env.NODE_ENV === 'development') {
      console.group(`[DEBUG] ${module}`);
      console.log(message);
      if (data) console.log('Data:', data);
      console.groupEnd();
    }
  },

  error: (module, error, context = null) => {
    console.group(`[ERROR] ${module}`);
    console.error(error);
    if (context) console.log('Context:', context);
    console.groupEnd();
  },

  performance: (label, fn) => {
    if (process.env.NODE_ENV === 'development') {
      console.time(label);
      const result = fn();
      console.timeEnd(label);
      return result;
    }
    return fn();
  }
};
```

## 2. Backend Debugging Tools and Techniques

### 2.1. Enhanced Logging Setup
Update the backend to include structured logging:

```python
# backend/utils/logger.py
import logging
import json
from datetime import datetime
from typing import Dict, Any

class StructuredLogger:
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def _log_structured(self, level: str, event: str, data: Dict[str, Any] = None):
        log_data = {
            'timestamp': datetime.utcnow().isoformat(),
            'event': event,
            'level': level
        }
        if data:
            log_data.update(data)

        getattr(self.logger, level.lower())(json.dumps(log_data))

    def info(self, event: str, data: Dict[str, Any] = None):
        self._log_structured('INFO', event, data)

    def error(self, event: str, data: Dict[str, Any] = None):
        self._log_structured('ERROR', event, data)

    def debug(self, event: str, data: Dict[str, Any] = None):
        self._log_structured('DEBUG', event, data)

# Usage in chat.py
logger = StructuredLogger(__name__)

@router.post("/message")
async def send_message(request: ChatRequest, session_id: str):
    logger.info("message_received", {
        "session_id": session_id,
        "content_length": len(request.content),
        "timestamp": datetime.utcnow().isoformat()
    })

    try:
        # Process message
        response = await process_chat_message(request.content)
        logger.info("message_processed", {
            "session_id": session_id,
            "response_length": len(response)
        })
        return ChatResponse(response=response, sources=[], context_used=[])
    except Exception as e:
        logger.error("message_processing_failed", {
            "session_id": session_id,
            "error": str(e),
            "traceback": str(e.__traceback__) if e.__traceback__ else None
        })
        raise
```

### 2.2. Health Check and Monitoring Endpoints
Add comprehensive health checks:

```python
# backend/main.py - Add these endpoints
@app.get("/health/extended")
async def extended_health_check():
    """Extended health check with system status"""
    import psutil
    import os

    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "system": {
            "cpu_percent": psutil.cpu_percent(),
            "memory_percent": psutil.virtual_memory().percent,
            "disk_percent": psutil.disk_usage('/').percent,
            "process_count": len(psutil.pids())
        },
        "services": {
            "api": "running",
            "database": "not_configured",  # Update when DB is added
            "vector_store": "not_configured"  # Update when vector store is added
        }
    }

@app.get("/debug/session/{session_id}")
async def debug_session(session_id: str):
    """Debug endpoint to inspect session state"""
    if session_id not in chat_sessions:
        raise HTTPException(status_code=404, detail="Session not found")

    session = chat_sessions[session_id]
    return {
        "session_id": session.id,
        "user_id": session.user_id,
        "message_count": len(session.messages),
        "created_at": session.created_at,
        "updated_at": session.updated_at,
        "is_active": session.is_active,
        "messages": [
            {
                "id": msg.id,
                "sender": msg.sender_type.value,
                "timestamp": msg.timestamp,
                "status": msg.status.value,
                "content_preview": msg.content[:50] + "..." if len(msg.content) > 50 else msg.content
            }
            for msg in session.messages[-5:]  # Last 5 messages
        ]
    }
```

## 3. Debugging Commands and Scripts

### 3.1. Frontend Debugging Commands
Add debugging scripts to package.json:

```json
{
  "scripts": {
    "debug": "docusaurus start --host 0.0.0.0 --port 3000",
    "debug:verbose": "VERBOSE_LOGGING=true docusaurus start",
    "analyze": "npm run build && npx webpack-bundle-analyzer build/bundle-stats.json",
    "test:debug": "npm test -- --watch --verbose"
  }
}
```

### 3.2. Backend Debugging Commands
Create debugging scripts:

```bash
#!/bin/bash
# debug_backend.sh
echo "Starting backend with detailed logging..."
uvicorn main:app --reload --host 0.0.0.0 --port 8000 --log-level debug
```

### 3.3. Environment Debugging
Create environment validation:

```bash
#!/bin/bash
# validate_env.sh
echo "Validating environment setup..."

# Check Node.js version
NODE_VERSION=$(node --version)
echo "Node.js version: $NODE_VERSION"

# Check npm version
NPM_VERSION=$(npm --version)
echo "NPM version: $NPM_VERSION"

# Check Python version
PYTHON_VERSION=$(python3 --version)
echo "Python version: $PYTHON_VERSION"

# Check if backend dependencies are installed
if python3 -c "import fastapi" 2>/dev/null; then
    echo "✓ FastAPI is installed"
else
    echo "✗ FastAPI is not installed"
    echo "Run: pip install -r requirements.txt"
fi

# Check if frontend dependencies are installed
if [ -d "node_modules" ]; then
    echo "✓ Frontend dependencies are installed"
else
    echo "✗ Frontend dependencies are not installed"
    echo "Run: cd frontend && npm install"
fi

# Test backend health
if curl -f http://localhost:8000/health >/dev/null 2>&1; then
    echo "✓ Backend is running and healthy"
else
    echo "✗ Backend is not responding"
    echo "Start backend with: cd backend && uvicorn main:app --reload"
fi

# Test frontend build
cd frontend
if npm run build --if-present; then
    echo "✓ Frontend builds successfully"
else
    echo "✗ Frontend build failed"
fi
cd ..

echo "Environment validation complete."
```

## 4. Common Debugging Scenarios and Solutions

### 4.1. API Connection Issues
**Symptoms**: Frontend can't reach backend
**Solutions**:
- Check if backend is running on correct port
- Verify CORS configuration
- Check network connectivity
- Validate API endpoint URLs

### 4.2. Session Management Issues
**Symptoms**: Chat sessions not persisting
**Solutions**:
- Check session ID generation
- Verify session storage
- Monitor session timeout
- Validate session cleanup

### 4.3. Message Processing Issues
**Symptoms**: Messages not displaying or processing
**Solutions**:
- Check message format validation
- Verify message storage
- Monitor processing delays
- Validate message rendering

## 5. Debugging Best Practices

### 5.1. Structured Debugging Approach
1. **Reproduce**: Consistently reproduce the issue
2. **Isolate**: Identify the specific component causing the issue
3. **Hypothesize**: Formulate a hypothesis about the root cause
4. **Test**: Test the hypothesis with minimal changes
5. **Fix**: Apply the fix and verify
6. **Prevent**: Add tests to prevent regression

### 5.2. Logging Best Practices
- Use structured logging with consistent format
- Include relevant context in logs
- Use appropriate log levels
- Avoid logging sensitive information
- Include timestamps and unique identifiers

### 5.3. Error Handling Best Practices
- Handle errors gracefully with user-friendly messages
- Log errors with sufficient context for debugging
- Implement retry mechanisms for transient failures
- Provide clear error recovery paths
- Monitor error rates and patterns

This debugging guide provides comprehensive tools and techniques to minimize troubleshooting overhead and quickly resolve issues in your Docusaurus + ChatKit implementation.
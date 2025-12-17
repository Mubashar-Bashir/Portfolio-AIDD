from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import os

from config import settings
import api_v1

# Create the FastAPI application
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set up CORS middleware
if settings.BACKEND_CORS_ORIGINS:
    origins = settings.BACKEND_CORS_ORIGINS.split(",")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        # Expose headers for client-side access
        expose_headers=["Access-Control-Allow-Origin"]
    )

# Include API routes
app.include_router(api_v1.router, prefix=settings.API_V1_STR)

@app.get("/")
def read_root():
    return {"message": "Docusaurus ChatKit Backend API", "status": "running"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "timestamp": "2025-12-15T18:25:00Z"}

# This would be run with: uvicorn main:app --reload
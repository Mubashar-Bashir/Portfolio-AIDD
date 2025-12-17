import os
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API Configuration
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Docusaurus ChatKit API"

    # Backend Configuration
    BACKEND_CORS_ORIGINS: str = os.getenv("BACKEND_CORS_ORIGINS", "http://localhost,http://localhost:3000,http://localhost:8080")

    # Cohere Configuration
    COHERE_API_KEY: Optional[str] = os.getenv("COHERE_API_KEY")

    # Qdrant Configuration
    QDRANT_URL: Optional[str] = os.getenv("QDRANT_URL", "http://localhost:6333")
    QDRANT_API_KEY: Optional[str] = os.getenv("QDRANT_API_KEY")

    # Environment
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    class Config:
        case_sensitive = True


def get_settings():
    return Settings()


# Global settings instance
settings = get_settings()
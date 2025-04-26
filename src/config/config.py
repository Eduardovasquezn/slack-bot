from typing import Optional, Literal
from pydantic import Field
from pathlib import Path
import os
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(
    __file__
).parent.parent.parent  # str(Path(__file__).parent.parent.parent)
ENV = os.getenv("ENVIRONMENT", "development")  # fallback to dev if not set

ENV_FILE = ROOT_DIR / f".env.{ENV}"  # dynamically choose the file


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_FILE, env_file_encoding="utf-8")
    """Central configuration settings for the application."""
    # --- Core Application Settings ---
    ENVIRONMENT: Literal["development", "production"] = "development"
    APP_NAME: str = "Slack Meeting Summarizer"
    DEBUG: bool = True
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "logs/app.log"

    # --- AI/ML Services ---
    EMBEDDING_MODEL: str = "text-embedding-3-small"
    EMBEDDING_DIMENSIONS: int = Field(1536, env="EMBEDDING_DIMENSIONS")
    EMBEDDING_PROVIDER: str = "openai"
    LLM_MODEL_NAME: str = "gpt-4o"
    OPENAI_API_KEY: str = Field(None, env="OPENAI_API_KEY")

    # --- Data Storage ---
    BUCKET_NAME: str = Field("team-meetings", env="BUCKET_NAME")

    # --- Qdrant Vector Database ---
    QDRANT_URL: str = Field("http://localhost:6333", env="QDRANT_URL")
    QDRANT_API_KEY: Optional[str] = Field(None, env="QDRANT_API_KEY")
    QDRANT_COLLECTION_NAME: str = Field("meetings", env="QDRANT_COLLECTION_NAME")

    # --- Monitoring (Optional) ---
    LANGFUSE_PUBLIC_KEY: Optional[str] = Field(None, env="LANGFUSE_PUBLIC_KEY")
    LANGFUSE_SECRET_KEY: Optional[str] = Field(None, env="LANGFUSE_SECRET_KEY")
    LANGFUSE_HOST: Optional[str] = Field(None, env="LANGFUSE_HOST")

    # --- Slack configuration ---
    SLACK_BOT_TOKEN: str = Field(None, env="SLACK_BOT_TOKEN")
    SLACK_SIGNING_SECRET: str = Field(None, env="SLACK_SIGNING_SECRET")
    SLACK_BOT_USER_ID: str = Field(None, env="SLACK_BOT_USER_ID")

    # --- Redis configuration ---
    REDIS_HOST: str = Field(None, env="REDIS_HOST")
    REDIS_PORT: int = Field(15591, env="REDIS_PORT")
    REDIS_USERNAME: Optional[str] = Field("default", env="REDIS_USERNAME")
    REDIS_PASSWORD: Optional[str] = Field(None, env="REDIS_PASSWORD")


# Instantiate settings
settings = Settings()

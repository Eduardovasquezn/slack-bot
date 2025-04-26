from langfuse import Langfuse
from openai import OpenAI
from google.cloud import storage
from config import settings
from pathlib import Path
from utils.custom_logging import get_logger
import redis

logger = get_logger()


def get_openai_client():
    """Return the initialized OpenAI client."""
    openai_client = OpenAI(api_key=settings.OPENAI_API_KEY)
    return openai_client


def get_langfuse_client():
    """Return the initialized LangFuse client."""
    langfuse_client = Langfuse(
        public_key=settings.LANGFUSE_PUBLIC_KEY,
        secret_key=settings.LANGFUSE_SECRET_KEY,
        host=settings.LANGFUSE_HOST,
    )
    return langfuse_client


def get_redis_client() -> redis.Redis:
    """
    Returns a Redis client using settings from the configuration.

    Returns:
        redis.Redis: A Redis client instance.
    """
    try:
        redis_client = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            decode_responses=True,
            username=settings.REDIS_USERNAME,
            password=settings.REDIS_PASSWORD,
        )
        # Optionally, check connection (ping to verify Redis is reachable)
        if redis_client.ping():
            logger.info("Successfully connected to Redis.")
        return redis_client
    except Exception as e:
        logger.error(f"Error connecting to Redis: {e}")
        raise


def create_google_storage_client() -> storage.Client:
    """
    Creates and returns a Google Cloud Storage client using service account credentials.

    The function first checks if the credentials file exists at the specified path.
    If the application is in a 'development' environment, it initializes the client using
    the service account credentials. In the 'production' environment, the client is
    initialized without specifying credentials (using the default application credentials).

    :raises FileNotFoundError: If the credentials file is not found at the expected location.

    :return: An instance of the Google Cloud Storage client.
    """
    try:
        # Path to the credentials file
        credentials_path = (
            Path(__file__).resolve().parent.parent.parent / "credentials.json"
        )

        logger.info("Initializing Google Cloud Storage client...")

        # Initialize client based on environment
        if settings.ENVIRONMENT == "development":
            storage_client = storage.Client.from_service_account_json(
                str(credentials_path)
            )
        elif settings.ENVIRONMENT == "production":
            storage_client = storage.Client()
        else:
            raise ValueError(
                "Invalid environment setting. Please check the 'ENVIRONMENT' configuration."
            )

        return storage_client

    except Exception as e:
        logger.error(f"Failed to create Google Cloud Storage client: {e}")


openai_client = get_openai_client()
langfuse_client = get_langfuse_client()
redis_client = get_redis_client()

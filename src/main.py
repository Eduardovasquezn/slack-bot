import functions_framework
from config import settings
from utils import (
    embedder,
    create_qdrant_client,
    create_qdrant_collection,
    insert_data_into_qdrant,
    extract_text_and_metadata,
)

# Connect to Qdrant
client_connection = create_qdrant_client()


@functions_framework.cloud_event
def offline_pipeline(cloud_event):
    """Event-based Cloud Function to ingest data into Qdrant."""
    try:
        print("Starting offline pipeline...")
        print(f"Bucket name used: {settings.BUCKET_NAME}")
        print(f"QDRANT_URL: {settings.QDRANT_URL}")
        data = extract_text_and_metadata(
            bucket_name=settings.BUCKET_NAME, extract_all=True
        )
        print(f"Extracted data: {data}")

        create_qdrant_collection(
            qdrant_client=client_connection,
            collection_name=settings.QDRANT_COLLECTION_NAME,
            vector_dimensions=settings.EMBEDDING_DIMENSIONS,
        )

        print("Starting insertion...")
        insert_data_into_qdrant(
            data,
            client_connection,
            collection_name=settings.QDRANT_COLLECTION_NAME,
            embedder=embedder,
        )

        print("Data inserted into Qdrant successfully.")

    except Exception as e:
        return {"error": str(e)}, 500

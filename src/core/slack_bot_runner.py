from utils import openai_client, llm_metadata_extracted, generate_response
from config import settings
from utils import (
    create_qdrant_client,
    search_in_qdrant,
    process_qdrant_conversation,
    get_logger,
)

logger = get_logger()


def run_bot(text: str) -> str:
    """
    Orchestrates the end-to-end pipeline of the Slack bot by extracting metadata,
    searching Qdrant, processing the results, and generating a response using an LLM.

    Args:
        text (str): The user input query (e.g., a request to summarize a meeting or ask a question).

    Returns:
        str: The LLM-generated response to the user input.
    """
    try:
        # Step 1: Use LLM to extract structured metadata (e.g., meeting title, speaker name, etc.)
        metadata_payload = llm_metadata_extracted(
            user_input=text, client=openai_client, model_name=settings.LLM_MODEL_NAME
        )

        # Step 2: Establish a connection to the Qdrant vector store
        qdrant_connection = create_qdrant_client()

        # Step 3: Query Qdrant with the input text and optional metadata filters
        qdrant_results = search_in_qdrant(
            qdrant_client=qdrant_connection,
            input_question=text,
            metadata_filters=metadata_payload.metadata_values,
            is_summary=metadata_payload.is_summary_request,
        )

        # Step 4: Format Qdrant results into a conversation context for the LLM
        conversation = process_qdrant_conversation(qdrant_results)

        # Step 5: Generate the LLM response based on the user input and context
        bot_reply = generate_response(
            user_input=text,
            conversation=conversation,
            client=openai_client,
            model_name=settings.LLM_MODEL_NAME,
        )

        return bot_reply.response

    except Exception as e:
        logger.error(f"Error running Slack bot pipeline: {e}")


if __name__ == "__main__":
    # Example usage for local testing
    text = "Summarize the meeting Product Development Update"
    response = run_bot(text)
    logger.info(response)

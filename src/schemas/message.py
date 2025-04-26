from typing import Literal
from typing import List, Optional, Dict
from pydantic import BaseModel, Field


class UserRequestMetadata(BaseModel):
    metadata: Optional[
        List[Literal["date", "meeting_title", "speaker_name", "position"]]
    ] = Field(
        default_factory=list,  # Ensure this is always a list, even if empty
        description="List of metadata explicitly provided by the user.",
    )

    metadata_values: Optional[Dict[str, List[str]]] = Field(
        default_factory=dict,  # Ensure this is always a dict, even if empty
        description="A dictionary mapping metadata field names to their extracted values (list of strings).",
    )

    description: str = Field(
        description="A structured description of the user's request after cleaning and extraction."
    )

    is_summary_request: bool = Field(
        description="Indicates whether the user is requesting a summarization of the meeting."
    )


class QueryResponse(BaseModel):
    response: str = Field(
        description="The answer or response text based on the conversation history"
    )
    confidence_score: float = Field(
        description="The confidence score of the response, ranging from 0 to 1"
    )

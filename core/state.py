from typing import TypedDict, List, Optional
from pydantic import BaseModel, Field

class ExtractionResult(BaseModel):
    perfume_name: Optional[str] = Field(description="Name of the perfume mentioned")
    preferences: Optional[str] = Field(description="Scent profile or budget preferences")
    intent: str = Field(description="Either 'search' for products or 'general' for greeting/small talk")

class SalesState(TypedDict):
    customer_query: str
    perfume_name: Optional[str]
    preferences: Optional[str]
    retrieved_context: str
    recommendation: str
    comparison: str
    pricing: str
    final_response: str # The combined final message
    memory: str
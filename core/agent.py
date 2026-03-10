from langgraph.graph import StateGraph, END
from core.state import SalesState
from core.nodes import (
    extract_preferences,
    retrieve_knowledge,
    recommend_perfume,
    pricing_and_comparison
)

workflow = StateGraph(SalesState)

workflow.add_node("extract", extract_preferences)
workflow.add_node("retrieve", retrieve_knowledge)
workflow.add_node("recommend", recommend_perfume)
workflow.add_node("finalize", pricing_and_comparison)

workflow.set_entry_point("extract")

# Conditional Logic: Should we search or just talk?
def route_after_extraction(state: SalesState):
    if state.get("intent") == "general":
        return "recommend" # Skip retrieval
    return "retrieve"

workflow.add_conditional_edges(
    "extract",
    route_after_extraction,
    {
        "recommend": "recommend",
        "retrieve": "retrieve"
    }
)

workflow.add_edge("retrieve", "recommend")
workflow.add_edge("recommend", "finalize")
workflow.add_edge("finalize", END)

sales_agent = workflow.compile()
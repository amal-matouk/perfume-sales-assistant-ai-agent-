from langchain_openai import ChatOpenAI
from core.vectorstore import vectorstore
from core.state import SalesState, ExtractionResult

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


def extract_preferences(state: SalesState):
    structured_llm = llm.with_structured_output(ExtractionResult)

    prompt = f"Analyze the user query and extract details:\n\n{state['customer_query']}"
    result = structured_llm.invoke(prompt)

    # Convert the Pydantic object to a dict to stop the serialization warning
    return {
        "perfume_name": result.perfume_name,
        "preferences": result.preferences,
        "intent": result.intent
    }

def retrieve_knowledge(state: SalesState):
    # Fallback search query
    search_term = f"{state.get('perfume_name', '')} {state.get('preferences', '')}".strip()

    if not search_term:
        return {"retrieved_context": "No specific perfume requested."}

    docs = vectorstore.similarity_search(search_term, k=2)
    context = "\n".join(doc.page_content for doc in docs)
    return {"retrieved_context": context}


def recommend_perfume(state: SalesState):

    prompt = f"""
    You are a luxury perfume expert. 
    Context: {state['retrieved_context']}
    History: {state['memory']}

    If the user just said hello, greet them warmly. 
    If they asked for a perfume, provide a detailed recommendation based ONLY on context.
    """
    response = llm.invoke(prompt)
    return {"recommendation": response.content}


def pricing_and_comparison(state: SalesState):
    """Combines pricing and comparison into one call to save tokens/time."""
    if not state.get("perfume_name"):
        return {"final_response": state["recommendation"]}

    prompt = f"""
    Based on this context: {state['retrieved_context']}
    1. Provide pricing for {state['perfume_name']}.
    2. Compare it briefly to one alternative in the context.

    Combine this with the previous recommendation: {state['recommendation']}
    """
    response = llm.invoke(prompt)
    return {"final_response": response.content}
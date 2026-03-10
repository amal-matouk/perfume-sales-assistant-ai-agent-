from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from core.memory import load_memory, save_chat
from core.agent import sales_agent
import uvicorn
app = FastAPI(title="Perfume Sales Assistant API")

# Define what the incoming request should look like
class ChatRequest(BaseModel):
    phone_number: str
    message: str

# Define the response structure
class ChatResponse(BaseModel):
    reply: str

@app.get("/")
async def health_check():
    return {"status": "online", "agent": "Perfume Assistant"}

@app.post("/chat", response_model=ChatResponse)
async def handle_chat(request: ChatRequest):
    try:
        # 1. Load context/memory
        memory = load_memory(request.phone_number)

        # 2. Run the LangGraph Agent
        result = sales_agent.invoke({
            "customer_query": request.message,
            "memory": memory
        })

        # 3. Extract the final response we built in the 'finalize' node
        reply = result.get("final_response") or result.get("recommendation")

        if not reply:
            raise HTTPException(status_code=500, detail="Agent failed to generate a response.")

        # 4. Save to DB
        save_chat(request.phone_number, request.message, reply)

        return ChatResponse(reply=reply)

    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":

    # Run the server on port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)
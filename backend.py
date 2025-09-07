# steup pydantic model (schema validation)
from pydantic import BaseModel
from typing import List
import os
import platform


class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool


#  setup ai agent from frontend
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agent import ai_agent

allowed_models = [
    "llama3-70b-8192",
    "mixtral-8x7b-32768",
    "llama-3.3-70b-versatile",
    "gpt-4o",
    "gpt-4o-mini",
]

app = FastAPI(title="Langgraph AI agent")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],  # Allow all origins for now - fix this later with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    return {
        "message": "Server is running",
        "port": os.getenv("PORT", "6969"),  # uvicorn default
        "environment": os.getenv("ENV", "development"),
        "python_version": platform.python_version(),
        "platform": platform.system(),
        "process_id": os.getpid(),
    }


@app.post("/chat")
def chat_endpoint(request: RequestState):
    """API Endpoint to interact with trhe chatbot using langgraph and search tools.
    It dynamically sleects the model specified in the request

    Args:
        request (RequestState): pydantic model
    """
    if request.model_name not in allowed_models:
        return {"error": "Invalid model name. Kndley sleect a valid ai model"}
    llm_id = request.model_name
    provider = request.model_provider
    system_prompt = request.system_prompt
    query = request.messages
    allow_search = request.allow_search

    # create ai agent and get response
    response = ai_agent(llm_id, provider, system_prompt, query, allow_search)
    return response


#  run app and explore swagger ui docs
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("backend:app", host="127.0.0.1", port=6969, reload=True)

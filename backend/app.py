"""
app.py
FastAPI backend for AI Workspace Assistant.
Exposes a single POST /chat endpoint.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from query_engine import detect_intent, filter_tasks, format_tasks_for_llm
from chatbot import generate_response

# Initialize FastAPI app
app = FastAPI(
    title="AI Workspace Assistant",
    description="A chatbot that answers queries about your workspace tasks.",
    version="1.0.0",
)

# Allow requests from the React frontend (running on localhost:5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request/Response models
class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


@app.get("/")
def root():
    """Health check endpoint."""
    return {"status": "AI Workspace Assistant is running!"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    """
    Main chat endpoint.
    1. Detect user intent
    2. Filter tasks using Pandas
    3. Send to Ollama LLM
    4. Return formatted response
    """
    user_message = request.message.strip()

    if not user_message:
        raise HTTPException(status_code=400, detail="Message cannot be empty.")

    # Step 1: Detect intent from user message
    intent = detect_intent(user_message)

    # Step 2: Filter task data using Pandas
    filtered_df = filter_tasks(intent)

    # Step 3: Format task data as text for the LLM
    task_text = format_tasks_for_llm(filtered_df)

    # Step 4: Generate LLM response
    reply = generate_response(user_message, task_text)

    return ChatResponse(reply=reply)

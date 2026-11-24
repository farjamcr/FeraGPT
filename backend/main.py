
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from google import genai

app = FastAPI(
    title="FeraGPT",
    description="Your Personal AI Assistant",
    version="0.4.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=10000)

@app.get("/")
def home():
    return {
        "name": "FeraGPT",
        "status": "online",
        "version": "0.4.0"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/chat")
def chat(request: ChatRequest):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise HTTPException(
            status_code=503,
            detail="AI is not configured yet."
        )

    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=request.message
        )

        return {"reply": response.text}

    except Exception:
        raise HTTPException(
            status_code=502,
            detail="AI service is temporarily unavailable."
        )
        

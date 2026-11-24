from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(
    title="FeraGPT",
    description="Your Personal AI Assistant and Software Engineer",
    version="0.2.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

SYSTEM_PROMPT = """
You are FeraGPT, an intelligent AI assistant.

Your specialties include:
- Python and JavaScript programming
- Website development
- Backend and frontend engineering
- FiveM and SAMP server development
- Debugging and code analysis

You are also a general-purpose assistant.
Answer clearly, accurately, and helpfully.
"""

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {
        "name": "FeraGPT",
        "status": "online",
        "version": "0.2.0",
        "description": "Personal AI Assistant"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/chat")
def chat_info():
    return {
        "message": "Use POST /chat to talk with FeraGPT"
    }

@app.post("/chat")
def chat(request: ChatRequest):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return {
            "error": "AI API key is not configured yet."
        }

    try:
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": request.message}
            ]
        )

        return {
            "name": "FeraGPT",
            "response": response.choices[0].message.content
        }

    except Exception as e:
        return {"error": str(e)}
        

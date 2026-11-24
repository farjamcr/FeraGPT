
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="FeraGPT",
    description="Your Personal AI Engineer",
    version="0.3.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {
        "name": "FeraGPT",
        "status": "online",
        "version": "0.3.0"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "reply": "پیامت به سرور FeraGPT رسید! اتصال بک‌اند برقرار است. ✨"
           }
    

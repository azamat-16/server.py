from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "AI Friend server is running 🚀"}

@app.post("/chat")
def chat(message: dict):
    user_message = message.get("message", "")
    return {
        "reply": f"🤖 Я AI Friend. Ты написал: {user_message}"
    }

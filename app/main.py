from fastapi import FastAPI
from app.models.event import Event

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/events")
async def get_events():
    return {"message": "Events endpoint working"}

@app.post("/signal")
def send_signal(payload: dict):
    return {
        "message": "signal received",
        "data": payload
    }

@app.post("/events/test")
async def test_event():
    return {
        "event": "AI Hackathon",
        "city": "London",
        "matched": True
    }

@app.post("/events")
async def create_event(event: Event):
    return {"Received": event.model_dump()}
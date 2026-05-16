from fastapi import FastAPI
from app.models.event import Event
from app.engine.matcher import match_event
from app.pipeline.event_pipeline import process_event
from app.services.services import get_user_preferences

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

@app.get("/events/test")
async def test_event():
    return {
        "event": "AI Hackathon",
        "city": "London",
        "matched": True
    }

@app.post("/events")
async def create_event(event: Event):

    user_preferences = ["AI", "Cybersecurity", "Tech"]

    matched = match_event(event, user_preferences)

    return {
        "Received": event.model_dump(),
        "matched": matched
        
    }


@app.post("/events/{user_id}")
async def create_event(user_id: str, event: Event):
    preferences = get_user_preferences(user_id)

    result = process_event(event, preferences)

    return result
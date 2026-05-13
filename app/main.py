from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/signal")
def send_signal(payload: dict):
    return {
        "message": "signal received",
        "data": payload
    }
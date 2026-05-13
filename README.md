# Signal App Backend

A FastAPI-based backend for an event-driven signal system. It processes incoming triggers and delivers real-time notifications via external services such as SMS, scheduled jobs, and APIs.

The system is designed to be lightweight, extensible, and easy to integrate with third-party services like Firebase, Twilio, and background schedulers.

## Features

- FastAPI-based REST backend
- Event-driven signal processing
- Background scheduling support with APScheduler
- Firebase integration ready (Firestore / Admin SDK)
- SMS notifications via Twilio (optional integration)
- Environment-based configuration with `.env` support
- Modular structure for easy extension

## System Architecture

At a high level, the system follows an event → processing → action pipeline:

- Client / External API
  - FastAPI Server
    - `/signal` endpoint (event intake)
    - Business Logic Layer
      - Scheduler (APScheduler)
      - Firebase (state / storage)
      - External APIs (Twilio, etc.)
    - Notification / Action Layer
      - SMS (Twilio)
      - Database writes (Firestore)
      - Logs / events

### Key Idea

A signal is any incoming event that triggers downstream actions such as notifications, storage updates, or scheduled workflows.

## Project Structure

```
hackathon-signal-app/
│
├── app/
│   ├── main.py            # FastAPI entry point
│   ├── routes/            # API endpoints (optional expansion)
│   ├── services/          # Business logic (signals, notifications)
│   ├── integrations/      # Firebase, Twilio, etc.
│   └── core/              # Config, settings, utils
│
├── requirements.txt
├── .env.example
├── README.md
└── venv/ (ignored)
```

## Getting Started

1. Clone the repository

```bash
git clone https://github.com/your-username/hackathon-signal-app.git
cd hackathon-signal-app
```

2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

- Git Bash / Linux / macOS:

```bash
source venv/Scripts/activate
```

- Windows (PowerShell):

```powershell
venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Set environment variables

Create a `.env` file from the example:

```bash
cp .env.example .env
```

Example environment variables:

```env
FIREBASE_PROJECT_ID=your_project_id
TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_token
```

5. Run the server

```bash
uvicorn app.main:app --reload
```

Server will be available at:

- http://127.0.0.1:8000
- API docs: http://127.0.0.1:8000/docs

## API Endpoints

### Health Check

- `GET /health`

Example response:

```json
{
  "status": "ok"
}
```

### Send Signal

- `POST /signal`

Example request:

```json
{
  "type": "test",
  "message": "hello signal"
}
```

Example response:

```json
{
  "message": "signal received",
  "data": {
    "type": "test",
    "message": "hello signal"
  }
}
```

## Planned Integrations

- Firebase Firestore (event persistence)
- Twilio SMS notifications
- Email notifications
- Cron-based scheduled signals
- External webhook triggers

## Design Principles

- Minimal core, extensible architecture
- Event-driven design
- Separation of concerns (routes / services / integrations)
- Easy local development
- Cloud-ready structure

## Tech Stack

- FastAPI
- Uvicorn
- Pydantic
- Firebase Admin SDK
- APScheduler
- Twilio
- Python-dotenv

## Future Improvements

- Auth system (JWT / Firebase Auth)
- Multi-user signal routing
- Dashboard UI
- Queue system (Redis / Celery)
- WebSocket real-time signals

## Development Notes

This project is structured for rapid iteration. Start by implementing a single end-to-end signal flow before scaling integrations.

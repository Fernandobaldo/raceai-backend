# 🏎️ RaceAI Backend (English)

This is the backend API for RaceAI, built with FastAPI.

## 📦 Features

- Accepts lap data via CSV (X, Y, Speed)
- Analyzes performance per point
- Returns JSON with tips and average speed

## 🚀 Running locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

## 📤 Endpoints

### `POST /analyze`
- Accepts CSV file
- Returns performance analysis

## 🌐 Deployment (Render)

Use the following setup:
- Python service
- Port: `10000`
- Start command: `bash start.sh`

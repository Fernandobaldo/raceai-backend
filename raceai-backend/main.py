from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import shutil
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)
    return {"filename": file.filename, "message": "File uploaded successfully."}

@app.post("/analyze")
async def analyze_csv(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    analysis = []
    avg_speed = df["Velocidade"].mean()

    for i, row in df.iterrows():
        tip = "Stable speed — regular section."
        if row["Velocidade"] < avg_speed * 0.8:
            tip = "Low speed — possible early braking."
        elif row["Velocidade"] > avg_speed * 1.1:
            tip = "High speed — watch out for traction loss."
        analysis.append({
            "point": i + 1,
            "X": row["X"],
            "Y": row["Y"],
            "Speed": row["Velocidade"],
            "tip": tip
        })

    return {"average_speed": avg_speed, "analysis": analysis}

@app.get("/")
def home():
    return {"message": "🚗 RaceAI Backend Online"}

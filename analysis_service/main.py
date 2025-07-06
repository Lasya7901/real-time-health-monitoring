from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class Vitals(BaseModel):
    patient_id: str
    heart_rate: int
    spo2: int
    timestamp: str

@app.post("/analyze")
def analyze(vitals: Vitals):
    alert = ""
    if vitals.heart_rate > 140:
        alert += "High heart rate. "
    if vitals.spo2 < 90:
        alert += "Low oxygen level."

    if alert:
        requests.post("http://localhost:8003/notify", json={
            "patient_id": vitals.patient_id,
            "alert": alert,
            "timestamp": vitals.timestamp
        })

    requests.post("http://localhost:8005/store", json=vitals.dict())
    return {"status": "analyzed"}

from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class Vitals(BaseModel):
    patient_id: str
    heart_rate: int
    spo2: int
    timestamp: str

@app.post("/preprocess")
def preprocess_data(vitals: Vitals):
    if 30 <= vitals.heart_rate <= 200 and 70 <= vitals.spo2 <= 100:
        requests.post("http://localhost:8002/analyze", json=vitals.dict())
    return {"status": "received"}

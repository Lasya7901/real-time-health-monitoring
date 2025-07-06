from fastapi import FastAPI
from pydantic import BaseModel
import requests
import random
import time
import threading

app = FastAPI()

class Vitals(BaseModel):
    patient_id: str
    heart_rate: int
    spo2: int
    timestamp: str

def simulate_sensor():
    while True:
        data = {
            "patient_id": "P123",
            "heart_rate": random.randint(60, 180),
            "spo2": random.randint(85, 100),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        requests.post("http://localhost:8001/preprocess", json=data)
        time.sleep(5)

@app.on_event("startup")
def start_simulation():
    threading.Thread(target=simulate_sensor).start()

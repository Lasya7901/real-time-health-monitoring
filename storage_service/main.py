from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()
conn = sqlite3.connect("health.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS vitals
              (patient_id TEXT, heart_rate INTEGER, spo2 INTEGER, timestamp TEXT)''')
conn.commit()

class Vitals(BaseModel):
    patient_id: str
    heart_rate: int
    spo2: int
    timestamp: str

@app.post("/store")
def store_data(vitals: Vitals):
    cursor.execute("INSERT INTO vitals VALUES (?, ?, ?, ?)",
                   (vitals.patient_id, vitals.heart_rate, vitals.spo2, vitals.timestamp))
    conn.commit()
    return {"status": "stored"}

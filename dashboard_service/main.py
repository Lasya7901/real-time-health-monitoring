from fastapi import FastAPI
import sqlite3

app = FastAPI()
conn = sqlite3.connect("health.db", check_same_thread=False)
cursor = conn.cursor()

@app.get("/dashboard/{patient_id}")
def get_latest_vitals(patient_id: str):
    cursor.execute("SELECT * FROM vitals WHERE patient_id = ? ORDER BY timestamp DESC LIMIT 5", (patient_id,))
    rows = cursor.fetchall()
    return {"vitals": rows}

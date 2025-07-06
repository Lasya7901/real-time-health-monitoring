from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Alert(BaseModel):
    patient_id: str
    alert: str
    timestamp: str

@app.post("/notify")
def send_notification(alert: Alert):
    print(f"[ALERT] {alert.patient_id} - {alert.alert} @ {alert.timestamp}")
    return {"status": "alert sent"}

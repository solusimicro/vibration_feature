# Entry FastAPI application
"""app/main.py"""

from fastapi import FastAPI
from app.api.routes import router
from app.services.sensor_reader import start_sensor_reader
import threading

app = FastAPI(title="Vibration Edge")

@app.on_event("startup")
def startup():
    t = threading.Thread(target=start_sensor_reader, daemon=True)
    t.start()

app.include_router(router)


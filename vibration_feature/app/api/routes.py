# Endpoint SCADA data service
# This service handles the endpoints for SCADA data retrieval and processing.
"""app/api/routes.py"""

from fastapi import APIRouter
from app.services.sensor_reader import LATEST_WINDOW
from app.services import (
    feature_engine,
    iso20816,
    health,
    fault_logic
)

router = APIRouter()

@router.get("/vibration")
def read_vibration():
    data = LATEST_WINDOW

    signal = data["signal"]
    rpm = data["rpm"]
    fs = data["sampling_rate"]

    features = feature_engine.extract(signal, rpm, fs)
    features["iso_zone"] = iso20816.get_zone(
        features["overall_vel_rms_mm_s"]
    )

    hi = health.compute(features)
    fault = fault_logic.evaluate(features, hi)

    return {
        "sensor": data["sensor_id"],
        "health_index": round(hi, 2),
        "fault": fault,
        "rms_g": features["overall_acc_rms_g"],
        "vel_mm_s": features["overall_vel_rms_mm_s"],
        "iso_zone": features["iso_zone"]
    }


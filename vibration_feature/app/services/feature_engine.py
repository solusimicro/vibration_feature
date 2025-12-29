# Orchestrator for feature engineering tasks
# This service coordinates the computation of various vibration features by utilizing specialized services.
"""app/services/feature_engine.py"""

import numpy as np
from scipy.fft import rfft, rfftfreq

from app.services.window_manager import update_buffer
from app.services.overall import overall_features
from app.services.bands import band_features
from app.services.harmonics import harmonic_features
from app.services.health import health_index
from app.services.fault_logic import detect_fault
from app.services.velocity import acc_to_velocity_rms
from app.services.iso20816 import iso_zone


def process_vibration(req):
    # === 1. BUFFER RAW SIGNAL ===
    window = update_buffer(req.sensor_id, req.signal)

    if window is None:
        return {"status": "BUFFERING"}

    # === 2. PREPARE DATA ===
    x = np.asarray(window, dtype=float)
    fs = req.sampling_rate
    rpm = req.rpm

    # === 3. FEATURE EXTRACTION ===
    features = {}

    # 3.1 Overall acceleration features
    features.update(overall_features(x))

    # 3.2 Band RMS (LF / MF / HF)
    features.update(band_features(x, fs))

    # 3.3 FFT & harmonics
    fft = np.abs(rfft(x))
    freq = rfftfreq(len(x), d=1.0 / fs)
    features.update(harmonic_features(freq, fft, rpm))

    # 3.4 ISO 20816 – Velocity RMS
    vel_rms = acc_to_velocity_rms(x, fs)
    features["overall_vel_rms_mm_s"] = vel_rms
    features["iso_zone"] = iso_zone(vel_rms)

    # === 4. RESULT ===
    return {
        "sensor": req.sensor_id,
        "health_index": health_index(features),
        "fault": detect_fault(features),
        "features": features
    }
# Feature engineering service
# This service orchestrates the computation of various vibration features by leveraging specialized services.
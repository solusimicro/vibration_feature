# 1x / 2x / 3x RPM Harmonics Service
# This service computes the harmonic components at 1x, 2x, and 3x the rotational speed (RPM) of machinery from vibration data.
"""app/services/harmonics.py"""

from app.utils.signal_utils import harmonic_peak

def harmonic_features(freq, fft, rpm):
    if not rpm:
        return {}
    f1 = rpm / 60
    return {
        "peak_1x_g": harmonic_peak(freq, fft, f1),
        "peak_2x_g": harmonic_peak(freq, fft, 2*f1),
        "peak_3x_g": harmonic_peak(freq, fft, 3*f1)
    }

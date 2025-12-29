# FFT, RMS helpers and other signal processing utilities
"""app/utils/signal_utils.py"""

import numpy as np
from scipy.signal import butter, filtfilt
from scipy.stats import kurtosis


def rms(x: np.ndarray) -> float:
    return float(np.sqrt(np.mean(np.square(x))))


def band_rms(signal: np.ndarray, fs: int, f_low: float, f_high: float) -> float:
    signal = np.asarray(signal)

    if len(signal) < fs * 0.2:
        return rms(signal)

    nyq = fs / 2
    low = f_low / nyq
    high = min(f_high / nyq, 0.99)

    b, a = butter(4, [low, high], btype="band")
    filtered = filtfilt(b, a, signal)

    return rms(filtered)


def harmonic_peak(freq, fft_mag, target_freq, tol=0.05) -> float:
    if target_freq <= 0:
        return 0.0

    band = (freq > target_freq * (1 - tol)) & (freq < target_freq * (1 + tol))
    if not band.any():
        return 0.0

    return float(np.max(fft_mag[band]))


def overall_features(signal: np.ndarray) -> dict:
    signal = np.asarray(signal)

    return {
        "overall_acc_rms_g": rms(signal),
        "overall_acc_peak_g": float(np.max(np.abs(signal))),
        "kurtosis": float(kurtosis(signal))
    }

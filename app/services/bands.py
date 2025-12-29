# LF / MF / HF RMS Bands Service 
# This service computes the RMS (Root Mean Square) values for low frequency (LF), mid frequency (MF), and high frequency (HF) bands of vibration data.
"""app/services/bands.py"""

from app.utils.signal_utils import band_rms

def band_features(x, fs):
    return {
        "acc_lf_rms_g": band_rms(x, fs, 10, 100),
        "acc_mf_rms_g": band_rms(x, fs, 100, 1000),
        "acc_hf_rms_g": band_rms(x, fs, 1000, fs/2)
    }

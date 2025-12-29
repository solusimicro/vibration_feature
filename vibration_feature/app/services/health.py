# Health index service
# This service computes a health index for machinery based on vibration data and various computed features.
"""app/services/health.py"""

def health_index(f):
    score = 0.0

    score += min(f["overall_acc_rms_g"] / 0.3, 1.0) * 0.4
    score += min(f["kurtosis"] / 6.0, 1.0) * 0.3
    score += min(f.get("acc_hf_rms_g", 0.0) / 0.2, 1.0) * 0.3

    hi = 1.0 - score

    # ⬇️ WAJIB
    hi = max(0.0, min(hi, 1.0))

    return round(hi, 3)


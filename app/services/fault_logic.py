# Fault matrix logic service
# This service handles the logic for determining fault conditions based on vibration data and computed features.
"""app/services/fault_logic.py"""

def detect_fault(f):
    if f.get("acc_hf_rms_g", 0) > 0.2 and f["kurtosis"] > 5:
        return "BEARING_FAULT"
    if f.get("peak_2x_g", 0) > f.get("peak_1x_g", 1):
        return "MISALIGNMENT"
    if f.get("peak_1x_g", 0) > 0.5:
        return "UNBALANCE"
    return "NORMAL"

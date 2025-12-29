# Overall metrics computation service
# This service computes overall metrics for machinery health by aggregating various vibration features and analyses.
"""app/services/overall.py"""

import numpy as np
from scipy.stats import kurtosis

def overall_features(x):
    rms = np.sqrt(np.mean(x**2))
    return {
        "overall_acc_rms_g": rms,
        "overall_acc_peak_g": float(np.max(np.abs(x))),
        "kurtosis": float(kurtosis(x, fisher=False))
    }

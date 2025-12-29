import numpy as np
from scipy.signal import butter, filtfilt

def bandpass(x, fs, f1=10, f2=1000, order=4):
    nyq = fs / 2
    b, a = butter(order, [f1/nyq, f2/nyq], btype='band')
    return filtfilt(b, a, x)

def acc_to_velocity_rms(acc_g, fs):
    # g → m/s²
    acc = acc_g * 9.81

    # ISO band
    acc_f = bandpass(acc, fs)

    # Integrate
    vel = np.cumsum(acc_f) / fs

    # m/s → mm/s
    vel_mm = vel * 1000

    return float(np.sqrt(np.mean(vel_mm**2)))

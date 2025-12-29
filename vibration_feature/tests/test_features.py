import numpy as np

from app.services.feature_engine import extract_vibration_features


def generate_signal(fs=2560, rpm=1500, n=4096):
    f1x = rpm / 60.0
    t = np.arange(n) / fs

    signal = (
        0.02 * np.sin(2 * np.pi * f1x * t) +
        0.005 * np.sin(2 * np.pi * 2 * f1x * t) +
        0.002 * np.sin(2 * np.pi * 3 * f1x * t) +
        0.003 * np.random.randn(n)
    )
    return signal.tolist()


def test_extract_vibration_features():
    fs = 2560
    rpm = 1500
    acc = generate_signal(fs, rpm)

    features = extract_vibration_features(acc, fs, rpm)

    # === BASIC ASSERT ===
    assert isinstance(features, dict)

    # === KEY FEATURES EXIST ===
    expected_keys = [
        "overall_acc_rms_g",
        "overall_acc_peak_g",
        "kurtosis",
        "acc_lf_rms_g",
        "acc_mf_rms_g",
        "acc_hf_rms_g",
        "peak_1x_g",
        "peak_2x_g",
        "peak_3x_g",
    ]

    for key in expected_keys:
        assert key in features

    # === LOGICAL CHECKS (ENGINEERING SENSE) ===
    assert features["overall_acc_rms_g"] > 0
    assert features["overall_acc_peak_g"] > features["overall_acc_rms_g"]
    assert features["peak_1x_g"] > features["peak_2x_g"]
    assert features["peak_2x_g"] > features["peak_3x_g"]


def iso_zone(vel_rms):
    if vel_rms < 1.8:
        return "A"   # Good
    elif vel_rms < 4.5:
        return "B"   # Acceptable
    elif vel_rms < 7.1:
        return "C"   # Unsatisfactory
    else:
        return "D"   # Unacceptable
# ISO 20816 service
# This service computes ISO 20816 vibration zones based on velocity RMS values.
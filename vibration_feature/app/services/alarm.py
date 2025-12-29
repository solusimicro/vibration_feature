# Alarm service
# This service computes alarm-related features for vibration data, including peak values in specified frequency bands.
"""app/services/alarm.py"""

def alarm_level(health):
    if health >= 0.9:
        return "NORMAL"
    if health >= 0.7:
        return "WARNING"
    if health >= 0.5:
        return "ALARM"
    return "TRIP"

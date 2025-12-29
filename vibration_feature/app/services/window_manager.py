# Buffer & windowing service
# This service manages data buffering and windowing operations for vibration data processing.
"""app/services/window_manager.py"""

WINDOW_SIZE = 128
_buffers = {}

def update_buffer(sensor_id, data):
    buf = _buffers.get(sensor_id, [])
    buf.extend(data)
    if len(buf) >= WINDOW_SIZE:
        window = buf[:WINDOW_SIZE]
        _buffers[sensor_id] = buf[WINDOW_SIZE:]
        return window
    _buffers[sensor_id] = buf
    return None

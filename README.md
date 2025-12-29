# Vibration Edge Feature Engine

Edge-level vibration feature extraction using FastAPI.

## Features
- Acceleration RMS & Peak
- Band RMS (LF / MF / HF)
- Kurtosis (ISO-style)
- Harmonic peaks (1x / 2x / 3x)
- Velocity RMS (ISO 20816)
- Health Index
- Fault Logic

## API Endpoint
`POST /vibration/process`

### Example Payload
```json
{
  "sensor_id": "PUMP_01_DE",
  "sampling_rate": 25600,
  "rpm": 1480,
  "signal": [0.001, -0.002, 0.003]
}

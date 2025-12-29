# Request / response models for schema definitions
"""app/models/schema.py"""

from pydantic import BaseModel
from typing import List

class VibRequest(BaseModel):
    sensor_id: str
    sampling_rate: int
    rpm: float
    signal: List[float]


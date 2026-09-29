from pydantic import BaseModel


class PredictionRequest(BaseModel):
    """One trial's first-3-day base aggregates, as the caller knows them."""
    # with a type for each. They are the same seven base aggregates your
    # feature code starts from; features.py names them.
    sessions_day1: int
    sessions_day2: int
    sessions_day3: int
    listen_sessions_3d: int
    total_minutes_3d: int
    country: str
    device_type: str

class PredictionResponse(BaseModel):
    """What we send back: a probability and a band a human can act on."""
    # probability, and the low/medium/high band it falls in.
    conversion_probability: float
    conversion_band: str

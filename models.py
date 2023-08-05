from pydantic import BaseModel

class Light(BaseModel):
    id: int
    on: bool = None
    bri: int = None
    hue: int = None
    sat: int = None
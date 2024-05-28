from pydantic import BaseModel


class AutoAddRequest(BaseModel):
    brand: str
    model: str
    enigine: str
    release_year: str
    color: str
    body: str
    complectation: str
    transmission: str
    drive: str
    wheel: str
    vin_number: str

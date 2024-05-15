from pydantic import BaseModel, Field


class UserAddRequest(BaseModel):
    username: str
    name: str
    phone_number: str
    email: str
    password: str
    

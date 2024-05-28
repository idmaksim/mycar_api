import datetime
from pydantic import BaseModel, Field


class DocumentAddRequest(BaseModel):
    name: str
    birth_date: datetime.date = Field(default=datetime.date.today())
    date_of_issue: datetime.date = Field(default=datetime.date.today())
    end_date: datetime.date = Field(default=datetime.date.today())
    issued_by: str = Field(default="")
    number: str = Field(default="")
    where_issued: str = Field(default="")
    categories: str = Field(default="")
    user_id: int    

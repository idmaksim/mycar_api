import datetime
from pydantic import BaseModel, Field


class DocumentAddRequest(BaseModel):
    name: str
    birth_date: datetime.date
    date_of_issue: datetime.date
    end_date: datetime.date
    issued_by: str 
    number: str
    where_issued: str
    categories: str 
    user_id: int    

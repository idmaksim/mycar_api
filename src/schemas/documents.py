import datetime
from pydantic import BaseModel


class DocumentAddRequest(BaseModel):
    name: str
    birth_date: datetime.date | str = ""
    date_of_issue: datetime.date | str = ""
    end_date: datetime.date | str = ""
    issued_by: str = ""
    number: str = ""
    where_issued: str = ""
    categories: str = ""
    user_id: int    

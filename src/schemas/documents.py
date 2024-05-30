from pydantic import BaseModel, Field


class DocumentAddRequest(BaseModel):
    name: str
    birth_date: str = Field(default="")
    date_of_issue: str = Field(default="")
    end_date: str = Field(default="")
    issued_by: str = Field(default="")
    number: str = Field(default="")
    where_issued: str = Field(default="")
    categories: str = Field(default="")
    user_id: int    

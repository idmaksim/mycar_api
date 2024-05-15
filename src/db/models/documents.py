import datetime
from sqlalchemy import Column, Integer, String, Date

from ..db import Base


class Documents(Base):
    __tablename__ = 'documents'

    id: int = Column(Integer, unique=True, primary_key=True, autoincrement=True, nullable=False)
    name: str = Column(String, nullable=False)
    birth_date: datetime.date = Column(Date, nullable=False)
    date_of_issue: datetime.date = Column(Date, nullable=False)
    end_date: datetime.date = Column(Date, nullable=False)
    issued_by: str = Column(String, nullable=False) 
    number: str = Column(String, nullable=False, unique=True)
    where_issued: str = Column(String, nullable=False)
    categories: str = Column(String, nullable=False)

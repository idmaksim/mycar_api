from sqlalchemy import Column, ForeignKey, Integer, String

from db.db import Base


class Documents(Base):
    __tablename__ = 'documents'

    name: str = Column(String, nullable=False)
    birth_date: str = Column(String, nullable=True)
    date_of_issue: str = Column(String, nullable=False)
    end_date: str = Column(String, nullable=True)
    issued_by: str = Column(String, nullable=True) 
    number: str = Column(String, nullable=True, unique=True)
    where_issued: str = Column(String, nullable=True)
    categories: str = Column(String, nullable=True)
    user_id: int = Column(Integer, ForeignKey('users.id'), nullable=False)

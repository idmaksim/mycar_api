from sqlalchemy import Column, String

from db.db import Base


class images(Base):
    __tablename__ = 'images'
    
    filename = Column(String, nullable=False, unique=True)
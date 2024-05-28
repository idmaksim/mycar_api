from sqlalchemy import Column, String
from db.db import Base


class Images(Base):
    __tablename__ = "images"

    filename: str = Column(String, unique=True, nullable=False)
from sqlalchemy import Column, String

from db.db import Base


class Images(Base):
    __tablename__ = 'images'

    filename = Column(String, nullable=False, unique=True)
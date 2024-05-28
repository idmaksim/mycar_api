from sqlalchemy import Column, String

from db.db import Base


class Users(Base):
    __tablename__ = 'users'

    username: str = Column(String, unique=True, nullable=False)
    name: str = Column(String, nullable=False)
    phone_number: str = Column(String, nullable=False)
    email: str = Column(String, unique=True, nullable=False)
    password: str = Column(String, nullable=False)

# class Images(Base):
#     __tablename__ = "images"

#     filename: str = Column(String, unique=True, nullable=False)
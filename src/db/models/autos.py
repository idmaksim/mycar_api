import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Date

from db.db import Base


class Autos(Base):
    __tablename__ = 'autos'

    brand: str = Column(String, nullable=False)
    model: str = Column(String, nullable=False)
    enigine: str = Column(String, nullable=False)
    release_year: str = Column(String, nullable=False)
    color: str = Column(String, nullable=False)
    body: str = Column(String, nullable=False)
    complectation: str = Column(String, nullable=False)
    transmission: str = Column(String, nullable=False)
    drive: str = Column(String, nullable=False)
    wheel: str = Column(String, nullable=False) 
    vin_number: str = Column(String, nullable=False) 
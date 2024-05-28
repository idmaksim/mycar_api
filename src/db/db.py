from sqlalchemy import Column, Integer
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from utils.config import DB_DRIVER, DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USERNAME


DATABASE_URL = f"{DB_DRIVER}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


class Base(DeclarativeBase):
    __table_args__ = {"extend_existing": True}

    id = Column(
        Integer, primary_key=True, unique=True, autoincrement=True, nullable=False
    )


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def create_db_and_tables():
    from db.models.images import Images
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
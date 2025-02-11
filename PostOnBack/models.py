from sqlalchemy import ForeignKey, Column, BigInteger, String, DateTime, Boolean, Integer
from typing import List
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship
from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs, async_sessionmaker
from datetime import datetime

engine = create_async_engine(
    "sqlite+aiosqlite:///./poston.db?charset=utf8",
    connect_args={"check_same_thread": False},
    echo=True
)
#engine = create_async_engine(url = 'sqlite+aiosqlite:///db.sqlite3', echo = True)

async_session = async_sessionmaker(engine, expire_on_commit = False)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    
    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)  # Drop existing tables
        await conn.run_sync(Base.metadata.create_all)
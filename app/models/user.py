from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from .base import Base, Column, Integer, Boolean, String, relationship
import uuid

from fastapi_users import schemas


class User(SQLAlchemyBaseUserTableUUID, Base):

    logs = relationship("Log", back_populates="owner")


class UserRead(schemas.BaseUser[uuid.UUID]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass

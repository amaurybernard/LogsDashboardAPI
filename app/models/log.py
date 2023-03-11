from enum import Enum
import uuid
from sqlalchemy.dialects.postgresql import UUID
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from .base import Base, Column, Integer, Boolean, String, relationship, ForeignKey


class Log(Base):
    __tablename__ = "logs"

    class SeverityLevels(Enum):
        DEBUG = 000
        INFO = 100
        WARN = 200
        ERROR = 300

    id = Column(Integer, primary_key=True, index=True)
    code = Column(Integer)
    message = Column(String)
    owner_id = Column(UUID, ForeignKey("user.id"), nullable=False)
    severity = Column(Integer, default=SeverityLevels.INFO)

    owner = relationship("User", back_populates="logs")

    def severity_level(self):
        return self.SEVERITY_LEVELS[self.severity]


PydanticLog = sqlalchemy_to_pydantic(Log)

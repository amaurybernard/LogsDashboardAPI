from .base import Base, Column, Integer, Boolean, String, relationship, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from enum import Enum
import uuid

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
    severity = Column(Integer, default=1)

    owner = relationship("User", back_populates="logs")

    def severity_level(self):
        return self.SEVERITY_LEVELS[self.severity]

from .base import Base, Column, Integer, Boolean, String, relationship, ForeignKey
from enum import Enum

class Log(Base):
    __tablename__ = "logs"

    SEVERITY_LEVELS = Enum('DEBUG', 'INFO', 'WARN', 'ERROR')

    id = Column(Integer, primary_key=True, index=True)
    code = Column(Integer)
    message = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    severity = Column(Integer, default=1)

    owner = relationship("User", back_populates="logs")

    def severity_level(self):
        return self.SEVERITY_LEVELS[self.severity]

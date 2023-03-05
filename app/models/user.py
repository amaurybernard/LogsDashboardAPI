from .base import Base, Column, Integer, Boolean, String, relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    logs = relationship("Log", back_populates="owner")

    @property
    def password(password: String):
        pass

    @password.setter
    def password(self, password: String):
        hash_password = password
        return None

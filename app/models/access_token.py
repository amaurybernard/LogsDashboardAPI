from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTableUUID,
)
from app.models.base import Base


class AccessToken(SQLAlchemyBaseAccessTokenTableUUID, Base):
    pass

from fastapi_users.authentication import AuthenticationBackend
from app.authentication.bearer_transport import bearer_transport
from app.authentication.strategy import get_database_strategy

auth_backend = AuthenticationBackend(
    name="db_bearer",
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)

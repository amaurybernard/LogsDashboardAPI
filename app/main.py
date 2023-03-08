from fastapi import FastAPI
from sqlalchemy import select
import uuid

from fastapi_users import FastAPIUsers

from app.models import User
from app.authentication.user_manager import get_user_manager
from app.authentication.backend import auth_backend


fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

app = FastAPI()
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="",
    tags=["auth"],
)

@app.get("/")
async def root():
    return {"message": "Welcome, please login"}

@app.post('/logs')
async def log():
    return {'message': 'Thanks for your logs'}
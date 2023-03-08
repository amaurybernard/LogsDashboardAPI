from fastapi import FastAPI, Depends
from sqlalchemy import select
import uuid

from fastapi_users import FastAPIUsers

from app.authentication.backend import auth_backend
from app.authentication.user_manager import get_user_manager, current_user
from app.models import User
from app.models.user import UserRead, UserUpdate


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

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

@app.get("/")
async def root():
    return {"message": "Welcome, please login"}

@app.post('/logs')
async def log(user: User = Depends(current_user)):
    return {'message': 'Thanks for your logs'}
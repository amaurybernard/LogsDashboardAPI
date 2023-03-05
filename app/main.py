from fastapi import FastAPI
from .models.user import Base, User
from .database import engine
from sqlalchemy import select


app = FastAPI()

Base.metadata.create_all(engine)

@app.get("/")
async def root():
    return {"message": "Welcome, please login"}

@app.post('/login')
async def login(email: str, password: str):
    user = select(User).where(User.email == email)
    if password == 'fine':
        return {"email": email}
    return {"message": "Failed"}

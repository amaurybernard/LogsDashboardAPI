from app.models import User
from app.database import engine
from sqlalchemy.orm import Session
import asyncio
from app.tasks.db.create_user import create_user


print('Seeds starting...')
asyncio.run(create_user("admin@admin.com", "superpass"))

print('Seeds done.')
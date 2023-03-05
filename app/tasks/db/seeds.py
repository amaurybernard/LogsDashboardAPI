from app.models import User
from app.database import engine
from sqlalchemy.orm import Session


print('Seeds starting...')

with Session(engine) as session:
    root = User(
        email='root@local',
        password='password'
    )

    session.add_all([root])
    session.commit()

print('Seeds done.')
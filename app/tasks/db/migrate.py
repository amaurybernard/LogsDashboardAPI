print('Migration imports')
from app.models import Base
from app.database import engine

print('Migration starting...')

Base.metadata.create_all(engine)

print('Migration done.')
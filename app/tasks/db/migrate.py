import sys
import asyncio

from app.models import Base
from app.database import engine


async def migrate(drop = False):
    async with engine.begin() as conn:
        if drop:
            print('Dropping data...')
            await conn.run_sync(Base.metadata.drop_all)
            print('Dropped.')
        await conn.run_sync(Base.metadata.create_all)


if __name__ == '__main__':
    print('Migration starting...')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(migrate(sys.argv.count('-rm') >= 1))
    print('Migration done.')


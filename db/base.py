from databases import Database
from sqlalchemy import create_engine, MetaData
from core.config import DATABASE_TYPE
from .local import Database as ldb

if DATABASE_TYPE == "db":
    from core.config import DATABASE_URL
    database = Database(DATABASE_URL)
    metadata = MetaData()
    engine = create_engine(DATABASE_URL,)


    class BaseRepository:
        def __init__(self, database: Database):
            self.database = database


elif DATABASE_TYPE == "local":
    local = ldb()
else:
    raise TypeError('Database type not found in supported. Select on db or local')

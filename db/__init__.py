from core.config import DATABASE_TYPE


if DATABASE_TYPE == "db":
    from .users import users
    from .base import metadata, engine
    metadata.create_all(bind=engine)
elif DATABASE_TYPE == "local":
    pass
else:
    raise TypeError('Database type not found in supported. Select on db or local')

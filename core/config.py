from starlette.config import Config


config = Config(".env")

DATABASE_TYPE = config("DATABASE_TYPE", cast=str, default="")
DATABASE_USER = config("DATABASE_USER", cast=str, default="root")
DATABASE_PASSWORD = config("DATABASE_PASSWORD", cast=str, default="root")
DATABASE_HOST = config("DATABASE_HOST", cast=str, default="localhost")
DATABASE_PORT = config("DATABASE_PORT", cast=str, default="32700")
DATABASE_NAME = config("DATABASE_NAME", cast=str, default="rest_service")

if DATABASE_TYPE == "db":
    DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
elif DATABASE_TYPE == "local":
    pass
else:
    raise TypeError('Database type not found in supported. Select on db or local')

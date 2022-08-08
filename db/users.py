import sqlalchemy
from core.config import DATABASE_TYPE

if DATABASE_TYPE == "db":
    from .base import metadata
    users = sqlalchemy.Table(
        "users",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
        sqlalchemy.Column("last_name", sqlalchemy.String),
        sqlalchemy.Column("first_name", sqlalchemy.String),
        sqlalchemy.Column("middle_name", sqlalchemy.String)
    )

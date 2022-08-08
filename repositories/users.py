from typing import Optional
from models.user import User, UserIn
from .base import BaseRepository
from core.config import DATABASE_TYPE

if DATABASE_TYPE == "db":
    from db.users import users

    class UserRepository(BaseRepository):
        async def get_by_id(self, id: int) -> Optional[User]:
            query = users.select().where(users.c.id==id)
            user = await self.database.fetch_one(query=query)
            if user is None:
                return None
            return User.parse_obj(user)

        async def create(self, u: UserIn) -> User:
            user = User(
                last_name=u.last_name,
                first_name=u.first_name,
                middle_name=u.middle_name
            )
            values = {**user.dict()}
            values.pop("id", None)
            query = users.insert().values(**values)
            user.id = await self.database.execute(query=query)
            return user

        async def update(self, id: int, u: UserIn) -> User:
            user = User(
                id=id,
                last_name=u.last_name,
                first_name=u.first_name,
                middle_name=u.middle_name
            )
            values = {**user.dict()}
            values.pop("id", None)
            query = users.update().where(users.c.id==id).values(**values)
            await self.database.execute(query=query)
            return user

        async def delete(self, id: int):
            query = users.delete().where(users.c.id==id)
            return await self.database.execute(query=query)

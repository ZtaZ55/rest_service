from typing import Dict, Optional
from models.user import User, UserIn


class Database:
    """
    Our local DB
    """

    def __init__(self):
        self._items: Dict[User] = {}

    def get(self, id: int) -> Optional[User]:
        return self._items.get(id)

    def create(self, u: UserIn) -> User:
        id = int(len(self._items) + 1)
        user_ = User(id=id, **u.dict())
        self._items[int(user_.id)] = user_
        return user_

    def update(self, id: int, u: UserIn) -> Optional[User]:
        user_ = User(id=id, **u.dict())
        self._items[int(user_.id)] = user_
        return self._items.get(id)

    def delete(self, id: int):
        del self._items[id]

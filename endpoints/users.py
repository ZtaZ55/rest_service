from fastapi import APIRouter, Depends, HTTPException, status
from models.user import User, UserIn

from core.config import DATABASE_TYPE

if DATABASE_TYPE == "db":
    from repositories.users import UserRepository
    from .depends import get_user_repository

    router = APIRouter()

    @router.get("/", response_model=User)
    async def read(id: int, users: UserRepository = Depends(get_user_repository)):
        user_ = await users.get_by_id(id=id)
        if user_ is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return await users.get_by_id(id=id)


    @router.post("/", response_model=User)
    async def create(user: UserIn, users: UserRepository = Depends(get_user_repository)):
        return await users.create(u=user)


    @router.put("/", response_model=User)
    async def update(id: int, user: UserIn, users: UserRepository = Depends(get_user_repository)):
        user_ = await users.get_by_id(id=id)
        if user_ is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return await users.update(id=id, u=user)


    @router.delete("/")
    async def delete(id: int, users: UserRepository = Depends(get_user_repository)):
        user_ = await users.get_by_id(id=id)
        if user_ is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        await users.delete(id=id)
        return {"status": True}

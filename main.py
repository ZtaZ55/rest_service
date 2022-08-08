import uvicorn
from fastapi import FastAPI, HTTPException, status
from endpoints import users
from models.user import User, UserIn
from core.config import DATABASE_TYPE

app = FastAPI(title="rest_service")

if DATABASE_TYPE == "db":
    from db.base import database
    app.include_router(users.router, prefix="/users", tags=["users"])

    @app.get("/")
    async def hello():
        return {"Rest Service": "User database"}

    @app.on_event("startup")
    async def startup():
        await database.connect()

    @app.on_event("shutdown")
    async def shutdown():
        await database.disconnect()

elif DATABASE_TYPE == "local":
    from db.base import local

    @app.get("/")
    async def hello():
        return {"Rest Service": "User database"}

    @app.get("/read", response_model=User)
    async def read_user(id: int):
        user = local.get(id=id)
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user

    @app.post("/create", response_model=User)
    async def create_user(user: UserIn):
        user_ = local.create(user)
        return user_

    @app.put("/update", response_model=User)
    async def update_user(id: int, user: UserIn):
        user_ = local.get(id=id)
        if user_ is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        local.update(id=id, u=user)
        return local.get(id=id)

    @app.delete("/delete")
    async def delete_user(id: int):
        user = local.get(id=id)
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        local.delete(id)
        return {"status": True}

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="127.0.0.1", reload=True)

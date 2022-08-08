from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: Optional[int] = None
    last_name: str
    first_name: str
    middle_name: Optional[str] = None


class UserIn(BaseModel):
    last_name: str
    first_name: str
    middle_name: Optional[str]

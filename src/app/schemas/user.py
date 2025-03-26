from typing import List
from pydantic import BaseModel, EmailStr, Field
from app.schemas.item import ItemRead

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int

    class Config:
        from_attributes = True

class UserWithItems(UserRead):
    items: List[ItemRead] = Field(default_factory=list)

UserWithItems.model_rebuild()
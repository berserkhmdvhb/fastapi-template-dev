from typing import List, Optional
from pydantic import BaseModel, EmailStr
from app.schemas.item import ItemRead

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int
    # replaces orm_mode
    class Config:
        from_attributes = True  

class UserWithItems(UserRead):
    items: List[ItemRead] = []
# needed for forward refs
UserWithItems.model_rebuild()  
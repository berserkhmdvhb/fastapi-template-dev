from pydantic import BaseModel, ConfigDict
from typing import Optional

class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    owner_id: Optional[int] = None

class ItemRead(ItemBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

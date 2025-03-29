from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List
from app.schemas.item import ItemCreate, ItemRead
from app.services.item_service import create_item, get_all_items, get_item_by_id
from app.dependencies.auth import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
def create_item_endpoint(item: ItemCreate, user: User = Depends(get_current_user)):
    item_data = item.model_dump()
    item_data["owner_id"] = user.id
    return create_item(ItemCreate(**item_data))

@router.get("/", response_model=List[ItemRead])
def list_items_endpoint(
    user: User = Depends(get_current_user),
    name: str | None = Query(None, description="Filter by item name"),
    description: str | None = Query(None, description="Filter by item description")
) -> List[ItemRead]:
    return get_all_items(name=name, description=description)

@router.get("/{item_id}", response_model=ItemRead)
def get_item_endpoint(
    item_id: int,
    name: str | None = Query(None, description="Optional name match"),
    user: User = Depends(get_current_user)
):
    item = get_item_by_id(item_id, name)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
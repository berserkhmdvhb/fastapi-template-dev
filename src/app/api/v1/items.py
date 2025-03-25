from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.schemas.item import ItemCreate, ItemRead
from app.services.item_service import create_item, get_all_items
from app.dependencies.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
def create_item_endpoint(item: ItemCreate, user: str = Depends(get_current_user)):
    return create_item(item)

@router.get("/", response_model=List[ItemRead])
def list_items_endpoint(user: str = Depends(get_current_user)):
    return get_all_items()
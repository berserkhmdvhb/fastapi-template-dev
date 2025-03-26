from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.user import UserCreate, UserRead, UserWithItems
from app.services.user_service import create_user, get_all_users, get_user_by_id

router = APIRouter()

@router.post("/", response_model=UserRead, status_code=201)
def create_user_endpoint(user: UserCreate) -> UserRead:
    return create_user(user)

@router.get("/", response_model=List[UserRead])
def list_users_endpoint() -> List[UserRead]:
    return get_all_users()

@router.get("/{user_id}", response_model=UserWithItems)
def get_user_endpoint(user_id: int) -> UserWithItems:
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
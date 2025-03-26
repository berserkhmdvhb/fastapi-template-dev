from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.schemas.user import UserCreate, UserRead, UserWithItems
from app.services.user_service import create_user, get_all_users, get_user_by_id
from app.dependencies.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=UserRead, status_code=201)
def create_user_endpoint(user: UserCreate) -> UserRead:
    return create_user(user)

@router.get("/", response_model=List[UserRead])
def list_users_endpoint(current_user: str = Depends(get_current_user)) -> List[UserRead]:
    return get_all_users()

@router.get("/{user_id}", response_model=UserWithItems)
def get_user_endpoint(user_id: int, current_user: str = Depends(get_current_user)) -> UserWithItems:
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
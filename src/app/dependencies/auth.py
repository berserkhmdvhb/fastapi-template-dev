from fastapi import Header, HTTPException, status
from typing import Annotated
from app.models.user import User
from app.services.user_service import get_user_by_username

def get_current_user(token: Annotated[str | None, Header()] = None) -> User:
    # If no token provided or token is invalid
    if token is None or token != "fake-super-secret-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized"
        )

    # Simulate user lookup by token (here we mock the lookup with a simple check)
    if token == "fake-super-secret-token":
        # Mocked user data
        user = User(id=1, username="authenticated_user", email="authenticated_user@example.com")
    else:
        user = None

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return user
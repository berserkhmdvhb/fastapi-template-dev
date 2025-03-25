from fastapi import Header, HTTPException, status
from typing import Annotated

def get_current_user(token: Annotated[str | None, Header()] = None):
    if token != "fake-super-secret-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized"
        )
    return "authenticated_user"
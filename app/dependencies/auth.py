from fastapi import Depends, HTTPException, status, Header

def get_current_user(token: str = Header(...)):
    if token != "fake-super-secret-token":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return "authenticated_user"
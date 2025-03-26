from sqlalchemy.orm import Session, selectinload
from app.models.user import User
from app.schemas.user import UserCreate
from app.db.session import SessionLocal

def create_user(user_data: UserCreate):
    db: Session = SessionLocal()
    user = User(**user_data.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return user

def get_all_users():
    db: Session = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users

def get_user_by_id(user_id: int):
    db: Session = SessionLocal()
    try:
        user = db.query(User)\
            .options(selectinload(User.items))\
            .filter(User.id == user_id)\
            .first()
        return user
    finally:
        db.close()

def get_user_by_username(username: str) -> User | None:
    db: Session = SessionLocal()
    try:
        # Fetch user by username and include their items
        user = db.query(User)\
            .options(selectinload(User.items))\
            .filter(User.username == username)\
            .first()
        return user
    finally:
        db.close()
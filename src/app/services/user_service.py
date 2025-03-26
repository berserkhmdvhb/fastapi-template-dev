from sqlalchemy.orm import Session
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
    user = db.query(User).filter(User.id == user_id).first()
    db.close()
    return user

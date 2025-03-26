from app.models.item import Item
from app.schemas.item import ItemCreate
from app.db.session import SessionLocal
from sqlalchemy.orm import Session

def create_item(item_data: ItemCreate):
    db: Session = SessionLocal()
    db_item = Item(**item_data.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    db.close()
    return db_item

def get_all_items():
    db: Session = SessionLocal()
    items = db.query(Item).all()
    db.close()
    return items

def get_item_by_id(item_id: int) -> Item | None:
    db: Session = SessionLocal()
    try:
        return db.query(Item).filter(Item.id == item_id).first()
    finally:
        db.close()
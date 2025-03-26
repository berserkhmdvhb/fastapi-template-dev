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

def get_all_items(name: str | None = None, description: str | None = None):
    db = SessionLocal()
    try:
        query = db.query(Item)
        if name:
            query = query.filter(Item.name.ilike(f"%{name}%"))
        if description:
            query = query.filter(Item.description.ilike(f"%{description}%"))
        return query.all()
    finally:
        db.close()

def get_item_by_id(item_id: int, name: str | None = None) -> Item | None:
    db: Session = SessionLocal()
    try:
        query = db.query(Item).filter(Item.id == item_id)
        if name:
            query = query.filter(Item.name.ilike(f"%{name}%"))
        return query.first()
    finally:
        db.close()

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base_class import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)

    items = relationship("Item", back_populates="owner")
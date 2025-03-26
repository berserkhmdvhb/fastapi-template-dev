import sys
import os

# Add the root of 'src/' to sys.path so 'app' becomes importable
current_dir = os.path.dirname(__file__)
source_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(source_dir)

from app.db.session import engine
from app.models.base_class import Base

# Import all models to register them with Base
from app.models.item import Item
from app.models.user import User

def run():
    print("Initializing database schema...")
    Base.metadata.create_all(bind=engine)
    print("Database schema created.")

if __name__ == "__main__":
    run()
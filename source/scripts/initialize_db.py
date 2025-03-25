import sys
import os

# Add the root of 'source/' to sys.path so 'app' becomes importable
current_dir = os.path.dirname(__file__)
source_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
sys.path.append(source_dir)

from app.models.item import Base
from app.db.session import engine

def run():
    print("Initializing database schema...")
    Base.metadata.create_all(bind=engine)
    print("Database schema created.")

if __name__ == "__main__":
    run()
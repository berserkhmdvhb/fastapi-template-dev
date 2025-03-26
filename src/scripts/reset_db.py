import os
import sys

# Add root of 'src/' to sys.path
current_dir = os.path.dirname(__file__)
source_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(source_dir)

from app.db.session import engine
from app.models import user, item  # Ensure models are imported so tables are known
from sqlalchemy.orm import declarative_base

Base = user.Base  # Reuse the same Base from your models

DB_PATH = "test_db.db"

def reset_db_file():
    print("Resetting database...")

    # Step 1: Delete the existing DB file if it exists
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print("Deleted old test_db.db")

    # Step 2: Recreate tables
    Base.metadata.create_all(bind=engine)
    print("Recreated DB schema")

if __name__ == "__main__":
    reset_db_file()

import sys
import os
from sqlalchemy import text

# Add root of 'src/' to sys.path so 'app' becomes importable
current_dir = os.path.dirname(__file__)
source_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(source_dir)

from app.db.session import SessionLocal
from app.models.item import Item
from app.models.user import User

def reset_tables():
    print("Resetting database tables...")

    db = SessionLocal()

    try:
        db.execute(text("DELETE FROM items"))
        db.execute(text("DELETE FROM users"))
        db.commit()

        # Reset AUTOINCREMENT (SQLite only, skip if not supported)
        try:
            db.execute(text("DELETE FROM sqlite_sequence WHERE name='items'"))
            db.execute(text("DELETE FROM sqlite_sequence WHERE name='users'"))
            db.commit()
        except Exception:
            print("Skipped AUTOINCREMENT reset (sqlite_sequence not found)")

        print("Tables truncated.")
    except Exception as e:
        db.rollback()
        print(f"Error during reset: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    reset_tables()
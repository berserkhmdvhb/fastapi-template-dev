from app.main import app

# This is just the launcher if you want to use `python main.py`
import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
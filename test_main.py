from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello(name: str | None = None):
    return {"msg": f"Hello, {name or 'world'}"}

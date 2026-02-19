from fastapi import FastAPI
from typing import Optional
from app.api.v2.routes import router


app = FastAPI()

app.include_router(router, prefix="/api/v2")

@app.get("/")
def read_root():
    return {"Hello": "Worldzzz"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "search_query": q}

@app.get("/users/{user_id}/items/{item_id}")
def read_user_item(user_id: int, item_id: int, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if short:
        item.update({"description": "This is a short description"})
    return item


@app.post("/terima")
def terima_data(data:dict):
    print(data)
    return{data:data}
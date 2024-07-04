from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.dependencies.database.db_connection import get_db
from ... import Item
from ... import ItemCreate


app = FastAPI(redoc_url=None)


# example GET endpoint to retrieve all items
@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = db.query(Item).offset(skip).limit(limit).all()
    return items


# example POST endpoint to create a new item
@app.post("/items/")
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

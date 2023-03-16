from fastapi import FastAPI
from typing import List
from .model import MyTable
from .db import get_db

app = FastAPI()

# view 
@app.get("/view-events/", response_model=List[MyTable])
async def get_items():
    db = get_db()
    db.execute("SELECT * FROM events;")
    items = [MyTable(id=row[0], name=row[1], event=row[2]) for row in db.fetchall()]
    db.close()
    return items

@app.post("/add-data")
async def add_data(name: str, event: str):
    """
    Add a new record to the database.
    """
    db = get_db()
    db.execute("INSERT INTO events (name, event) VALUES (%s, %s);", (name, event))
    db.connection.commit()
    db.close()
    return {"status": "ok", "message": "Data added successfully."}


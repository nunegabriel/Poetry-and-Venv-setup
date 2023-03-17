import psycopg2
from fastapi import FastAPI
from pathlib import Path

from fastapi import FastAPI, APIRouter
import settings
from settings import Settings
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import List

from dotenv import load_dotenv
import os

from database import SessionLocal, engine, DATABASE_PASSWORD
from schemas import Event
# import crud, models
import models
from models import MyTable
# from app.schemas import Event
# from app.schemas import Event
env_path = Path('.', '.env')
load_dotenv(dotenv_path=env_path)

load_dotenv()

models.Base.metadata.create_all(bind=engine)

# router = APIRouter()
router = APIRouter(
    prefix="/api/v1/ticket",
    tags=["tickets"],
)

settings = Settings()

# view 
@router.get("/view-events/",response_model=List[Event])
async def get_items():
    db = SessionLocal()
    items = db.query(MyTable).all()
    print(items)
    return items
    

#delete
@router.delete("/mytable/{item_id}")
async def delete_item(item_id: int):
    db = SessionLocal()
    db.query(MyTable).filter(MyTable.id == item_id).delete()
    db.commit()
    return {"message": "Item deleted"}

#edit
@router.put("/mytable/{item_id}")
async def update_item(item_id: int, name: str, event: str):
    db = SessionLocal()
    item = db.query(MyTable).filter(MyTable.id == item_id).first()
    if not item:
        return {"error": "Item not found"}
    item.name = name
    item.event = event
    db.add(item)
    db.commit()
    return {"message": "Item updated"}

# db details would be imported via settings

def get_db():
    """
    Open a new database connection and return a cursor object.
    """
    conn = psycopg2.connect(
        dbname=settings.db_name,
        user=settings.db_user,
        password=f"{DATABASE_PASSWORD}",
        host=settings.db_host,
        port=settings.db_port
    )
    cursor = conn.cursor()
    return cursor

@router.post("/add-data")
def add_data(name: str, event: str):
    """
    Add a new record to the database.
    """
    cursor = get_db()
    cursor.execute("INSERT INTO events (name, event) VALUES (%s, %s);", (name, event))
    cursor.connection.commit()
    cursor.close()
    return {"status": "ok", "message": "Data added successfully."}
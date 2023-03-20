import psycopg2
from fastapi import Depends,FastAPI
from pathlib import Path

from fastapi import FastAPI, APIRouter
import settings
from settings import Settings
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import List
import crud, schemas
from dotenv import load_dotenv
import os

from database import SessionLocal, engine, DATABASE_PASSWORD
from schemas import Event
import models
from models import MyTable

env_path = Path('.', '.env')
load_dotenv(dotenv_path=env_path)

load_dotenv()

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/api/v1/ticket",
    tags=["tickets"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

settings = Settings()

# view 
@router.get("/view-events/",response_model=List[Event])
async def get_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    events = crud.get_events(db, skip=skip, limit=limit)
    return events
    

#delete
@router.delete("/mytable/{item_id}")
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    db.query(MyTable).filter(MyTable.id == item_id).delete()
    db.commit()
    return {"message": "Item deleted"}

#edit
@router.put("/mytable/{item_id}")
async def update_item(item_id: int, name: str, event: str, db: Session = Depends(get_db)):
    item = db.query(MyTable).filter(MyTable.id == item_id).first()
    if not item:
        return {"error": "Item not found"}
    item.name = name
    item.event = event
    db.add(item)
    db.commit()
    return {"message": "Item updated"}

@router.post("/add-data", response_model=schemas.Event)

def add_event(event_create: schemas.CreateEvent, db: Session = Depends(get_db)):
     return crud.create_event(db=db, event_create=event_create)
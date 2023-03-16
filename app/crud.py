import psycopg2
from fastapi import FastAPI
from pathlib import Path

from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from . import crud, models, schemas
from .database import SessionLocal, engine
from . import models, schemas

 def get_items():
    db = SessionLocal()
    items = db.query(MyTable).all()
    return items

#delete
 def delete_item(item_id: int):
    db = SessionLocal()
    db.query(MyTable).filter(MyTable.id == item_id).delete()
    db.commit()
    return {"message": "Item deleted"}

#edit
 def update_item(item_id: int, name: str, event: str):
    db = SessionLocal()
    item = db.query(MyTable).filter(MyTable.id == item_id).first()
    if not item:
        return {"error": "Item not found"}
    item.name = name
    item.event = event
    db.add(item)
    db.commit()
    return {"message": "Item updated"}

# db details
db_name = "testing"
db_user = "postgres"
db_host = "localhost"
db_port = "5432"


def get_db():
    """
    Open a new database connection and return a cursor object.
    """
    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=f"{DATABASE_PASSWORD}",
        host=db_host,
        port=db_port
    )
    cursor = conn.cursor()
    return cursor

def add_data(name: str, event: str):
    """
    Add a new record to the database.
    """
    cursor = get_db()
    cursor.execute("INSERT INTO events (name, event) VALUES (%s, %s);", (name, event))
    cursor.connection.commit()
    cursor.close()
    return {"status": "ok", "message": "Data added successfully."}
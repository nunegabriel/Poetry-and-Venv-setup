import psycopg2
from fastapi import FastAPI
from pathlib import Path

from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
import os

env_path = Path('.', '.env')
load_dotenv(dotenv_path=env_path)

load_dotenv()

DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")


# SQLAlchemy engine to connect to your PostgreSQL database
SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{DATABASE_PASSWORD}@localhost/{DATABASE_NAME}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SQLAlchemy session to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class MyTable(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    event = Column(String)

app = FastAPI()

# view 
@app.get("/view-events/")
async def get_items():
    db = SessionLocal()
    items = db.query(MyTable).all()
    return items

#delete
@app.delete("/mytable/{item_id}")
async def delete_item(item_id: int):
    db = SessionLocal()
    db.query(MyTable).filter(MyTable.id == item_id).delete()
    db.commit()
    return {"message": "Item deleted"}

#edit
@app.put("/mytable/{item_id}")
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

@app.post("/add-data")
def add_data(name: str, event: str):
    """
    Add a new record to the database.
    """
    cursor = get_db()
    cursor.execute("INSERT INTO events (name, event) VALUES (%s, %s);", (name, event))
    cursor.connection.commit()
    cursor.close()
    return {"status": "ok", "message": "Data added successfully."}

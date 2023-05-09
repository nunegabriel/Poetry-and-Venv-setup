from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from typing import List
from schemas import ticket_schema
from database.database import get_db
from models import models
from controller import ticket_controller
from typing import Optional
from datetime import datetime


router = APIRouter(
    prefix="/api/v1/ticket",
    tags=["tickets"],
)


# view 
@router.get("/view-events/",response_model=List[ticket_schema.Event])
async def get_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    events = ticket_controller.get_events(db, skip=skip, limit=limit)
    return events
    
#delete
@router.delete("/mytable/{item_id}")
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    db.query(models.Event).filter(models.Event.id == item_id).delete()
    db.commit()
    return {"message": "Item deleted"}



@router.patch("/update-event/{item_id}")
async def update_item(
    item_id: int,
    name: str = None, 
    event: Optional[str] = None,
     db: Session = Depends(get_db)):
    item = db.query(models.Event).filter(models.Event.id == item_id).first()
    if not item:
        return {"error": "Item not found"}

    if name is not None:
        item.name = name
    if event is not None:
        item.event = event

    item.modified_date = datetime.now() 

    db.add(item)
    db.commit()
    return {"message": "Item updated"}

@router.post("/create-event", response_model=ticket_schema.Event)
def add_event(event_create: ticket_schema.CreateEvent, db: Session = Depends(get_db)):
     return ticket_controller.create_event(db=db, event_create=event_create)


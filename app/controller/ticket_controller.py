from sqlalchemy.orm import Session
from models import models
from schemas import ticket_schema

def get_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Event).offset(skip).limit(limit).all()

def create_event(db: Session, event_create: ticket_schema.Event):
    event_field = event_create.event
    time = event_create.creation_date
    mod_time = event_create.modified_date
    db_event = models.Event(name=event_create.name, event=event_field, creation_date=time, modified_date=mod_time)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

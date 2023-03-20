from sqlalchemy.orm import Session

import models
import schemas

def get_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MyTable).offset(skip).limit(limit).all()

def create_event(db: Session, event_create: schemas.CreateEvent):
    event_field = event_create.event
    db_event = models.MyTable(name=event_create.name, event=event_field)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

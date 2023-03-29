from pydantic import BaseModel
from typing import Optional
import datetime

# class CreateEvent(BaseModel):
#     name: str
#     event: str | None = None

class Event(BaseModel):
    id: int
    name: str
    event:str
    creation_date: datetime.datetime
    modified_date: datetime.datetime

    class Config:
        orm_mode = True

class CreateEvent(Event):
    pass
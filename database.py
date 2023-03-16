# schemas.py

from pydantic import BaseModel


class EventBase(BaseModel):
    name: str
    event: str


class EventCreate(EventBase):
    pass


class EventUpdate(EventBase):
    pass


class Event(EventBase):
    id: int

    class Config:
        orm_mode = True

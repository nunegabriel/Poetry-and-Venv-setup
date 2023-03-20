from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    event: str | None = None

class Event(BaseModel):
    id: int
    name: str
    event:str

    class Config:
        orm_mode = True

class CreateEvent(Event):
    pass
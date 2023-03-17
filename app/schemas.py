from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    event: str | None = None

class Event(BaseModel):
    name: str
    # event:str

    class Config:
        orm_mode = True
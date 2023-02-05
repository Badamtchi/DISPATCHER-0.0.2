from pydantic import BaseModel
from typing import Optional, Union
from datetime import datetime

class Message(BaseModel):
    title: str
    content: str

class MessageCreate(Message):
    sender: Optional[str] = "9121726429"
    receiver: Optional[str] = "9121143071"
    seen: bool = False

class MessageEdit(Message):
    pass 

class MessageBack(BaseModel):
    sender: str
    receiver: str
    title: str
    content: str
    seen: bool
    created_at: datetime

    class Config:
        orm_mode = True
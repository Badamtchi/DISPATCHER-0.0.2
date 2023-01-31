from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from .. import schemas
from ..data_access.database import get_db
from ..data_access.crud import MessageRepository

router = APIRouter(prefix='/msg', tags=['Messages'])

@router.get('/', response_model=list[schemas.MessageBack])
def get_all_msgs(db: Session=Depends(get_db)):
    msgs = MessageRepository(db).get_all_messages()
    return msgs
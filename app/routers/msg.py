from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
import uuid
from ..data_access import models
from .. import schemas
from ..data_access.database import get_db
from ..data_access.crud import MessageRepository

router = APIRouter(prefix='/msg', tags=['Messages'])

@router.get('/inbox', response_model=list[schemas.MessageBack])
def get_inbox(db:Session=Depends(get_db), user="9121143071"):
    msgs = MessageRepository(db).inbox(user)
    return msgs


@router.get('/inbox/unseen', response_model=list[schemas.MessageBack])
def get_inbox(db:Session=Depends(get_db), user="9121143071", unseen="False"):
    msgs = MessageRepository(db).inbox_unseen(user)
    return msgs


@router.get('/outbox', response_model=list[schemas.MessageBack])
def get_inbox(db:Session=Depends(get_db), user="9121143071"):
    msgs = MessageRepository(db).outbox(user)
    return msgs

@router.get('/{id}')
def get_msg(id: str, db:Session=Depends(get_db)):
    pass


@router.post('/send')
def send_msg(msg: schemas.MessageCreate, db: Session=Depends(get_db), user="9121726429"):
    new_id = uuid.uuid1()
    return MessageRepository(db).send(models.Messages(id=new_id, sender=user, **msg.dict()))
    

from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from .. import schemas
from ..data_access.database import get_db
from ..data_access.crud import MessageRepository

router = APIRouter(prefix='/msg', tags=['Messages'])


@router.get('/', response_model=list[schemas.MessageBack])
def get_inbox(db:Session=Depends(get_db), user="9121143071"):
    msgs = MessageRepository(db).inbox(user)
    return msgs

@router.get('/12', response_model=list[schemas.MessageBack])
def get_inbox(db:Session=Depends(get_db), user="9121143071"):
    msgs = MessageRepository(db).get_all_msgs(user)
    return msgs



#MessageRepository(db).get_messages(filters={"receiver": user})

"""
@router.get('/10', response_model=list[schemas.MessageBack])
def get_all_msgs(db: Session=Depends(get_db)):
    msgs = MessageRepository(db).get_all_messages()
    return msgs

@router.get('/12', response_model=list[schemas.MessageBack])
def get_messages(user="9121143071", db:Session=Depends(get_db)):
    msgs = MessageRepository(db).get_all_msgs(user)
    return msgs

@router.get('/15', response_model=list[schemas.MessageBack])
def get_messages(user="9121143071", db:Session=Depends(get_db)):
    msgs = MessageRepository(db).get_messages({"receiver": user})
    return msgs

@router.get('/17', response_model=list[schemas.MessageBack])
def get_messages(user="9121143071", db:Session=Depends(get_db)):
    msgs = MessageRepository(db).get_messages(filters={"receiver": user})
    return msgs
    """

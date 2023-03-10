from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
import uuid
from ..data_access import models
from .. import schemas, utils, oauth2
from ..data_access.database import get_db
from ..data_access.crud import MessageRepository

router = APIRouter(prefix='/msg', tags=['Messages'])


# get all inbox messages of current user
@router.get('/inbox', response_model=list[schemas.MessageBack])
def get_inbox(db:Session=Depends(get_db), user:str=Depends(oauth2.get_current_user)):
    return MessageRepository(db).inbox(user.phone)


# get all unseen inbox messages of current user
@router.get('/inbox/unseen', response_model=list[schemas.MessageBack])
def get_inbox_unseen(db:Session=Depends(get_db), user:str=Depends(oauth2.get_current_user)):
    return MessageRepository(db).inbox_unseen(user.phone)


# get all outbox messages of current user
@router.get('/outbox', response_model=list[schemas.MessageBack])
def get_outbox(db:Session=Depends(get_db), user:str=Depends(oauth2.get_current_user)):
    return MessageRepository(db).outbox(user.phone)


# get a message by id
@router.get('/{id}', response_model=schemas.MessageBack)
def get_msg(id: str, db:Session=Depends(get_db), user:str=Depends(oauth2.get_current_user)):
    msg = MessageRepository(db).msg_by_id_receiver(id, user.phone)
    if not msg:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Message was not found!')
    return msg


# send a new message by current user
@router.post('/send', status_code=status.HTTP_201_CREATED, response_model=schemas.MessageBack)
def send_msg(msg: schemas.MessageCreate, db: Session=Depends(get_db), user:str=Depends(oauth2.get_current_user)):
    new_id = uuid.uuid1()
    return MessageRepository(db).send(models.Messages(id=new_id, sender=user.phone, **msg.dict()))


# edit an existing message by it's sender
@router.put('/edit/{id}', response_model=schemas.MessageBack)
def edit_msg(id:str, updated_msg: schemas.MessageEdit, db: Session=Depends(get_db), user:str=Depends(oauth2.get_current_user)):
    msg = MessageRepository(db).msg_by_id_sender(id, user.phone)
    if not msg:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Message was not found!')
    return MessageRepository(db).edit(id, updated_msg, user.phone)


# delete an existing message by it's sender
@router.delete('/delete/{id}')
def delete_msg(id:str, db: Session=Depends(get_db), user:str=Depends(oauth2.get_current_user)):
    msg = MessageRepository(db).msg_by_id_sender(id, user.phone)
    if not msg:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Message was not found!')
    return Response(status_code=status.HTTP_204_NO_CONTENT)
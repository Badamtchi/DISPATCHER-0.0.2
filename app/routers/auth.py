from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..data_access.database import get_db
from .. import schemas, utils, oauth2
from ..data_access import models
from ..data_access.crud import UserRepository

router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(user_credential:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(get_db)):
    user = UserRepository(db).usr_by_phone(user_credential.username)
    if not user:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail='Invalid Credentials!')
    if not utils.verify(user_credential.password, user.password):
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail='Invalid Password!')
    access_token = oauth2.create_access_token(data={"user_id": user.phone})
    return {"access_token": access_token, "token_type": "bearer"}
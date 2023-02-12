from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from ..data_access import models
from .. import schemas, utils
from ..data_access.database import get_db
from ..data_access.crud import UserRepository

router = APIRouter(prefix='/user', tags=['Users'])

# create a new user
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.UserBack)
def get_inbox(user: schemas.UserCreate, db:Session=Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    return UserRepository(db).create(models.Users(**user.dict()))


# get a user by phone number as id
@router.get('/{phone}', response_model=schemas.UserBack)
def get_user(phone: str, db:Session=Depends(get_db)):
    pass
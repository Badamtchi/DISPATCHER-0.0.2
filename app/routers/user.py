from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from ..data_access import models
from .. import schemas
from ..data_access.database import get_db
from ..data_access.crud import UserRepository

router = APIRouter(prefix='/user', tags=['Users'])

@router.get('/')
def get_inbox():
    return {"message": "Khoda ro shokr"}
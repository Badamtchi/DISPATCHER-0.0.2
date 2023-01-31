from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(prefix='/msg', tags=['Messages'])

@router.get('/')
def hello_world():
    return {"message": "Hello Hello World"}
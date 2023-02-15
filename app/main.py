"""
DISPATCHER v0.0.2
NewVersion based on the architecture of repository pattern
FastAPI, PostgreSQL, ORM SQLalchemy, Alembic
Jan 2023
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import msg, user, auth
from .data_access import models
from .data_access.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='DISPATCHER',
    description='Simple messanger based on FastAPI',
    version='0.0.2',
    contact={
        "name": "Mehrdad Badamtchi",
        "email": "badamtchi@gmail.com"
    },
    license_info={
        "name": "BCE"
    }
)

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(msg.router)
app.include_router(user.router)
app.include_router(auth.router)
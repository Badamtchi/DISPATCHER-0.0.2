"""
DISPATCHER v0.0.2
NewVersion based on the architecture of repository pattern
FastAPI, PostgreSQL, ORM SQL alchemy, Alembic
Jan 2023
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router()
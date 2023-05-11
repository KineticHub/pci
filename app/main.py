import os

import psycopg2 as psycopg2
from fastapi import FastAPI

from app.utils.database import run_query

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/database/version")
def check_database_connection():
    db_version = run_query('SELECT version()')
    return {"message": f"Version: {db_version}"}

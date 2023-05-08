import os

import psycopg2 as psycopg2
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/database/version")
def check_database_connection():
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST', "localhost"),
        database=os.environ.get('DB_NAME'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        port=os.environ.get('DB_PORT', "5432")
    )

    cur = conn.cursor()
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    return {"message": f"Version: {db_version}"}


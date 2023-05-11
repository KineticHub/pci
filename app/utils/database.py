import os

import psycopg2
from psycopg2._psycopg import connection, cursor


def create_connection() -> connection:
    return psycopg2.connect(
        host=os.environ.get('DB_HOST', "localhost"),
        database=os.environ.get('DB_NAME'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        port=os.environ.get('DB_PORT', "5432")
    )


def run_query(query: str, size: int = None) -> []:
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(query)
    res = cur.fetchmany(size) if size else cur.fetchall()
    conn.close()
    return res

import logging
import os

import psycopg2
from dotenv import load_dotenv
from psycopg2.extensions import connection

load_dotenv()
logging.basicConfig(filename='logs/app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

conn: connection


def connect_to_db():
    global conn
    conn = psycopg2.connect(
        database=os.getenv('DATABASE_NAME'),
        host=os.getenv('DATABASE_HOST'),
        user=os.getenv('DATABASE_USER'),
        password=os.getenv('DATABASE_PASSWORD'),
        port=os.getenv('DATABASE_PORT')
    )
    logging.debug("CONNECTED TO DATABASE")


def disconnect_from_db():
    global conn
    if conn.closed != 0:
        conn.close()
    logging.debug("DISCONNECTED FROM DATABASE")


def run_select_query(query: str):
    logging.info(conn.closed)
    logging.debug(query)
    with conn.cursor() as cur:
        # cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchall()
    return result


def run_update_query(query: str):
    pass

import psycopg2
import os
import logging
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(filename='app.log', filemode='w', format='%(process)d - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

conn = psycopg2.connect(
    database=os.getenv('DATABASE_NAME'),
    host=os.getenv('DATABASE_HOST'),
    user=os.getenv('DATABASE_USER'),
    password=os.getenv('DATABASE_PASSWORD'),
    port=os.getenv('DATABASE_PORT')
)


def run_select_query(query: str):
    logging.info(conn.closed)
    # query = 'SELECT * FROM "Akas" akas WHERE akas.tconst'
    logging.debug(query)
    with conn.cursor() as cur:
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchall()
    return result

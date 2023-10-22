import logging
from fastapi import FastAPI
import helper

logging.basicConfig(filename='app.log', filemode='w', format='%(process)d - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/titles")
async def get_titles(adult: bool = True):
    query = """
        SELECT * FROM "Basic" b;
    """
    return helper.parse_basic(query, adult)


@app.get("/titles/other_names/{tconst}")
async def get_additional_titles(tconst: str):
    query = f"""
    SELECT * FROM "Akas" akas WHERE akas.tconst='{tconst}';
    """
    return helper.parse_akas(query)


@app.get("/titles/name/{sub_string}")
async def get_title_by_name(sub_string: str, adult: bool = True):
    query = f"""
    SELECT * from "Basic" b WHERE 
    b.original_title LIKE '%{sub_string}%' OR 
    b.promotion_title LIKE '%{sub_string}%';
    """
    return helper.parse_basic(query, adult)


@app.get("/actors/{tconst}")
async def get_actors_for_title(tconst: str):
    query = f"""
    SELECT * FROM "Person" p 
    WHERE p.nconst in (
    SELECT nconst FROM "Linker" l
    WHERE l.tconst='{tconst}');
    """
    return helper.parse_person(query)

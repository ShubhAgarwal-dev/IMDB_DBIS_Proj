from fastapi import FastAPI, Response, status
import logging

import db_handler
import helper
import docs

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

app = FastAPI(description=docs.description,
              openapi_tags=docs.tags_metadata)


@app.on_event("startup")
async def app_startup():
    logging.debug("APP STARTUP EVENT(S) STARTED")
    db_handler.connect_to_db()


@app.on_event("shutdown")
async def app_shutdown():
    logging.debug("APP SHUTDOWN EVENT(S) TAKING PLACE")
    db_handler.disconnect_from_db()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/titles", tags=["Basic"])
async def get_titles(adult: bool = True):
    query = """
        SELECT * FROM "Basic" b;
    """
    return helper.parse_basic(query, adult)


@app.get("/titles/other_names/{tconst}")
async def get_additional_titles(tconst: str):
    query = f"""
    SELECT DISTINCT * FROM "Akas" akas WHERE akas.tconst='{tconst}';
    """
    return helper.parse_akas(query)


@app.get("/titles/name")
async def get_title_by_name(sub_string: str, adult: bool = True):
    query = f"""
    SELECT DISTINCT * from "Basic" b WHERE 
    b.original_title LIKE '%{sub_string}%' OR 
    b.promotion_title LIKE '%{sub_string}%';
    """
    return helper.parse_basic(query, adult)


@app.get("/actors")
async def get_actors_for_title(tconst: str):
    query = f"""
    SELECT DISTINCT * FROM "Person" p 
    WHERE p.nconst in (
    SELECT nconst FROM "Linker" l
    WHERE l.tconst='{tconst}');
    """
    return helper.parse_person(query)


@app.get("/titles/order")
async def order_titles_by(param: str, adult: bool, response: Response):
    if not helper.basic_sort_param_checker(param):
        response.status_code = status.HTTP_204_NO_CONTENT
        return
    query = f"""
    SELECT DISTINCT * FROM "Basic" ORDER BY {param};
    """
    response.status_code = status.HTTP_200_OK
    return helper.parse_basic(query, adult)


@app.get("/titles/search")
async def basic_search(param: str, val: str, adult: bool, response: Response):
    if not helper.basic_sort_param_checker(param) or "," in param:
        response.status_code = status.HTTP_204_NO_CONTENT
        return
    query = f"""
    SELECT DISTINCT * FROM "Basic" b WHERE b.{param}='{val}';
    """
    response.status_code = status.HTTP_200_OK
    return helper.parse_basic(query, adult)


@app.get("/titles/director")
async def title_by_director(director: str, adult: bool, response: Response):
    query = f"""
    SELECT DISTINCT * FROM "Basic" b WHERE b.tconst IN 
    (SELECT d.tconst FROM "Director" d 
    JOIN "Person" P ON d.nconst = P.nconst 
    WHERE P.name LIKE '%{director}%' );
    """
    response.status_code = status.HTTP_200_OK
    return helper.parse_basic(query, adult)


@app.get("/titles/writer")
async def title_by_writer(writer: str, adult: bool, response: Response):
    query = f"""
    SELECT DISTINCT * FROM "Basic" b WHERE b.tconst IN 
    (SELECT w.tconst FROM "Writer" w 
    JOIN "Person" P ON w.nconst = P.nconst 
    WHERE P.name LIKE '%{writer}%' );
    """
    response.status_code = status.HTTP_200_OK
    return helper.parse_basic(query, adult)


@app.get("/titles/person")
async def title_by_person(name: str, adult: bool, response: Response):
    query = f"""
    SELECT DISTINCT *
    FROM "Basic" b
    WHERE b.tconst IN (SELECT L.tconst
                   FROM "Linker" L
                            JOIN "Person" P on P.nconst = L.nconst
                   WHERE P.name LIKE '%{name}%')
    """
    response.status_code = status.HTTP_200_OK
    return helper.parse_basic(query, adult)


@app.get("/titles/advSearch")
async def advanced_search(params: helper.SearchParams, adult: bool, response: Response):
    if not helper.advanced_param_validator(params):
        response.status_code = status.HTTP_204_NO_CONTENT
        return {"message": "send parameter correctly"}
    query = """SELECT * FROM "Basic" b;"""
    if params.num_params == 1:
        return helper.parse_basic(query, adult)
    response.status_code = status.HTTP_200_OK
    return {"message": "Implementation in progress"}

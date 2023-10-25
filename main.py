import logging

from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware

import Queries
import db_handler
import docs
import helper
import pw_handler

logging.basicConfig(filename='logs/app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)
                    
                    
app = FastAPI(description=docs.description,
              openapi_tags=docs.tags_metadata)


origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def app_startup():
    logging.debug("APP STARTUP EVENT(S) STARTED")
    db_handler.connect_to_db()
    pw_handler.make_salter()


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
    query = Queries.basic.basic_query()
    return helper.parse_basic(query, adult)


@app.get("/titles/other_names")
async def get_additional_titles(tconst: str, response: Response):
    if not helper.tconst_exists_in_relation("Akas", tconst):
        response.status_code = status.HTTP_404_NOT_FOUND
        return
    query = Queries.akas.akas_titles_by_tconst(tconst)
    response.status_code = status.HTTP_200_OK
    return helper.parse_akas(query)


@app.get("/titles/name")
async def get_title_by_name(sub_string: str, adult: bool, response: Response):
    if not sub_string:
        response.status_code = status.HTTP_404_NOT_FOUND
        return
    query = Queries.basic.basic_title_by_name(sub_string)
    response.status_code = status.HTTP_200_OK
    return helper.parse_basic(query, adult)


@app.get("/titles/order")
async def order_titles_by(param: str, adult: bool, response: Response):
    if not helper.basic_sort_param_checker(param):
        response.status_code = status.HTTP_204_NO_CONTENT
        return
    query = Queries.basic.basic_title_order_by_params(param)
    response.status_code = status.HTTP_200_OK
    return helper.parse_basic(query, adult)


@app.get("/titles/search")
async def basic_search(param: str, val: str, adult: bool, response: Response):
    logging.debug(param)
    logging.debug(val)
    if not helper.basic_search_param_checker(param) or "," in param:
        logging.debug("Request went here")
        response.status_code = status.HTTP_204_NO_CONTENT
        return
    query = Queries.basic.basic_title_filter_by_param_val(param, val)
    logging.info(query)
    response.status_code = status.HTTP_200_OK
    return helper.parse_basic(query, adult)


@app.get("/titles/director")
async def title_by_director(director: str, adult: bool, response: Response):
    query = Queries.basic.basic_title_by_director(director)
    response.status_code = status.HTTP_200_OK
    return helper.parse_basic(query, adult)


@app.get("/titles/writer")
async def title_by_writer(writer: str, adult: bool, response: Response):
    query = Queries.basic.basic_title_by_writers(writer)
    response.status_code = status.HTTP_200_OK
    return helper.parse_basic(query, adult)


@app.get("/titles/person")
async def title_by_person(name: str, adult: bool, response: Response):
    query = Queries.basic.basic_title_by_person(name)
    response.status_code = status.HTTP_200_OK
    return helper.parse_basic(query, adult)


@app.get("/titles/genres")
async def title_by_genres(gen_list: str, adult: bool, response: Response):
    query = Queries.basic.basic_title_with_genre(gen_list)
    response.status_code = status.HTTP_200_OK
    return helper.parse_basic(query, adult)


@app.post("/titles/advSearch")
async def advanced_search(params: helper.SearchParams, adult: bool, response: Response):
    if not helper.advanced_param_validator(params):
        response.status_code = status.HTTP_204_NO_CONTENT
        return {"message": "send parameter correctly"}
    query = """SELECT * FROM "Basic" b;"""
    if params.num_params == 1:
        return helper.parse_basic(query, adult)
    response.status_code = status.HTTP_200_OK
    return {"message": "Implementation in progress"}


@app.get("/actors")
async def get_actors_for_title(tconst: str, response: Response):
    if not helper.tconst_exists_in_relation("Linker", tconst):
        response.status_code = status.HTTP_404_NOT_FOUND
        return
    query = Queries.actors.get_actors_for_titles(tconst)
    response.status_code = status.HTTP_200_OK
    return helper.parse_person(query)


@app.get("/directors")
async def get_directors_for_title(tconst: str, response: Response):
    if not helper.tconst_exists_in_relation("Director", tconst):
        response.status_code = status.HTTP_404_NOT_FOUND
        return
    query = Queries.directors.get_directors_for_title(tconst)
    response.status_code = status.HTTP_200_OK
    return helper.parse_person(query)

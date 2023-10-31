import logging
from typing import Union

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
        response.status_code = status.HTTP_204_NO_CONTENT
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
        response.status_code = status.HTTP_204_NO_CONTENT
        return
    query = Queries.actors.get_actors_for_titles(tconst)
    response.status_code = status.HTTP_200_OK
    return helper.parse_person(query)


@app.get("/directors")
async def get_directors_for_title(tconst: str, response: Response):
    if not helper.tconst_exists_in_relation("Director", tconst):
        response.status_code = status.HTTP_204_NO_CONTENT
        return
    query = Queries.directors.get_directors_for_title(tconst)
    response.status_code = status.HTTP_200_OK
    return helper.parse_person(query)


@app.get("/title/id")
async def get_movie_by_title(tconst: str, response: Response):
    if not helper.tconst_exists_in_relation("Basic", tconst):
        response.status_code = status.HTTP_404_NOT_FOUND
        return
    query = Queries.basic.basic_movie_data(tconst)
    response.status_code = status.HTTP_200_OK
    return helper.parse_basic(query, True)


@app.get("/allPeople", tags=["Person"])
async def get_people(response: Response):
    query = Queries.persons.person_query()
    response.status_code = status.HTTP_200_OK
    return helper.parse_person(query)


@app.get("/titles/diretor_id")
async def get_movie_director(director_id: str, response: Response):
    query = Queries.directors.get_titles_for_director(director_id)
    response.status_code = status.HTTP_200_OK
    return helper.parse_basic(query, True)


@app.get("/person/titles", tags=["Person"])
async def get_person_movies(nconst: str, adult: bool, response: Response):
    query = Queries.persons.person_all_movie_query(nconst)
    response.status_code = status.HTTP_200_OK
    return helper.parse_basic(query, adult)


@app.get("/person/details", tags=["Person"])
async def get_person_details(nconst: str, response: Response):
    query = Queries.persons.person_detail_query(nconst)
    response.status_code = status.HTTP_200_OK
    return helper.parse_person(query)


@app.post("/user/rate")
async def rate_title(credentials: helper.Credentials, tconst: str, rating: float, review: Union[str, None],
                     response: Response):
    if not (uconst := helper.check_user_exists(credentials.username)):
        response.status_code = status.HTTP_404_NOT_FOUND
        return
    if not Queries.user.check_if_pwd_correct(credentials.username, credentials.password):
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return
    if res := helper.has_user_rated_movie(credentials.username, tconst):
        *_, old_rating, review = res
        Queries.user.update_rating(credentials.username, tconst, rating)
        rating = rating - old_rating
    else:
        Queries.user.insert_rating(uconst, tconst, rating, review)
    old_movie_rating = db_handler.run_select_query(Queries.basic.get_urating(tconst))[0][0]
    db_handler.run_insert_or_update_query(
        Queries.basic.update_urating(tconst, helper.calculate_rating(old_movie_rating, rating)))
    response.status_code = status.HTTP_200_OK
    return


@app.post("/user/add")
async def add_user(credentials: helper.Credentials, response: Response):
    if helper.check_user_exists(credentials.username):
        response.status_code = status.HTTP_409_CONFLICT
        return
    Queries.user.add_user(credentials.username, credentials.password)
    response.status_code = status.HTTP_200_OK
    return

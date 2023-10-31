import logging
from enum import Enum
from typing import Union, Tuple

from pydantic import BaseModel, Field

import db_handler
from db_handler import run_select_query

import Queries


logging.basicConfig(filename='logs/app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)


class Genres(Enum):
    Fiction = 1
    Crime = 2
    Horror = 3
    Ghoul = 4
    Romance = 5
    Fantasy = 6
    Drama = 7
    Action = 8
    War = 9
    Historical = 10
    Erotic = 11
    Adventure = 12
    Mystery = 13
    Anime = 14  # Anime ka 14
    Documentary = 15


class TitleTypes(Enum):
    alternative = 1
    dvd = 2
    festival = 3
    television = 4
    video = 5
    working = 6
    original_title = 7
    imdbDisplay = 8


class SearchParams(BaseModel):
    actor_name: Union[str, None] = None
    director_name: Union[str, None] = None
    writer_name: Union[str, None] = None
    person_name: Union[str, None] = None
    start_year: Union[int, None] = None
    end_year: Union[int, None] = None
    title: Union[str, None] = None  # FOR AKAS
    language: Union[str, None] = None  # FOR AKAS
    is_original_title: Union[bool, None] = None  # FOR AKAS
    # attributes: Union[TitleTypes, None] = None
    rating: Union[float, None] = Field(None, ge=0, le=10)
    urating: Union[float, None] = Field(None, ge=0, le=10)
    # genres: Union[List[Genres], None] = None


class Credentials(BaseModel):
    username: str
    password: str


def parse_basic(query: str, adult: bool):
    res = run_select_query(query)
    logging.debug(res)
    result = {
        "movies": [],
        "status": 200
    }
    for i in res:
        if adult or i[4] == False:
            result["movies"].append({
                "t_const": i[0],
                "title_type": i[1],
                "original_title": i[2],
                "promotional_title": i[3],
                "is_adult": i[4],
                "start_year": i[5],
                "end_year": i[6],
                "genres": i[7],
                "rating": i[8],
                "image_link": i[9]
            })
    return result


def parse_akas(query: str):
    res = run_select_query(query)
    logging.debug(res)
    result = {
        "movies": [],
        "status": 200
    }
    for i in res:
        result['movies'].append({
            "ordering": i[1],
            "local_title": i[2],
            "region": i[3],
            "language": i[4],
            "types": i[5],
            "attributes": i[6],
            "is_original_title": i[7]
        })
    return result


def parse_person(query: str):
    res = run_select_query(query)
    result = {
        "persons": [],
        "status": 200
    }
    for i in res:
        result["persons"].append({
            "nconst": i[0],
            "name": i[1],
            "birth_year": i[2],
            "death_year": i[3],
            "primary_profession": i[4]
        })
    return result


def parse_rating(query: str):
    res = run_select_query(query)
    result = {
        "rating": [],
        "status": 200
    }
    for i in res:
        result["rating"].append({
            "tconst": i[0],
            "rating": i[1],
            "review": i[2]
        })
    return result


def basic_sort_param_checker(param: str) -> bool:
    param_list = [param]
    if "," in param:
        param_list = param.split(",")
    valid_params = {"start_year", "end_year", "promotion_title", "original_title", "rating"}
    for param in param_list:
        param = param.strip()
        if param not in valid_params:
            return False
    return True


def basic_search_param_checker(param: str) -> bool:
    valid_params = {"start_year", "end_year", "promotion_title", "original_title", "genres", "rating", "title_type"}
    print(param)
    if param not in valid_params:
        return False
    return True


def parse_bool_for_sql(val: bool) -> str:
    return 'true' if val else 'false'


def query_builder(params: SearchParams):
    all_queries = []
    if params.actor_name:
        all_queries.append(Queries.actors.adv_actor_query(params.actor_name))
    if params.person_name:
        all_queries.append(Queries.persons.adv_person_query(params.person_name))
    if params.director_name:
        all_queries.append(Queries.directors.adv_director_query(params.director_name))
    if params.writer_name:
        all_queries.append(Queries.writers.adv_writer_query(params.writer_name))
    if params.start_year:
        all_queries.append(f"""SELECT tconst FROM "Basic" B WHERE B.start_year >= {params.start_year}""")
    if params.end_year:
        all_queries.append(f"""SELECT tconst FROM "Basic" B WHERE B.end_year <= {params.end_year}""")
    if params.rating:
        all_queries.append(f"""SELECT tconst FROM "Basic" B WHERE B.rating >= {params.rating}""")
    if params.urating:
        all_queries.append(f"""SELECT tconst FROM "Basic" B WHERE B.urating >= {params.urating}""")
    if params.title:
        base_query = f"""SELECT DISTINCT tconst FROM "Akas" WHERE local_title LIKE '%{params.title}%'"""
        if params.language:
            base_query = base_query + f""" AND language LIKE '%{params.language}%'"""
        if params.is_original_title:
            base_query = base_query + f""" AND is_original_title={parse_bool_for_sql(params.is_original_title)}"""
        all_queries.append(base_query)
    if not all_queries:
        # No parameter supplied
        return """SELECT * FROM "Basic";"""
    else:
        inner_part = " INTERSECT ".join(all_queries)
        final_query = f"""SELECT * FROM "Basic" WHERE tconst IN ({inner_part});"""
        return final_query


relations_with_tconst = {"Basic", "Akas", "Director", "Episode", "Linker", "Principal", "Writer"}


# noinspection SqlResolve
def tconst_exists_in_relation(relation: str, tconst: str) -> bool:
    if relation not in relations_with_tconst:
        return False
    query = f"""SELECT T.tconst from "{relation}" T WHERE T.tconst='{tconst}';"""
    logging.debug(query)
    res = run_select_query(query)
    logging.debug(bool(res))
    logging.debug(res)
    return bool(res)


def check_user_exists(uname: str) -> Union[Tuple[str], bool]:
    query = f"""
    SELECT * FROM "User" where username='{uname}';
    """
    res = run_select_query(query)
    return res[0] if bool(res) else False


def has_user_rated_movie(uname: str, tconst: str) -> Union[Tuple[str], bool]:
    if not (res := check_user_exists(uname)):
        return False
    uconst: str = res[0]
    query = f"""
    SELECT * FROM "Rating" R WHERE R.uconst='{uconst}' AND R.tconst='{tconst}';
    """
    res = run_select_query(query)
    return res[0] if bool(res) else False


def calculate_rating(old_rating, new_rating):
    return old_rating + (new_rating - old_rating) / 2 ** 14


def parse_individual_episode(episodes, parent):
    res = {
        parent: []
    }
    for episode in episodes:
        res[parent].append({
            "tconst": episode[0],
            "season": episode[2],
            "episode": episode[3]
        })
    return res


def get_all_episodes_mapping():
    opt = {
        "mapping": [],
        "status": 200
    }
    res = db_handler.run_select_query(Queries.episode.get_all_parent())
    for r in res:
        p_tconst = r[0]
        nres = db_handler.run_select_query(Queries.episode.get_episode_of_parent(p_tconst))
        opt["mapping"].append(parse_individual_episode(nres, p_tconst))
    return opt


def check_user_exists(uname: str) -> Union[Tuple[str], bool]:
    query = f"""
    SELECT * FROM "User" where username='{uname}';
    """
    res = run_select_query(query)
    return res[0] if bool(res) else False


def has_user_rated_movie(uname: str, tconst: str) -> Union[Tuple[str], bool]:
    if not (res := check_user_exists(uname)):
        return False
    uconst: str = res[0]
    query = f"""
    SELECT * FROM "Rating" R WHERE R.uconst='{uconst}' AND R.tconst='{tconst}';
    """
    res = run_select_query(query)
    return res[0] if bool(res) else False


def calculate_rating(old_rating, new_rating):
    return old_rating + (new_rating - old_rating) / 2 ** 14


def parse_individual_episode(episodes, parent):
    res = {
        parent: []
    }
    for episode in episodes:
        res[parent].append({
            "tconst": episode[0],
            "season": episode[2],
            "episode": episode[3]
        })
    return res


def get_all_episodes_mapping():
    opt = {
        "mapping": [],
        "status": 200
    }
    res = db_handler.run_select_query(Queries.episode.get_all_parent())
    for r in res:
        p_tconst = r[0]
        nres = db_handler.run_select_query(Queries.episode.get_episode_of_parent(p_tconst))
        opt["mapping"].append(parse_individual_episode(nres, p_tconst))
    return opt

def parse_query_results(results):
    return [{"title": row[0], "director": row[1], "writer": row[2], "actor": row[3]} for row in results]

def add_movie_to_database(title, director, writer, actor):
    try:
        query = f"INSERT INTO Movies (Title, Director, Writer, Actor) VALUES ('{title}', '{director}', '{writer}', '{actor}');"
        run_select_query(query)
        return True
    except Exception as e:
        print(f"Failed to add data: {e}")
        return False
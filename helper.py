import logging
from db_handler import run_select_query
from pydantic import BaseModel
from typing import Union
from enum import Enum

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',
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
    actor_name: Union[str | None] = None
    director_name: Union[str | None] = None
    writer_name: Union[str | None] = None
    start_year: Union[str | int | None] = None
    end_year: Union[str | int | None] = None
    title: Union[str | None] = None
    language: Union[str | None] = None
    is_original_title: Union[bool | None] = None
    attributes: Union[TitleTypes | None] = None
    rating: Union[float | str | None] = None
    genres: Union[Genres | None] = None
    num_params: Union[int] = 0


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
                "end_year": i[6]
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
        "movies": [],
        "status": 200
    }
    for i in res:
        result["movies"].append({
            "nconst": i[0],
            "name": i[1],
            "birth_year": i[2],
            "death_year": i[3],
            "primary_profession": i[4]
        })
    return result


def basic_sort_param_checker(param: str) -> bool:
    param_list = [param]
    if "," in param:
        param_list = param.split(",")
    valid_params = {"start_year", "end_year", "promotion_title", "original_title"}
    for param in param_list:
        param = param.strip()
        if param not in valid_params:
            return False
    return True


def advanced_param_validator(param: SearchParams) -> bool:
    if param.num_params == 0:
        return True
    elif param.num_params == 1:
        return False

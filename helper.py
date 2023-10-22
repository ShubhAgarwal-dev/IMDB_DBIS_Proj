import logging
from connection import run_select_query

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)


def parse_basic(query: str, adult: bool):
    res = run_select_query(query)
    logging.debug(res)
    result = {
        "movies": [],
        "status": 200
    }
    for i in res:
        if adult or i[4] == False:
            logging.debug(f"Value of is_adult {i[4]} for the movie {i[2]}")
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

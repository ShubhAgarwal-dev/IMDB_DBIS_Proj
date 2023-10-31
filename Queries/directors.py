def get_directors_for_title(tconst: str):
    return f"""
    SELECT * FROM "Person" P
    WHERE P.nconst IN (
    SELECT D.nconst FROM "Director" D
    WHERE D.tconst = '{tconst}');
    """


def get_titles_for_director(nconst: str):
    return f"""
    SELECT * FROM "Basic" B
    WHERE B.tconst IN (
        SELECT D.tconst FROM "Director" D
        WHERE D.nconst = '{nconst}'
    );
    """


def adv_director_query(director_name):
    director_name = director_name.split(",")
    total_queries = []
    for dir_name in director_name:
        total_queries.append(
            f"""SELECT L.tconst FROM "Director" L JOIN "Person" P on L.nconst = P.nconst WHERE name LIKE '%{dir_name}%'""")
    # total_queries[-1] = total_queries[-1] + ';'
    return " INTERSECT ".join(total_queries)

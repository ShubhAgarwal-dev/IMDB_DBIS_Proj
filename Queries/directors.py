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

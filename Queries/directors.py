def get_directors_for_title(tconst: str):
    return f"""
    SELECT * FROM "Person" P
    WHERE P.nconst IN (
    SELECT D.nconst FROM "Director" D
    WHERE D.tconst = '{tconst}');
    """

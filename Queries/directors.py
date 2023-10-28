def get_directors_for_title(tconst: str):
    return f"""
    SELECT * FROM "Person" P
    WHERE P.nconst IN (
    SELECT D.nconst FROM "Director" D
    WHERE D.tconst = '{tconst}');
    """

def basic_title_by_director(director: str):
    return f"""
    SELECT DISTINCT * FROM "Basic" b WHERE b.tconst IN 
    (SELECT d.tconst FROM "Director" d 
    JOIN "Person" P ON d.nconst = P.nconst 
    WHERE P.name LIKE '%{director}%' );
    """

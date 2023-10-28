def basic_title_by_writers(writer: str):
    return f"""
    SELECT DISTINCT * FROM "Basic" b WHERE b.tconst IN 
    (SELECT w.tconst FROM "Writer" w 
    JOIN "Person" P ON w.nconst = P.nconst 
    WHERE P.name LIKE '%{writer}%' );
    """

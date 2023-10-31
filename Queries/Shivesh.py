from db_handler import run_query

def get_movies_by_director(director_name):
    query = f"""
    SELECT B.tconst, B.original_title
    FROM "Basic" B
    JOIN "Director" D ON B.tconst = D.tconst
    JOIN "Person" P ON D.nconst = P.nconst
    WHERE P.name LIKE '%{director_name}%';
    """
    return run_query(query)

def get_movies_by_writer(writer_name):
    query = f"""
    SELECT B.tconst, B.original_title
    FROM "Basic" B
    JOIN "Writer" W ON B.tconst = W.tconst
    JOIN "Person" P ON P.nconst = W.nconst
    WHERE P.name LIKE '%{writer_name}%';
    """
    return run_query(query)

def get_actor_role_in_movie(actor_name):
    query = f"""
    SELECT B.tconst, B.original_title, P.name, R.role
    FROM "Basic" B
    JOIN "Principal" R ON B.tconst = R.tconst
    JOIN "Person" P ON P.nconst = R.nconst
    WHERE P.name LIKE '%{actor_name}%';
    """
    return run_query(query)

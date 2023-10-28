from db_handler import run_query

def get_movies_by_director(director_name):
    query = f"SELECT * FROM Movies WHERE Director = '{director_name}';"
    return run_query(query)

def get_movies_by_writer(writer_name):
    query = f"SELECT * FROM Movies WHERE Writer = '{writer_name}';"
    return run_query(query)

def get_actor_role_in_movie(actor_name):
    query = f"SELECT * FROM Movies WHERE Actor = '{actor_name}';"
    return run_query(query)

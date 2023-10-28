def get_actors_for_titles(tconst):
    return f"""
    SELECT DISTINCT * FROM "Person" p 
    WHERE p.nconst in (
    SELECT nconst FROM "Linker" l
    WHERE l.tconst='{tconst}');
    """

def get_role_of_actor_in_movie(actor_name: str):
   return f"SELECT movie_name, role FROM actor_roles WHERE actor_name = '{actor_name}';"


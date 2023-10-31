def get_actors_for_titles(tconst):
    return f"""
    SELECT DISTINCT * FROM "Person" p 
    WHERE p.nconst in (
    SELECT nconst FROM "Principal" l
    WHERE l.tconst='{tconst}' AND category = 'actor' OR category = 'actress');
    """


def adv_actor_query(actors_name):
    actors_name = actors_name.split(",")
    total_queries = []
    for act_name in actors_name:
        total_queries.append(
            f"""SELECT L.tconst FROM "Principal" L JOIN "Person" P on L.nconst = P.nconst WHERE name LIKE '%{act_name}%' AND category = 'actor' OR category = 'actress'""")
    # total_queries[-1] = total_queries[-1] + ';'
    return " INTERSECT ".join(total_queries)

def person_query():
    return """SELECT DISTINCT * FROM "Person" p;"""


def person_all_movie_query(nconst: str):
    return f"""SELECT DISTINCT * FROM "Basic" b 
            WHERE b.tconst IN (SELECT l.tconst from "Linker" l
            WHERE l.nconst='{nconst}');"""


def person_detail_query(nconst: str):
    return f"""SELECT * FROM "Person" p
            WHERE p.nconst='{nconst}';"""


def adv_person_query(persons_name: str):
    persons_name = persons_name.split(",")
    total_queries = []
    for per_name in persons_name:
        total_queries.append(
            f"""SELECT L.tconst FROM "Linker" L JOIN "Person" P on L.nconst = P.nconst WHERE name LIKE '%{per_name}%'""")
    # total_queries[-1] = total_queries[-1] + ';'
    return " INTERSECT ".join(total_queries)

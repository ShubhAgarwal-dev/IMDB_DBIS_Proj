def adv_writer_query(writer_name):
    writer_name = writer_name.split(",")
    total_queries = []
    for writer in writer_name:
        total_queries.append(
            f"""SELECT L.tconst FROM "Writer" L JOIN "Person" P on L.nconst = P.nconst WHERE name LIKE '%{writer}%'""")
    # total_queries[-1] = total_queries[-1] + ';'
    return " INTERSECT ".join(total_queries)
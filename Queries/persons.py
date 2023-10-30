def person_query():
    return """SELECT DISTINCT * FROM "Person" p;"""

def person_all_movie_query(nconst: str):
    return f"""SELECT DISTINCT * FROM "Basic" b 
            WHERE b.tconst IN (SELECT l.tconst from "Linker" l
            WHERE l.nconst='{nconst}');"""
    
def person_detail_query(nconst: str):
    return f"""SELECT * FROM "Person" p
            WHERE p.nconst='{nconst}';"""
            

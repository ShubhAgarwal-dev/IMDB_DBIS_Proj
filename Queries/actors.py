def get_actors_for_titles(tconst):
    return f"""
    SELECT DISTINCT * FROM "Person" p 
    WHERE p.nconst in (
    SELECT nconst FROM "Linker" l
    WHERE l.tconst='{tconst}');
    """

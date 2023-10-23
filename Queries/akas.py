def akas_titles_by_tconst(tconst: str):
    return f"""
    SELECT DISTINCT * FROM "Akas"
    akas WHERE akas.tconst='{tconst}';
    """

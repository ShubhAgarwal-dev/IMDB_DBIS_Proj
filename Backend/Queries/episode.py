def get_all_parent():
    return """SELECT DISTINCT parent_tconst FROM "Episode";"""


def get_episode_of_parent(p_tconst: str):
    return f"""SELECT DISTINCT * FROM "Episode" WHERE parent_tconst='{p_tconst}';"""

from typing import Union

import db_handler


def update_rating(uname: str, tconst: str, rating: float):
    query = f"""
    UPDATE "Rating" SET rating = {rating} WHERE 
    tconst='{tconst}' AND 
    uconst=(SELECT uconst FROM "User" U WHERE U.username='{uname}');
    """
    return db_handler.run_insert_or_update_query(query)


def insert_rating(uconst: str, tconst: str, rating: float, review: Union[str, None] = None):
    query = f"""
    INSERT INTO "Rating" (uconst, tconst, rating, review) values ('{uconst}', '{tconst}', {rating});
    """
    db_handler.run_insert_or_update_query(query)
    if review:
        query = f"""
        UPDATE "Rating" SET review = '{review}' WHERE
        uconst = '{uconst}' AND tconst = '{tconst}';
        """
        db_handler.run_insert_or_update_query(query)
    return


def get_titles(uconst: str):
    return f"""
    SELECT R.tconst, R.rating, R.review FROM "Rating" R WHERE uconst='{uconst}';
    """

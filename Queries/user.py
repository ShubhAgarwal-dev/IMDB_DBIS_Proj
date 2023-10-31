import db_handler
import pw_handler


def add_user(uname: str, password: str):
    hashed_password = pw_handler.hash_password(password)
    sql_compatible = pw_handler.sql_encoding(hashed_password)
    query = f"""
    INSERT INTO "User" (password, username) VALUES ('{sql_compatible}', '{uname}');
    """
    return db_handler.run_insert_or_update_query(query)


def check_if_pwd_correct(uname: str, password: str):
    query = f"""
    SELECT password FROM "User" where username = '{uname}';
    """
    pwd = db_handler.run_select_query(query)[0][0]
    decoded_pwd = pw_handler.decode_sql_pwd(pwd)
    return pw_handler.compare(password, decoded_pwd)

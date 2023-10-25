import argon2

import db_handler

pwh: argon2.PasswordHasher


def make_salter():
    global pwh
    pwh = argon2.PasswordHasher(parallelism=4)


def hash_password(password: str) -> str:
    return pwh.hash(password)


def compare(password: str, hashed_password: str) -> bool:
    return pwh.verify(hashed_password, password)


def retrieve_password(uname: str) -> str:
    query = """;"""
    return db_handler.run_select_query(query)


def store_password(uname: str):
    query = """"""

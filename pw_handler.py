import argon2

import db_handler

pwh: argon2.PasswordHasher
consts = ['', 'argon2id', 'v=19', 'm=102400,t=2,p=8', '']


def make_salter():
    global pwh
    global consts
    pwh = argon2.PasswordHasher(time_cost=2, memory_cost=102400, parallelism=8, hash_len=16, salt_len=16)


def hash_password(password: str) -> str:
    return pwh.hash(password)


def sql_encoding(hashed_password: str):
    fragments = hashed_password.split("$")
    return fragments[-2].encode().hex() + fragments[-1].encode().hex()


def compare(password: str, hashed_password: str) -> bool:
    try:
        pwh.verify(hashed_password, password)
        return True
    except argon2.exceptions.VerifyMismatchError:
        return False


def decode_sql_comp(password: str):
    salt, pwd = password[:44], password[44:]
    assemble_pwd = "$".join(consts)
    assemble_pwd += bytes.fromhex(salt).decode() + "$" + bytes.fromhex(pwd).decode()
    return assemble_pwd


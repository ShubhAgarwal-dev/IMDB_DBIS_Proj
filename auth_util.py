import os
from datetime import datetime, timedelta
from typing import Union, Any

from jose import jwt
from pydantic import BaseModel, ValidationError
from fastapi.security import HTTPBearer


jwt_path = HTTPBearer()

ACCESS_TOKEN_EXPIRE_MINUTES = 0.0
ALGORITHM = None
JWT_SECRET_KEY = "null"


def jwt_initialization():
    global ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, JWT_SECRET_KEY
    ACCESS_TOKEN_EXPIRE_MINUTES = 300
    ALGORITHM = "HS256"
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')


class TokenSchema(BaseModel):
    access_token: str


def create_access_token(subject: Union[str, Any], expires_delta: timedelta = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt


async def get_current_user(token):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, [ALGORITHM])
    except(jwt.JWTError, ValidationError):
        pass

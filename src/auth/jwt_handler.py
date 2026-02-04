import os
from datetime import datetime, timedelta
from jose import JWTError, jwt
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    encode = data.copy()
    expire = datetime.now() + (
        expires_delta if expires_delta else timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    encode.update({"exp": expire})
    token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
    return token


def verify_access_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None

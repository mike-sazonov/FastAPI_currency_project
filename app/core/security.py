import jwt
from fastapi import Depends, HTTPException, status
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer

from .config import settings
from app.db.fake_db import USER_DATA


oauth2_cheme = OAuth2PasswordBearer(tokenUrl="/auth/login/")    # !!!ОБЯЗАТЕЛЬНО АДРЕС КОНЕЧНОЙ ТОЧКИ АВТОРИЗАЦИИ!!!

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
EXP_TIME = timedelta(minutes=1)


# функция для создания JWT-токена
def create_jwt_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


# функция получения JWT-токена с полезной нагрузкой
def get_jwt_token_by_name(username):
    try:
        return {"access_token": create_jwt_token({
            "sub": username,
            "exp": datetime.utcnow() + EXP_TIME})}
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )


# функция получения пользователя по имени из БД
def get_user_from_db(username: str):
    for user in USER_DATA:
        if username == user.username:
            return user
    return None


# функция по извлечению информации о пользователе из полезной нагрузки
def get_user_from_token(token=Depends(oauth2_cheme)) -> str:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM,])
    return payload.get("sub")




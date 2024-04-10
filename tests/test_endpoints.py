from fastapi.testclient import TestClient
import unittest
from unittest.mock import patch, MagicMock

from main import app
from app.api.schemas.users import User
from app.db.fake_db import USER_DATA

client = TestClient(app)


# тест конечной точки регистрации
def test_register_new_user():
    response = client.post("/auth/register", json={"username": "Test_user", "password": "test_pass"})
    assert response.status_code == 200
    assert User(**{"username": "Test_user", "password": "test_pass"}) in USER_DATA
    assert response.json() == {"message": "Пользователь Test_user успешно зарегистрирован"}


# тест конечной точки аутентификации
def test_login():
    data = {"username": "Mike", "password": "1234"}
    response = client.post("/auth/login", data=data, headers={"content-type": "application/x-www-form-urlencoded"})
    # в headers передаём данные для jwt-ключа
    assert response.status_code == 200
    response_data = response.json()
    assert "access_token" in response_data
    return response.json()["access_token"]

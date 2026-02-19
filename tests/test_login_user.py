import allure
import pytest
from tests.config import LOGIN_URL, REG_URL
from tests.helper import generate_random_string
import requests

class TestLoginUser:
    @allure.title("вход под существующим пользователем")
    def test_login_user(self, user):
        
        resp = requests.post(LOGIN_URL, data = user)
        assert resp.status_code == 200
        data = resp.json()
        assert data["success"] == True
        assert 'accessToken' in data
        assert 'refreshToken' in data
        assert data["user"]["email"] == user["email"]
        assert data["user"]["name"] == user["name"]

    @pytest.mark.parametrize('field', ['email', 'password'])
    @allure.title("вход с неверным логином и паролем: {field}")
    def test_login_user(self, user, field):
        user[field] = user[field] + "!"
        resp = requests.post(LOGIN_URL, data = user)
        assert resp.status_code == 401
        data = resp.json()
        assert data["success"] == False
        assert data['message'] == 'email or password are incorrect'


"""
Создание пользователя:
создать уникального пользователя;
создать пользователя, который уже зарегистрирован;
создать пользователя и не заполнить одно из обязательных полей.
Логин пользователя:
вход под существующим пользователем;
вход с неверным логином и паролем.
Создание заказа:
с авторизацией;
без авторизации;
с ингредиентами;
без ингредиентов;
с неверным хешем ингредиентов.
"""

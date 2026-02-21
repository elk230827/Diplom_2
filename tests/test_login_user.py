import allure
import pytest
from tests.config import LOGIN_URL, REG_URL
from tests.helper import generate_random_string
import requests

class TestLoginUser:
    @allure.title("вход под существующим пользователем")
    def test_login_user(self, service, user):
        resp = service.create_user(user)
        resp = service.login(user)
        assert resp.status_code == 200
        data = resp.json()
        assert data["success"] == True
        assert 'accessToken' in data
        assert 'refreshToken' in data
        assert data["user"]["email"] == user["email"]
        assert data["user"]["name"] == user["name"]

    @pytest.mark.parametrize('field', ['email', 'password'])
    @allure.title("вход с неверным логином и паролем: {field}")
    def test_login_user_incorrect_data(self, service, user, field):
        resp = service.create_user(user)
        user[field] = user[field] + "!"
        resp = requests.post(LOGIN_URL, data = user)
        assert resp.status_code == 401
        data = resp.json()
        assert data["success"] == False
        assert data['message'] == 'email or password are incorrect'



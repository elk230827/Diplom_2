import allure
import pytest
from tests.config import REG_URL
from tests.helper import generate_random_string
import requests

class TestCreateUser:
    @allure.title("создать уникального пользователя")
    def test_create_unique_user(self):
        
        name = generate_random_string()
        user = {
            "name": name,
            "password": generate_random_string(),
            "email": f"{name}@yandex.ru"
            
        }

        resp = requests.post(REG_URL, data = user)
        assert resp.status_code == 200

    @allure.title("создать пользователя, который уже зарегистрирован")
    def test_create_user_duplicate(self, user):

        resp = requests.post(REG_URL, data = user)
        assert resp.status_code == 403
        assert resp.json()["message"] == 'User already exists'
 
    @pytest.mark.parametrize('field', ['name', 'password', 'email'])
    @allure.title("создать пользователя и не заполнить одно из обязательных полей: {field}")
    def test_create_user_wo_mandatory_fields(self, user, field):
        del user[field]
        resp = requests.post(REG_URL, data = user)
        assert resp.status_code == 403
        assert resp.json()["message"] == 'Email, password and name are required fields'



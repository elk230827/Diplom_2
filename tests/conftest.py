
import pytest
import requests

from tests.config import LOGIN_URL, REG_URL
from tests.helper import generate_random_string


@pytest.fixture
def user():
        return {'name': 'vvkfhjepqu', 'password': 'xmftrahimo', 'email': 'vvkfhjepqu@yandex.ru'}

        name = generate_random_string()

        user = {
            "name": name,
            "password": generate_random_string(),
            "email": f"{name}@yandex.ru"
            
        }

        resp = requests.post(REG_URL, data = user)
        return user

@pytest.fixture
def auth(user):
    resp = requests.post(LOGIN_URL, data = user)
    return resp.json()

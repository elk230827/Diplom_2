
import pytest
import requests

from tests.config import LOGIN_URL, REG_URL
from tests.helper import generate_random_string
from tests.user_service import UserService


@pytest.fixture
def user():
        name = generate_random_string()

        user = {
            "name": name,
            "password": generate_random_string(),
            "email": f"{name}@yandex.ru"
            
        }
        return user

@pytest.fixture
def auth(user):
    svc = UserService()
    svc.create_user(user)
    resp = svc.login(user)
    return resp.json()

@pytest.fixture
def service():
      return UserService()


import random
import string

import pytest

from tests.user_service import UserService

def generate_random_string(length=10):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

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

import allure
import pytest
from tests.config import INGREDIENTS, LOGIN_URL, ORDER_URL, REG_URL
from tests.helper import generate_random_string
import requests

class TestLoginUser:
    @allure.title("Создание заказа:с авторизацией")
    def test_order_auth(self, auth):
        headers  = {
            "Authorization": auth["accessToken"]
        }
        order = {
            "ingredients": INGREDIENTS
        }
        resp = requests.post(ORDER_URL, data=order, headers= headers)
        assert resp.status_code == 200
        data = resp.json()
        assert data["success"] == True

    @allure.title("Создание заказа без авторизации")
    def test_order_no_auth(self):
        order = {
            "ingredients": INGREDIENTS
        }
        resp = requests.post(ORDER_URL, data=order)
        assert resp.status_code == 403
        data = resp.json()
        assert data["success"] == False

    @allure.title("Создание заказа без ингредиентов")
    def test_order_no_ings(self):
        order = {
            "ingredients": []
        }
        resp = requests.post(ORDER_URL, data=order)
        assert resp.status_code == 400
        data = resp.json()
        assert data["success"] == False

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_order_bad_ings(self):
        order = {
            "ingredients": [INGREDIENTS[0] + "1"]
        }
        resp = requests.post(ORDER_URL, data=order)
        assert resp.status_code == 500



"""
Создание заказа:
с авторизацией;
без авторизации;
с ингредиентами;
;
с неверным хешем ингредиентов.
"""

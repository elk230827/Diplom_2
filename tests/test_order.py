import allure
from tests.config import INGREDIENTS

class TestOrder:
    @allure.title("Создание заказа:с авторизацией")
    def test_order_auth(self, service, auth):
        order = {
            "ingredients": INGREDIENTS
        }
        resp = service.order(order, auth)
        assert resp.status_code == 200
        data = resp.json()
        assert data["success"] == True

    @allure.title("Создание заказа без авторизации")
    def test_order_no_auth(self, service):
        order = {
            "ingredients": INGREDIENTS
        }
        resp = service.order(order)
        assert resp.status_code == 403
        data = resp.json()
        assert data["success"] == False

    @allure.title("Создание заказа без ингредиентов")
    def test_order_no_ings(self, service):
        order = {
            "ingredients": []
        }
        resp = service.order(order)
        assert resp.status_code == 400
        data = resp.json()
        assert data["success"] == False

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_order_bad_ings(self, service):
        order = {
            "ingredients": [INGREDIENTS[0] + "1"]
        }
        resp = service.order(order)
        assert resp.status_code == 500




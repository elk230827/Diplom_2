import allure
import requests

from tests.config import LOGIN_URL, ORDER_URL, REG_URL

NO_AUTH = {"accessToken": None}

class UserService:
    @allure.step("Создать пользователя")
    def create_user(self, user):
        return requests.post(REG_URL, data = user)

    @allure.step("Войти")
    def login(self, user):
        return requests.post(LOGIN_URL, data = user)
    
    @allure.step("Заказать")
    def order(self, order, auth = NO_AUTH):
        headers  = {
            "Authorization": auth["accessToken"]
        }
        return requests.post(ORDER_URL, data=order, headers= headers)


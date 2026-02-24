import allure
from .base_page import BasePage


class CarPage(BasePage):

    @allure.step("Проверяем, что карточка автомобиля открыта")
    def is_opened(self):
        return "car" in self.page.url

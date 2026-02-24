import allure
from .base_page import BasePage


class MainPage(BasePage):
    URL = "https://sberauto.com/"

    @allure.step("Открываем главную страницу")
    def open_main(self):
        self.open(self.URL)

    @allure.step("Переходим в поиск по параметрам")
    def go_to_search(self):
        self.page.get_by_role("link", name="Поиск по параметрам").click()

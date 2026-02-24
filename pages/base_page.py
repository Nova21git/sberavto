import allure
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Открываем страницу: {url}")
    def open(self, url: str):
        self.page.goto(url)

    @allure.step("Кликаем по локатору: {locator}")
    def click(self, locator: str):
        self.page.locator(locator).click()

    @allure.step("Кликаем по роли: {role}, имя: {name}")
    def click_role(self, role: str, name: str, nth=None):
        loc = self.page.get_by_role(role, name=name)
        loc = loc.nth(nth) if nth is not None else loc
        loc.click()

    @allure.step("Кликаем по тексту: {text}")
    def click_text(self, text: str):
        self.page.get_by_text(text).click()

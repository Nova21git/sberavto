import allure
from .base_page import BasePage


class SearchPage(BasePage):

    @allure.step("Выбираем марку: {brand}")
    def select_brand(self, brand: str):
        self.page.get_by_role("button", name="Open").first.click()
        self.page.get_by_role("option", name=brand).get_by_test_id("selectBrand_0_option").click()

    @allure.step("Выбираем модель: {model}")
    def select_model(self, model: str):
        self.page.get_by_role("button", name="Open").nth(1).click()
        self.page.get_by_role("option", name=model, exact=True).get_by_test_id("selectModel_0_option").click()

    @allure.step("Выбираем поколение: {generation}")
    def select_generation(self, generation: str):
        self.page.get_by_role("button", name="Open").nth(1).click()
        self.page.get_by_text(generation).click()
        self.page.get_by_role("button", name="Close").click()

    @allure.step("Открываем карточку автомобиля")
    def open_car_card(self):
        self.page.locator("[data-test-id='filterTotalCount']").click()
        with self.page.expect_popup() as popup:
            self.page.locator("[data-test-id^='car_card_']").first.click()
        return popup.value

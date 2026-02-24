import allure
from playwright.sync_api import expect
from .base_page import BasePage


class FiltersPage(BasePage):

    URL = "https://sberauto.com/cheboksary/cars?geoDistance=200"

    @allure.step("Открываем страницу фильтров")
    def open_filters(self):
        self.open(self.URL)

    # Локаторы
    @property
    def no_mileage(self):
        return self.page.get_by_test_id("withoutMileageFilter").get_by_test_id("filterCheckbox_checkbox")

    @property
    def warranty(self):
        return self.page.get_by_test_id("warrantySwitch").get_by_test_id("filterCheckbox_checkbox")

    @property
    def credit(self):
        return self.page.get_by_test_id("creditSearchSwitch").get_by_test_id("filterCheckbox_checkbox")

    @property
    def price_to(self):
        return self.page.get_by_role("textbox", name="До").first

    @allure.step("Переключаем чекбокс: ожидаем состояние {expected_state}")
    def toggle_checkbox(self, element, expected_state: bool):
        if expected_state:
            element.check()
            expect(element).to_be_checked()
        else:
            element.uncheck()
            expect(element).not_to_be_checked()

    @allure.step("Устанавливаем цену 'До' = {value}")
    def set_price_to(self, value: str):
        self.price_to.fill(value)
        expect(self.price_to).to_have_value(value)

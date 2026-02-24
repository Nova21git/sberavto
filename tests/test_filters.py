import pytest
import allure
from pages.filters_page import FiltersPage


@pytest.mark.parametrize("checkbox_name, expected_state", [
    ("no_mileage", True),
    ("no_mileage", False),
    ("warranty", True),
    ("warranty", False),
    ("credit", True),
    ("credit", False),
])
@allure.feature("Фильтры")
@allure.story("Проверка чекбоксов")
def test_filter_checkboxes(page, checkbox_name, expected_state):
    filters = FiltersPage(page)
    filters.open_filters()

    checkbox = getattr(filters, checkbox_name)
    filters.toggle_checkbox(checkbox, expected_state)


@allure.feature("Фильтры")
@allure.story("Проверка ввода суммы")
def test_price_input(page):
    filters = FiltersPage(page)
    filters.open_filters()

    filters.credit.check()
    filters.set_price_to("4 000 000")

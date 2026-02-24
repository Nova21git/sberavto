import allure
from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.car_page import CarPage


@allure.feature("Поиск авто")
@allure.story("Поиск Kia Ceed")
def test_search_kia_ceed(page):
    main = MainPage(page)
    search = SearchPage(page)

    main.open_main()
    main.go_to_search()

    search.select_brand("Kia")
    search.select_model("Ceed")
    search.select_generation("3 Рестайлинг")

    car_page = search.open_car_card()
    car = CarPage(car_page)

    assert car.is_opened()

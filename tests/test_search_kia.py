from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.car_page import CarPage

def test_search_kia_ceed(page):
    main = MainPage(page)
    search = SearchPage(page)

    # 1. Открываем главную
    main.open_main()

    # 2. Переходим в поиск
    main.go_to_search()

    # 3. Выбираем параметры
    search.select_brand("Kia")
    search.select_model("Ceed")
    search.select_generation("3 Рестайлинг")

    # 4. Открываем карточку авто
    car_page = search.open_car_card()
    car = CarPage(car_page)

    # 5. Проверяем, что карточка открылась
    assert car.is_opened()

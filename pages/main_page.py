from .base_page import BasePage

class MainPage(BasePage):
    URL = "https://sberauto.com/"

    def open_main(self):
        self.open(self.URL)

    def go_to_search(self):
        self.page.get_by_role("link", name="Поиск по параметрам").click()

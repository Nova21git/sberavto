from .base_page import BasePage

class CarPage(BasePage):

    def is_opened(self):
        return "car" in self.page.url

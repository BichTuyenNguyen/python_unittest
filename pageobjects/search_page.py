from pageobjects.page import BasePage
from pageobjects.constant_locators import *


class SearchPage(BasePage):
    def search(self, product):
        self.set_element_text(SEARCH_INPUT, product, enter=True)

    def click_on_first_item(self):
        self.click_element(FIRST_ITEM)

    def get_item_name(self):
        return self.get_element_text(DETAIL_ITEM_NAME)










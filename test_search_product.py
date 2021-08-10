import time
import unittest

from hamcrest import equal_to, contains_string
from hamcrest.core import assert_that
from selenium import webdriver
from config.env_setup import EnvSetup
from pageobjects.login_page import LoginPage
from pageobjects.search_page import SearchPage
from config.test_users import TUYEN


class TestDetailProduct(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver')

    def test_add_to_cart(self):
        login_page = LoginPage(self.driver)
        login_page.navigate(EnvSetup.URL)
        login_page.login(test_user=TUYEN)
        assert_that(login_page.get_username(), contains_string('bichtuyen0068'))

    def test_search_product(self):
        search_page = SearchPage(self.driver)
        search_page.navigate(EnvSetup.URL)
        search_page.search('Sách')
        search_page.click_on_first_item()
        actual_name = search_page.get_item_name()
        assert_that(actual_name.lower(), contains_string('sách'))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

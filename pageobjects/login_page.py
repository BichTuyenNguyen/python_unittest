from pageobjects.page import BasePage
from pageobjects.constant_locators import *


class LoginPage(BasePage):
    def click_ads_close_button(self):
        self.click_element(ADS_CLOSE_BTN)

    def click_login_button(self):
        self.click_element(LOGIN_BUTTON)

    def input_email(self, email):
        self.set_element_text(EMAIL_INPUT, email)

    def input_password(self, password):
        self.set_element_text(PASSWORD_INPUT, password, enter=True)

    def get_username(self):
        return self.get_element_text(USERNAME_LBL)

    def login(self, test_user):
        self.click_ads_close_button()
        self.click_login_button()
        self.input_email(test_user['email'])
        self.input_password(test_user['password'])











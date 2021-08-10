from selenium.webdriver.common.by import By

# SEARCH PAGE
SEARCH_INPUT = (By.CLASS_NAME, 'shopee-searchbar-input__input')
FIRST_ITEM = (By.XPATH, '//div[contains(@class, "shopee-search-item-result__item")][1]/a')
DETAIL_ITEM_NAME = (By.XPATH, '((//div[contains(@class, "product-briefing flex card")]//div[contains(@class, "flex-auto")])[1]//span)[1]')

# LOGIN PAGE
ADS_CLOSE_BTN = (By.CLASS_NAME, 'shopee-popup__close-btn')
LOGIN_BUTTON = (By.XPATH, '//a[text()="Đăng nhập"]')
EMAIL_INPUT = (By.NAME, 'loginKey')
PASSWORD_INPUT = (By.NAME, 'password')
USERNAME_LBL = (By.CLASS_NAME, 'navbar__username')
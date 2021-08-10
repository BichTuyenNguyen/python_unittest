from config.env_setup import EnvSetup
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage(object):
    SELENIUM_TIMEOUT_SECONDS = EnvSetup.SELENIUM_TIMEOUT_SECONDS

    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def wait_element_to_be_clickable(self, tuple_locator, timeout=SELENIUM_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.element_to_be_clickable(tuple_locator))
        return element

    def wait_element_to_be_visible(self, tuple_locator, timeout=SELENIUM_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.visibility_of_element_located(tuple_locator))
        return element

    def wait_elements_to_be_present(self, tuple_locator, timeout=SELENIUM_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.presence_of_all_elements_located(tuple_locator))
        return element

    def click_element(self, tuple_locator, timeout=SELENIUM_TIMEOUT_SECONDS):
        element = self.wait_element_to_be_clickable(tuple_locator, timeout)
        element.click()

    def set_element_text(self, tuple_locator, value, enter=False, timeout=SELENIUM_TIMEOUT_SECONDS):
        element = self.wait_element_to_be_visible(tuple_locator, timeout)
        element.send_keys(value)
        if enter:
            element.send_keys(Keys.ENTER)

    def get_element_text(self, tuple_locator, timeout=SELENIUM_TIMEOUT_SECONDS):
        element = self.wait_element_to_be_visible(tuple_locator, timeout)
        return element.text

    def get_element_texts(self, tuple_locator, timeout=SELENIUM_TIMEOUT_SECONDS):
        elements = self.wait_elements_to_be_present(tuple_locator, timeout)
        texts = []
        for element in elements:
            texts.append(element.text)
        return texts

    def get_current_url(self):
        return self.driver.current_url

    def get_attribute_of_element(self, tuple_locator, attribute, timeout=SELENIUM_TIMEOUT_SECONDS):
        element = self.wait_element_to_be_visible(tuple_locator, timeout)
        return element.get_attribute(attribute)

    def clear_element_text(self, tuple_locator, timeout=SELENIUM_TIMEOUT_SECONDS):
        element = self.wait_element_to_be_visible(tuple_locator, timeout)
        return element.clear()

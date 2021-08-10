import os


class EnvSetup:
    URL = os.getenv('URL', 'https://shopee.vn/')
    API = os.getenv('API', 'https://shopee.vn/')
    TOKEN = os.getenv('TOKEN', 'https://shopee.vn/')
    SELENIUM_TIMEOUT_SECONDS = 30



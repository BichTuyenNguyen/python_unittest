import os


class EnvSetup:
    API = os.getenv('API', 'https://api.unsplash.com')
    TOKEN = os.getenv('TOKEN', '9uaS6y3F4-ulSf8MJPuM9EKL4CY2NVkq7yRUOodnv3A')


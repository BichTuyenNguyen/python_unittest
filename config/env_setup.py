import os


class EnvSetup:
    API = os.getenv('API', 'https://api.unsplash.com')
    TOKEN = os.getenv('TOKEN', '9Fr3N7X0ngNl5xp2-t6x7ZNrEb1-UFq2At6cR4tSAmQ')


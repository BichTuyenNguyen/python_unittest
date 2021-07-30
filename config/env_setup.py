import os


class EnvSetup:
    API = os.getenv('API', 'https://api.unsplash.com')
    TOKEN = os.getenv('TOKEN', 'iVsrOL71QA-AOJ_JeeCCIiT1fP3eN6uNJhQz3IFdSNs')


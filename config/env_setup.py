import os


class EnvSetup:
    API = os.getenv('API', 'https://api.unsplash.com')
    TOKEN = os.getenv('TOKEN', 'XVu_3P_7WQ_zEEH7v_66TWW8eN7YVhLTdcikzGRCIso')


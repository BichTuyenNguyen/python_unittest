import requests
from config.env_setup import EnvSetup


class RequestHelper:
    API_URL = EnvSetup.API
    HEADERS = {
        'Authorization': f'Bearer {EnvSetup.TOKEN}',
    }

    @staticmethod
    def get(endpoint, headers=False, params=None):
        if headers:
            headers = RequestHelper.HEADERS
        return requests.get(url=RequestHelper.API_URL + endpoint, headers=headers, params=params)

    @staticmethod
    def post(endpoint, headers=False, params=None, data=None):
        if headers:
            headers = RequestHelper.HEADERS
        return requests.post(url=RequestHelper.API_URL + endpoint, headers=headers, params=params, data=data)

    @staticmethod
    def put(endpoint, headers=False, params=None, data=None):
        if headers:
            headers = RequestHelper.HEADERS
        return requests.put(url=RequestHelper.API_URL + endpoint, headers=headers, params=params, data=data)

    @staticmethod
    def delete(endpoint, headers=False, params=None, data=None):
        if headers:
            headers = RequestHelper.HEADERS
        return requests.delete(url=RequestHelper.API_URL + endpoint, headers=headers, params=params, data=data)
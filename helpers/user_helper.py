from helpers.request_helper import RequestHelper
from helpers.endpoints import GET_USER_PROFILE_ENDPOINT


class UserHelper(RequestHelper):
    @staticmethod
    def get_user_profile(username):
        return RequestHelper.get(endpoint=GET_USER_PROFILE_ENDPOINT.format(username), headers=True)

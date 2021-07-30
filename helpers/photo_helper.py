from helpers.request_helper import RequestHelper
from helpers.endpoints import GET_PHOTO_ENDPOINT, GET_A_PHOTO_INFOMATION_ENDPOINT, GET_A_RANDOM_PHOTO_ENDPOINT, UNLIKE_AND_LIKE_A_PHOTO_ENDPOINT


class PhotoHelper(RequestHelper):
    @staticmethod
    def get_a_photo(photo_id):
        return RequestHelper.get(endpoint=GET_PHOTO_ENDPOINT.format(id=photo_id), headers=True)

    @staticmethod
    def get_a_random_photo():
        return RequestHelper.get(endpoint=GET_A_RANDOM_PHOTO_ENDPOINT, headers=True)

    @staticmethod
    def unlike_a_photo(photo_id):
        return RequestHelper.delete(endpoint=UNLIKE_AND_LIKE_A_PHOTO_ENDPOINT.format(id=photo_id), headers=True)

    @staticmethod
    def like_a_photo(photo_id):
        return RequestHelper.post(endpoint=UNLIKE_AND_LIKE_A_PHOTO_ENDPOINT.format(id=photo_id), headers=True)

    @staticmethod
    def get_a_photo_infomation(id):
        return RequestHelper.get(endpoint=GET_A_PHOTO_INFOMATION_ENDPOINT.format(id), headers=True)

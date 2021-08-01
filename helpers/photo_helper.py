from helpers.request_helper import RequestHelper
from helpers.endpoints import *


class PhotoHelper(RequestHelper):
    @staticmethod
    def get_a_photo(photo_id):
        return RequestHelper.get(endpoint=GET_PHOTO_ENDPOINT.format(id=photo_id), headers=True)

    @staticmethod
    def get_a_random_photo():
        return RequestHelper.get(endpoint=GET_RANDOM_PHOTO_ENDPOINT, headers=True)

    @staticmethod
    def like_a_photo(photo_id):
        return RequestHelper.post(endpoint=LIKE_PHOTO_ENDPOINT.format(id=photo_id), headers=True)

    @staticmethod
    def unlike_a_photo(photo_id):
        return RequestHelper.delete(endpoint=UNLIKE_PHOTO_ENDPOINT.format(id=photo_id), headers=True)

    @staticmethod
    def get_a_photo_info(photo_id):
        return RequestHelper.get(endpoint=GET_A_PHOTO_INFO_ENDPOINT.format(id=photo_id), headers=True)

    @staticmethod
    def get_a_photo_related(photo_id):
        return RequestHelper.get(endpoint=GET_A_PHOTO_RELATED_ENDPOINT.format(id=photo_id), headers=True)

    @staticmethod
    def update_a_photo(photo_id, description, show_on_profile, tags):
        data = {
            'description': description,
            'show_on_profile': show_on_profile,
            'tags': tags
        }
        return RequestHelper.put(endpoint=GET_PHOTO_ENDPOINT.format(id=photo_id), headers=True, data=data)

from helpers.request_helper import RequestHelper
from helpers.endpoints import *


class CollectionHelper(RequestHelper):
    @staticmethod
    def get_collection(collection_id):
        return RequestHelper.get(endpoint=GET_COLLECTION_ENDPOINT.format(id=collection_id), headers=True)

    @staticmethod
    def get_collection_photo(collection_id):
        return RequestHelper.get(endpoint=GET_COLLECTION_PHOTO_ENDPOINT.format(id=collection_id), headers=True)

    @staticmethod
    def create_collection(title, description, private):
        data = {
            "title": title,
            "description": description,
            "private": private
        }
        return RequestHelper.post(endpoint=CREATE_COLLECTION_ENDPOINT, headers=True, data=data)

    @staticmethod
    def update_collection(collection_id, title, description, private):
        data = {
            'title': title,                 # Required
            'description': description,     # Optional
            'private': private              # Optional
        }
        return RequestHelper.put(endpoint=GET_COLLECTION_ENDPOINT.format(id=collection_id), headers=True, data=data)

    @staticmethod
    def delete_collection(collection_id):
        return RequestHelper.delete(endpoint=GET_COLLECTION_ENDPOINT.format(id=collection_id), headers=True)

    @staticmethod
    def add_photo_to_collection(collection_id, photo_id):
        data = {
            'photo_id': photo_id       # Required
        }
        return RequestHelper.post(endpoint=ADD_PHOTO_TO_COLLECTION_ENDPOINT.format(id=collection_id),
                                  headers=True, data=data)

    @staticmethod
    def remove_photo_from_collection(collection_id, photo_id):
        data = {
            'photo_id': photo_id  # Required
        }
        return RequestHelper.delete(endpoint=DELETE_PHOTO_COLLECTION_ENDPOINT.format(id=collection_id),
                                    headers=True, data=data)

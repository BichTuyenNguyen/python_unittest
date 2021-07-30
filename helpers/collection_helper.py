from helpers.request_helper import RequestHelper
from helpers.endpoints import GET_COLLECTION_ENDPOINT, GET_COLLECTION_PHOTO_ENDPOINT, CREATE_COLLECTION_ENDPOINT,COLLECTION_ID_ENDPOINT, ADD_PHOTO_TO_COLLECTION_ENDPOINT, REMOVE_PHOTO_FROM_COLLECTION_ENDPOINT

class CollectionHelper(RequestHelper):
    @staticmethod
    def get_collection(collection_id):
        # endpoint = '/collections/{id}'.format(id=collection_id)
        return RequestHelper.get(endpoint=GET_COLLECTION_ENDPOINT.format(id=collection_id), headers=True)

    @staticmethod
    def get_collection_photo(collection_id):
        # endpoint = '/collections/{id}/photos'.format(id=collection_id)
        return RequestHelper.get(endpoint=GET_COLLECTION_PHOTO_ENDPOINT.format(id=collection_id), headers=True)

    @staticmethod
    def create_collection(title, description, private):
        # endpoint = '/collections'
        data = {
            'title': title,                             # Required
            'description': description,     # Optional
            'private': private                      # Optional
        }
        return RequestHelper.post(endpoint=CREATE_COLLECTION_ENDPOINT, headers=True, data=data)

    @staticmethod
    def update_collection(collection_id, title, description, private):
        params = {
            'title': title,                             # Required
            'description': description,     # Optional
            'private': private                      # Optional
        }
        return RequestHelper.put(endpoint=COLLECTION_ID_ENDPOINT.format(id=collection_id), headers=True, params=params)

    @staticmethod
    def delete_collection(collection_id):
        return RequestHelper.delete(endpoint=COLLECTION_ID_ENDPOINT.format(id=collection_id), headers=True)

    @staticmethod
    def add_photo_to_collection(collection_id, photo_id):
        params = {
            'photo_id': '{photo_id}'.format(photo_id=photo_id)        # Required
        }
        return RequestHelper.post(endpoint=ADD_PHOTO_TO_COLLECTION_ENDPOINT.format(id=collection_id), headers=True, params=params)

    @staticmethod
    def remove_photo_from_collection(collection_id, photo_id):
        params = {
            'collection_id': id,  # Required
            'photo_id': photo_id  # Required
        }
        return RequestHelper.delete(endpoint=REMOVE_PHOTO_FROM_COLLECTION_ENDPOINT.format(id=collection_id), headers=True, params=params)

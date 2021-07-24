from helpers.request_helper import RequestHelper


class CollectionHelper(RequestHelper):
    @staticmethod
    def get_collection(collection_id):
        endpoint = '/collections/{id}'.format(id=collection_id)
        return RequestHelper.get(endpoint=endpoint, headers=True)

    @staticmethod
    def get_collection_photo(collection_id):
        endpoint = '/collections/{id}/photos'.format(id=collection_id)
        return RequestHelper.get(endpoint=endpoint, headers=True)

    @staticmethod
    def create_collection(title, description, private):
        endpoint = '/collections'
        params = {
            'title': '{title}'.format(title=title),                             # Required
            'description': '{description}'.format(description=description),     # Optional
            'private': '{private}'.format(private=private)                      # Optional
        }
        return RequestHelper.post(endpoint=endpoint, headers=True, params=params)

    @staticmethod
    def update_collection(collection_id, title, description, private):
        endpoint = '/collections/{id}'.format(id=collection_id)
        params = {
            'title': '{title}'.format(title=title),                             # Required
            'description': '{description}'.format(description=description),     # Optional
            'private': '{private}'.format(private=private)                      # Optional
        }
        return RequestHelper.put(endpoint=endpoint, headers=True, params=params)

    @staticmethod
    def delete_collection(collection_id):
        endpoint = '/collections/{id}'.format(id=collection_id)
        return RequestHelper.delete(endpoint=endpoint, headers=True)

    @staticmethod
    def add_photo_to_collection(collection_id, photo_id):
        endpoint = '/collections/{id}/add'.format(id=collection_id)
        params = {
            'photo_id': '{photo_id}'.format(photo_id=photo_id)        # Required
        }
        return RequestHelper.post(endpoint=endpoint, headers=True, params=params)

    @staticmethod
    def remove_photo_from_collection(collection_id, photo_id):
        endpoint = '/collections/{id}/remove'.format(id=collection_id)
        params = {
            'collection_id': '{id}'.format(id=collection_id),  # Required
            'photo_id': '{photo_id}'.format(photo_id=photo_id)  # Required
        }
        return RequestHelper.delete(endpoint=endpoint, headers=True, params=params)

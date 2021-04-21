from unit_test_demo.helpers.request_helper import RequestHelper


class PhotoHelper(RequestHelper):
    @staticmethod
    def get_a_photo(photo_id):
        endpoint = '/photos/{id}'.format(id=photo_id)
        return RequestHelper.get(endpoint=endpoint, headers=True)

    @staticmethod
    def get_a_random_photo():
        endpoint = '/photos/random'
        return RequestHelper.get(endpoint=endpoint, headers=True)

    @staticmethod
    def unlike_a_photo(photo_id):
        endpoint = '/photos/{id}/like'.format(id=photo_id)
        return RequestHelper.delete(endpoint=endpoint, headers=True)

    @staticmethod
    def like_a_photo(photo_id):
        endpoint = '/photos/{id}/like'.format(id=photo_id)
        return RequestHelper.post(endpoint=endpoint, headers=True)

import unittest
from hamcrest import assert_that, greater_than
from helpers.photo_helper import PhotoHelper


class LikeAPhotoTestCase(unittest.TestCase):
    def setUp(self):
        self.photo_id = PhotoHelper.get_a_random_photo().json()['id']

    def test_like_photo(self):
        # 1. get photo's previous like
        photo_previous_like = PhotoHelper.get_a_photo(self.photo_id).json()['likes']
        print('photo_previous_like: ' + str(photo_previous_like))

        # 2. Like -> get photo's current like
        response = PhotoHelper.like_a_photo(self.photo_id)
        photo_current_like = response.json()['photo']['likes']
        print('photo_current_like: ' + str(photo_current_like))

        # Assertion
        assert_that(photo_current_like, greater_than(photo_previous_like), 'Verify the photo like')

    def tearDown(self):
        # Dislike
        PhotoHelper.unlike_a_photo(self.photo_id)
        print('teardown: ' + str(PhotoHelper.unlike_a_photo(self.photo_id).json()['photo']['likes']))


if __name__ == '__main__':
    unittest.main()

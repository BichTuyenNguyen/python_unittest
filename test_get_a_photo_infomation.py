import unittest
from hamcrest import assert_that, equal_to
from helpers.photo_helper import PhotoHelper


class TestCaseStringMethods(unittest.TestCase):
    def setUp(self):
        self.photo_id = PhotoHelper.get_a_random_photo().json()[id]

    def get_a_photo_infomation(self):
        photo_info = PhotoHelper.get_a_photo(self.photo_id).json()['exif']
        print('photo infomation: ' + str(photo_info))

        # 2. Like -> get photo's current like
        # response = PhotoHelper.like_a_photo(self.photo_id)
        # photo_current_like = response.json()['photo']['likes']

        # response = PhotoHelper.get_a_photo_infomation("3c5v9BGnMe8")
        # info_photo = response.json()['exif']['make']
        # # print('photo infomation' + str(info_photo))
        # assert_that(response.status_code, 200, 'Verify status')


if __name__ == '__main__':
    unittest.main()

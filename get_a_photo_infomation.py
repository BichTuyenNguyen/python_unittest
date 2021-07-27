import unittest
from hamcrest import assert_that, equal_to
from helpers.photo_helper import PhotoHelper


class TestCaseStringMethods(unittest.TestCase):
    def get_a_photo_infomation(self):
        response = PhotoHelper.get_a_photo_infomation("3c5v9BGnMe8")
        info_photo = response.json()['exif']
        print('photo infomation' + str(info_photo))

if __name__ == '__main__':
    unittest.main()

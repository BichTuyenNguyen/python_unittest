import unittest
from hamcrest import assert_that, greater_than
from helpers.photo_helper import PhotoHelper


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.photo_id = PhotoHelper.get_a_random_photo().json()['id']

    def test_get_a_photo_info(self):
        exif = PhotoHelper.get_a_photo_info(self.photo_id).json()['exif']
        print('exif: ' + str(exif))
        # make = PhotoHelper.get_a_photo_info(self.photo_id).json()['exif']['make']
        # print('make: ' + str(make))
        # model = PhotoHelper.get_a_photo_info(self.photo_id).json()['exif']['model']
        # print('model: ' + str(model))
        # exposure_time = PhotoHelper.get_a_photo_info(self.photo_id).json()['exif']['exposure_time']
        # print('exposure_time: ' + str(exposure_time))
        # aperture = PhotoHelper.get_a_photo_info(self.photo_id).json()['exif']['aperture']
        # print('aperture: ' + str(aperture))
        # focal_length = PhotoHelper.get_a_photo_info(self.photo_id).json()['exif']['focal_length']
        # print('focal_length: ' + str(focal_length))

        # 2. Like -> get photo's current like
        #response = PhotoHelper.like_a_photo(self.photo_id)
        #photo_current_like = response.json()['photo']['likes']
        #print('photo_current_like: ' + str(photo_current_like))

        # Assertion
        #assert_that(photo_current_like, greater_than(photo_previous_like), 'Verify the photo like')

    #def tearDown(self):
        # Dislike
        #PhotoHelper.unlike_a_photo(self.photo_id)
        #print('teardown: ' + str(PhotoHelper.unlike_a_photo(self.photo_id).json()['photo']['likes']))


if __name__ == '__main__':
    unittest.main()

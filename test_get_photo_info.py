import unittest
from hamcrest import assert_that, equal_to
from helpers.photo_helper import PhotoHelper

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        # self.photo_id = PhotoHelper.get_a_random_photo().json()['id']
        self.photo_id = '3c5v9BGnMe8'
    def test_get_photo_info(self):
        # get_photo_info = PhotoHelper.get_a_photo(self.photo_id).json()['exif']
        # print("get photo info" + str(get_photo_info))
        # get_photo_infomation = PhotoHelper.get_a_photo_infomation(self.photo_id).json()['exif']
        # print("Get photo infomation id 3c" + str(get_photo_infomation))
        response = PhotoHelper.get_a_photo_infomation(self.photo_id)
        # Camera Make - Camera Model - Focal Length - Aperture - Shutter Speed - ISO
        camera_make = response.json()['exif']['make'] # Canon
        # print('\nCamera make: ' + str(camera_make))
        camera_model = response.json()['exif']['model'] # Canon EOS R5
        focal_length = response.json()['exif']['focal_length'] # 139.0
        aperture = response.json()['exif']['aperture'] # 5.0
        shutter_speed = response.json()['exif']['exposure_time'] # 1/250
        iso = response.json()['exif']['iso'] # 320

        assert_that(response.status_code, 200, 'Verify status')
        assert_that(camera_make, equal_to('Canon'), 'Verify the camera make')
        assert_that(camera_model, equal_to('Canon EOS R5'), 'Verify the camera model')
        assert_that(focal_length, equal_to('139.0'), 'Verify focal length')
        assert_that(aperture, equal_to('5.0'), 'Verify the aperture')
        assert_that(shutter_speed, equal_to('1/250'), 'Verify shutter speed')
        assert_that(iso, equal_to(320), 'Verify ISO')

if __name__ == '__main__':
    unittest.main()
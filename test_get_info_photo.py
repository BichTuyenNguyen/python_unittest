import unittest
from hamcrest import assert_that, equal_to
from helpers.photo_helper import PhotoHelper


class GetAPhotoInfoTestCase(unittest.TestCase):
    def setUp(self):
        self.photo_id = 'LcZ9JhMQ-JQ'

    def test_get_a_photo_info(self):
        response = PhotoHelper.get_a_photo(self.photo_id)
        print('self.photo_id: ' + str(self.photo_id))
        exif = response.json()['exif']
        print('exif: ' + str(exif))
        make = response.json()['exif']['make']
        print('Camera Make: ' + str(make))
        model = response.json()['exif']['model']
        print('Camera Model: ' + str(model))
        exposure_time = response.json()['exif']['exposure_time']
        print('Shutter Speed: ' + str(exposure_time) + 's')
        aperture = response.json()['exif']['aperture']
        print('Aperture: f/' + str(aperture))
        focal_length = response.json()['exif']['focal_length']
        print('Focal Length: ' + str(focal_length) + 'mm')
        iso = response.json()['exif']['iso']
        print('ISO: ' + str(iso))
        height = response.json()['height']
        width = response.json()['width']
        print('Dimensions: ' + str(width) + ' x ' + str(height))

        # Assertion
        assert_that(response.status_code, 200, 'Verify response status code')
        assert_that(make, equal_to("Canon"), 'Verify the make')
        assert_that(model, equal_to("Canon EOS Rebel SL2"), 'Verify the model')
        assert_that(exposure_time, equal_to("1/500"), 'Verify the exposure_time')
        assert_that(aperture, equal_to("1.8"), 'Verify the aperture')
        assert_that(focal_length, equal_to("50.0"), 'Verify the focal_length')
        assert_that(iso, equal_to(100), 'Verify the iso')
        assert_that(height, equal_to(3657), 'Verify the height')
        assert_that(width, equal_to(5484), 'Verify the width')


if __name__ == '__main__':
    unittest.main()

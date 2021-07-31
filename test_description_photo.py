import unittest
from hamcrest import assert_that, equal_to
from helpers.photo_helper import PhotoHelper


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.id_ = '3j2DndiM7BQ'
        self.photo_id = self.id_

    def test_discription_photo(self):
        response = PhotoHelper.get_a_photo(self.photo_id)
        description = response.json()['description']
        print('\nDiscription: ' + str(description))
        alt_description = response.json()['alt_description']
        print('Alt Description: ' +str(alt_description))

        assert_that(response.status_code, 200, 'Verify response status code')
        assert_that(description, equal_to('girls, jeep, sand dunes'),
                    'Verify the discription of photo width id is 3j2DndiM7BQ')
        assert_that(alt_description, equal_to('red suv on brown sand during daytime'), 'Verify the alt discription of photo width id is 3j2DndiM7BQ')


if __name__ == '__main__':
    unittest.main()
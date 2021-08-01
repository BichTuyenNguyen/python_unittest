import unittest
from hamcrest import assert_that, equal_to
from helpers.photo_helper import *


class UpdateAPhotoTestCase(unittest.TestCase):
    def setUp(self):
        self.oy = 'm7Y8uI8xiOY'
        self.photo_id = self.oy

    def test_update_a_photo(self):
        update = PhotoHelper.update_a_photo(self.photo_id, 'Carabao Dang Energy Drink', 'No', 'Energy Drink')
        description = update.json()['description']
        print('Description: ' + str(description))
        assert_that(update.status_code, 200, 'Verify response status code')
        print('Status code: ' + str(update.status_code))
        assert_that(description, equal_to('Carabao Dang Energy Drink'), 'Verify the Description')

    def tearDown(self):
        tear_down_res = PhotoHelper.update_a_photo(self.photo_id, 'Nước tăng lực Carabao', 'Yes', 'Nước tăng lực')
        print('teardown: ' + str(tear_down_res.status_code))


if __name__ == '__main__':
    unittest.main()

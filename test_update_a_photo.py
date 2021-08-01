import unittest
from hamcrest import assert_that, equal_to
from helpers.photo_helper import PhotoHelper

class TestCaseUpdateAPhoto(unittest.TestCase):
    def setUp(self):
        self.id_ = "t2p6LV8SLn4"
        self.photo_id= self.id_

    def test_update_a_photo(self):
        get_description_of_photo =PhotoHelper.get_a_photo(self.photo_id).json()['description']
        print('\ndercription befor update a photo: ' + str(get_description_of_photo))

        response = PhotoHelper.update_description_of_photo(self.photo_id, 'update description new')
        description = response.json()['description']
        print('description update:' + str(description))
        assert_that(response.status_code, 200, 'Verify update descriptio successfully')
        assert_that(description, equal_to('update description new'), 'Verify update new descripton of photo by me upload')

    def tearDown(self):
        back_description = PhotoHelper.update_description_of_photo(self.photo_id, 'abc def')
        # print('back description:' + str(back_description))
        assert_that(back_description.status_code, 200, 'Verify back description after')

if __name__ == '__main__':
    unittest.main()
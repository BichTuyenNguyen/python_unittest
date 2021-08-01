import unittest
from hamcrest import assert_that, equal_to, greater_than
from helpers.photo_helper import PhotoHelper


class GetDescriptionTestCase(unittest.TestCase):
    def setUp(self):
        self.u = 'Sg3XwuEpybU'
        self.photo_id = self.u

    def test_get_photo_description(self):
        response = PhotoHelper.get_a_photo(self.photo_id)
        print('self.photo_id: ' + str(self.photo_id))
        alt_description = response.json()['alt_description']
        print('alt Description: ' + str(alt_description))
        description = response.json()['description']
        print('Description: ' + str(description))

        assert_that(response.status_code, 200, 'Verify response status code')
        assert_that(alt_description, equal_to("yellow Labrador retriever biting yellow tulip flower"),
                    'Verify the alt Description')
        assert_that(description, equal_to("Happy Women’s Day!"), 'Verify the Description')

    def test_get_photo_related(self):
        response = PhotoHelper.get_a_photo_related(self.photo_id)
        print('self.photo_id: ' + str(self.photo_id))
        counting_results = response.json()['total']
        print('results: ' + str(counting_results) + ' related id')

        assert_that(response.status_code, 200, 'Verify response status code')
        assert_that(counting_results, greater_than(0), 'Verify count result is greater than 0')


if __name__ == '__main__':
    unittest.main()

import unittest
from hamcrest import assert_that, greater_than
from helpers.photo_helper import PhotoHelper

class TestCaseGetTotalRelated(unittest.TestCase):
    def setUp(self):
        self.id_ = '3j2DndiM7BQ'
        self.photo_id = self.id_

    def test_get_total_related(self):
        response = PhotoHelper.get_related_photos(self.photo_id)
        total_related = response.json()['total']
        print(str(total_related))

        assert_that(response.status_code, 200, 'Verify response status code of related a photo')
        assert_that(total_related, greater_than(0), 'Verify total of related of photo')

    if __name__ == '__main__':
        unittest.main()
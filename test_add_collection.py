import unittest
from hamcrest import assert_that
from helpers.collection_helper import CollectionHelper
from helpers.photo_helper import PhotoHelper


class AddCollectionTestCase(unittest.TestCase):
    def setUp(self):
        # Get photo
        self.photo_id = PhotoHelper.get_a_random_photo().json()['id']
        print('photo_id: ' + str(self.photo_id))
        # Create collection
        self.collection_id = CollectionHelper.create_collection('hien zzz', 'Siu nhon', 'true').json()['id']
        print('New collection: ' + str(self.collection_id))

    def test_add_a_photo_to_collection(self):
        # Add photo to collection
        response = CollectionHelper.add_photo_to_collection(self.collection_id, self.photo_id)

        actual_total_photo = response.json()['photo']['current_user_collections'][0]['total_photos']
        print('collection_current_add_photo: ' + str(actual_total_photo))

        assert_that(actual_total_photo, 1, 'Verify the collection total_photo')

    def tearDown(self):
        # Delete collection
        tear_down_response = CollectionHelper.delete_collection(self.collection_id)
        print('teardown: ' + str(tear_down_response.status_code))


if __name__ == '__main__':
    unittest.main()

import unittest
from hamcrest import assert_that, equal_to
from helpers.collection_helper import CollectionHelper
from helpers.photo_helper import PhotoHelper


class RemoveACollectionTestCase(unittest.TestCase):
    def setUp(self):
        # Get photo
        self.photo_id = PhotoHelper.get_a_random_photo().json()['id']
        print('photo_id: ' + str(self.photo_id))
        # Create collection
        self.collection_id = CollectionHelper.create_collection('hien zzz', 'Siu nhon', 'true').json()['id']
        print('New collection: ' + str(self.collection_id))

        # Add photo to collection
        response = CollectionHelper.add_photo_to_collection(self.collection_id, self.photo_id)
        actual_total_photo = response.json()['photo']['current_user_collections'][0]['total_photos']
        print('collection_current_add_photo: ' + str(actual_total_photo))

    def test_remove_a_photo_to_collection(self):
        # Remove photo to collection
        response = CollectionHelper.remove_photo_from_collection(self.collection_id, self.photo_id)
        print('Status code: ' + str(response))

        actual_total_photo = response.json()['collection']['total_photos']
        print('total photos: ' + str(actual_total_photo))
        assert_that(actual_total_photo, equal_to(0), 'Verify the collection total_photo')


if __name__ == '__main__':
    unittest.main()


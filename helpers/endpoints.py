#endpoint users
GET_USER_PROFILE_ENDPOINT = '/users/{}'

#end point Photos
GET_PHOTO_ENDPOINT = '/photos/{id}'
GET_A_PHOTO_INFOMATION_ENDPOINT = '/photos/{}'
GET_A_RANDOM_PHOTO_ENDPOINT = '/photos/random'
UNLIKE_AND_LIKE_A_PHOTO_ENDPOINT = '/photos/{id}/like'
GET_RELATED_PHOTOS_ENDPOINT = '/photos/{id}/related'
UPDATE_A_PHOTO_ENDPOINT = '/photos/{id}'

#end point collection
GET_COLLECTION_ENDPOINT = '/collections/{id}'
GET_COLLECTION_PHOTO_ENDPOINT = '/collections/{id}/photos'
CREATE_COLLECTION_ENDPOINT = '/collections'
COLLECTION_ID_ENDPOINT = '/collections/{id}'
# DELETE _ UPDATE
ADD_PHOTO_TO_COLLECTION_ENDPOINT = '/collections/{id}/add'
REMOVE_PHOTO_FROM_COLLECTION_ENDPOINT = '/collections/{id}/remove'
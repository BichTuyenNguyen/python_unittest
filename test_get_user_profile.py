import unittest
from hamcrest import assert_that, contains_string, equal_to
from helpers.user_helper import UserHelper


class TestCaseStringMethods(unittest.TestCase):
    def test_add_a_photo_to_collection(self):

        response = UserHelper.get_user_profile("mailchimp")
        first_name = response.json()['first_name']
        last_name = response.json()['last_name']

        if first_name is None:
            fullname = last_name
        elif last_name is None:
            fullname = first_name
        else:
            fullname = f"{first_name} {last_name}"

        assert_that(response.status_code, 200, 'Verify status')
        assert_that(fullname, equal_to("Mailchimp"), 'Verify the full name')


if __name__ == '__main__':
    unittest.main()

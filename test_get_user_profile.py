import unittest
from hamcrest import assert_that, equal_to
from helpers.user_helper import UserHelper


class GetUserProfileTestCase(unittest.TestCase):
    def test_get_username(self):

        response = UserHelper.get_user_profile("mailchimp")
        first_name = response.json()['first_name']
        last_name = response.json()['last_name']
        full_name = ""

        if first_name is None:
            full_name = last_name
        elif last_name is None:
            full_name = first_name
        else:
            full_name = f"{first_name} {last_name}"

        assert_that(response.status_code, 200, 'Verify status')
        assert_that(full_name, equal_to("Mailchimp"), 'Verify the full name')


if __name__ == '__main__':
    unittest.main()

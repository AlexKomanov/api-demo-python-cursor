from assertpy import assert_that
from test_data.jsonplaceholder_test_data import (
    EXPECTED_USER_COUNT,
    EXPECTED_USER_STRUCTURE,
    THIRD_USER_DATA
)

class TestJSONPlaceholderAPI:
    def test_users_status_code(self, jsonplaceholder_client):
        response = jsonplaceholder_client.get_users()
        assert_that(response.status_code).is_equal_to(200)

    def test_users_count(self, jsonplaceholder_client):
        response = jsonplaceholder_client.get_users()
        users = response.json()
        assert_that(len(users)).is_equal_to(EXPECTED_USER_COUNT)

    def test_first_user_structure(self, jsonplaceholder_client):
        response = jsonplaceholder_client.get_users()
        first_user = response.json()[0]
        
        for field, expected_type in EXPECTED_USER_STRUCTURE.items():
            assert_that(first_user).contains_key(field)
            assert_that(first_user[field]).is_instance_of(expected_type)

    def test_third_user_data(self, jsonplaceholder_client):
        response = jsonplaceholder_client.get_user(3)
        user = response.json()
        
        for field, expected_value in THIRD_USER_DATA.items():
            assert_that(user[field]).is_equal_to(expected_value) 
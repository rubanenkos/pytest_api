import pytest
from constants.routes import Routes
from logger_config import setup_logger
from assertions.assertion_base import AssertionBase as Verify
from client.api import Api

logger = setup_logger()


class TestMainCrud:
    def test_get_list_of_users(self):
        response = Api.request("GET", Routes.USERS)
        Verify.validate_status_code(response, 200)

    @pytest.mark.parametrize("user_id", [
        2, 3
    ])
    def test_get_single_user(self, user_id):
        response = Api.request("GET", f"{Routes.USERS}/{user_id}")
        Verify.validate_status_code(response, 200)
        Verify.validate_schema(response, "get_single_user.json")

    def test_create_new_user(self):
        data = {
            "name": "Paul Oliver",
            "movies": ["Terminator", "Asteroid"]
        }
        response = Api.request("POST", Routes.USERS, data=data)
        logger.info(f"Response Body: {response.json()}")
        Verify.validate_status_code(response, 201)

    def test_update_user(self):
        data = {
            "name": "Paulo Updated"
        }
        response = Api.request("PUT", f"{Routes.USERS}/2", data=data)
        logger.info(f"Response Body: {response.json()}")
        Verify.validate_status_code(response, 200)

    def test_delete_user(self):
        response = Api.request("DELETE", f"{Routes.USERS}/2")
        Verify.validate_status_code(response, 204)

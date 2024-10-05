import requests

from constants.routes import Routes
from logger_config import setup_logger

logger = setup_logger()


def test_get_list_of_users():
    url = Routes.USERS
    response = requests.get(url)
    logger.info(f"Request URL: {url}")
    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.json()}")
    assert response.status_code == 200

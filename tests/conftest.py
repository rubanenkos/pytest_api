import pytest
import requests


@pytest.fixture(scope="session")
def api_session():
    url = "https://example.com/api/login"
    data = {"username": "myuser", "password": "mypassword"}
    response = requests.post(url, data=data)
    assert response.status_code == 200
    session = requests.Session()
    session.headers.update({"Authorization": f"Bearer {response.json()['access_token']}"})
    yield session

import logging

import pytest
import requests
from faker import Faker

logger = logging.getLogger("api")


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="http://localhost:56733",
    ),


faker = Faker()



@pytest.fixture(scope="session")
def url(request):
    url_api = request.config.getoption("--api-url")
    return url_api


@pytest.fixture
def regsiter() -> dict:
    body = {"username": faker.email(), "password": faker.password()}
    response = requests.post(url=f'{"http://localhost:56733"}/register', json=body)
    assert response.status_code == 201
    return body
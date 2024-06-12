import logging

import pytest
import requests
from faker import Faker


logger = logging.getLogger('api')

URL = "http://localhost:56733"


faker = Faker()


def pytest_addoption(parser):
    parser.addoption("--api-url", action="store", default="http://localhost:56733",
                     help="API url")


@pytest.fixture(scope='session')
def url(request):
    url = request.config.getoption("--api-url")
    logger.info(f'Start tests, url is {url}')
    return url

@pytest.fixture
def regsiter() -> dict:
    body = {"username": faker.email(), "password": faker.password()}
    response = requests.post(url=f'{URL}/register', json=body)
    assert response.status_code == 201
    return body
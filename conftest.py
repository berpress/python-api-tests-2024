import pytest
import requests
from faker import Faker


URL = "http://localhost:56733"


faker = Faker()



@pytest.fixture
def regsiter() -> dict:
    body = {"username": faker.email(), "password": faker.password()}
    response = requests.post(url=f'{URL}/register', json=body)
    assert response.status_code == 201
    return body
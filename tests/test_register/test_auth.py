import requests
from faker import Faker

URL = "http://localhost:56733"


faker = Faker()

class TestAuth:
    def test_auth_valid_data(self, regsiter):
        """
        1. Try to register new user
        2. Check that status code 201
        3. Check response
        """
        # 2
        response_auth = requests.post(url=f'{URL}/auth', json=regsiter)
        assert response_auth.status_code == 200

        pass
        # assert response.status_code == 201
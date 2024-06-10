import pytest
import requests
from faker import Faker

URL = "http://localhost:56733"

faker = Faker()


class TestRegister:
    def test_register_valid_data(self):
        """
        1. Try to register new user
        2. Check that status code 201
        3. Check response
        """
        body = {"username": faker.email(), "password": faker.password()}
        response = requests.post(url=f'{URL}/register', json=body)
        assert response.status_code == 201

        # существуют
        assert response.json()['message']
        assert response.json()['uuid']
        # типы
        assert isinstance(response.json()['message'], str)
        assert isinstance(response.json()['uuid'], int)


    @pytest.mark.skip(reason='1234')
    @pytest.mark.parametrize('username', ['test@test', 'test', 1234, True])
    def test_register_invalid_username(self, username):
        """
        1. Try to register new user with invalid username
        2. Check that status code 400
        3. Check response
        """
        body = {"username": username, "password": faker.password()}
        response = requests.post(url=f'{URL}/register', json=body)
        assert response.status_code == 400

    @pytest.mark.skip(reason='1234')
    @pytest.mark.parametrize('password', ['test@test', 'test', 1234, True])
    def test_register_invalid_password(self, password):
        """
        1. Try to register new user with invalid password
        2. Check that status code 400
        3. Check response
        """
        body = {"username": faker.email(), "password": password}
        response = requests.post(url=f'{URL}/register', json=body)
        assert response.status_code == 201

    def test_register_empty_username(self, username=None):
        """
        1. Try to register new user with empty username
        2. Check that status code 400
        3. Check response
        """
        body = {"username": username, "password": faker.password()}
        response = requests.post(url=f'{URL}/register', json=body)
        assert response.status_code == 400
        assert response.json()['message'] == 'Username and password are required fields'

    def test_register_empty_password(self, password=None):
        """
        1. Try to register new user with empty password
        2. Check that status code 400
        3. Check response
        """
        body = {"username": faker.email(), "password": password}
        response = requests.post(url=f'{URL}/register', json=body)
        assert response.status_code == 400
        assert response.json()['message'] == 'Username and password are required fields'

    def test_register_len_password(self):
        """
        1. Try to register new user with len password
        2. Check that status code 200
        3. Check response
        """
        pass

    def test_double_register_valid_data(self):
        """
        1. Try to double register new user
        2. Check that status code 400
        3. Check response
        """
        body = {"username": faker.email(), "password": faker.password()}
        response_1 = requests.post(url=f'{URL}/register', json=body)
        assert response_1.status_code == 201
        response_2 = requests.post(url=f'{URL}/register', json=body)
        assert response_2.status_code == 400
        assert response_2.json()['message'] == 'A user with that username already exists'


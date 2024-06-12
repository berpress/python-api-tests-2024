from common.requests_logger import requests_logger
from fixtures.endpoints.register.schema import REGISTER_SCHEMA
from fixtures.request import Client


class Register:
    _POST_REGISTER = '/register'

    def __init__(self, url: str):
        self.client = Client()
        self.url = url

    def register_user(self, body: dict, schema=REGISTER_SCHEMA):
        res = self.client.request('POST', f'{self.url}{self._POST_REGISTER}',
                                   json=body)
        schema.validate(res.json())
        requests_logger(res)
        return res


from common.requests_logger import requests_logger
from fixtures.http_client import Client
from fixtures.register.schema import REGISTER_SCHEMA


class Register:
    def __init__(self, url):
        self.client = Client()
        self.url = url

    _POST_REGISTER = 'register'

    def register(self, body: dict, schema=REGISTER_SCHEMA):
        res = self.client.request('POST',
                                   f'{self.url}/{self._POST_REGISTER}',
                                   json=body)
        schema.validate(res.json())
        requests_logger(res)
        return res

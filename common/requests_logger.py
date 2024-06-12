import logging

logger = logging.getLogger("api")


def requests_logger(response):
    logger.info(f"Request: url: {response.request.url}, method: "
                f"{response.request.method}, body: {response.request.body.decode('utf-8')}")
    logger.info(f"Response: status code: {response.status_code} "
                f"method: "
                f"{response.request.method}, body: {response.json()}")

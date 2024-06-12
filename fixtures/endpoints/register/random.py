from faker import Faker

faker = Faker()

def random_register() -> dict:
    return {"username": faker.email(), "password": faker.password()}
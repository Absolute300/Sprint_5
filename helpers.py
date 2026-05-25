from faker import Faker

faker = Faker()

def generate_random_credentials():
    name = faker.name()
    email = faker.email()
    password = faker.password(length=10, special_chars=True, digits=True)
    return name, email, password

def generate_invalid_password():
    name = faker.name()
    email = faker.email()
    invalid_password = faker.password(length=5, special_chars=True, digits=True)
    return name, email, invalid_password
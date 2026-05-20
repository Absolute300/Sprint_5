import random
import string


def generate_email(
    firstname: str = "ilyha",
    lastname: str = "tikhonov",
    cohort: str = "045",
    domain: str = "yandex.ru",
) -> str:
    suffix = "".join(random.choices(string.digits, k=3))
    return f"{firstname}_{lastname}_{cohort}_{suffix}@{domain}"


def generate_password(min_length: int = 6) -> str:
    length = max(8, min_length)
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=length))


def generate_name() -> str:
    return "Ilyha Tikhonov"
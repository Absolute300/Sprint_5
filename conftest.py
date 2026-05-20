import pytest
from selenium import webdriver

from data_generators import generate_email, generate_name, generate_password
from locators.main_locators import MainLocators
from pages.account_page import AccountPage
from pages.auth_page import AuthPage
from pages.main_page import MainPage


@pytest.fixture
def driver():
    driver_instance = webdriver.Chrome()

    yield driver_instance
    driver_instance.quit()


@pytest.fixture
def user_credentials():
    return {
        "name": generate_name(),
        "email": generate_email(firstname="ilyha", lastname="tikhonov", cohort="045"),
        "password": generate_password(6),
    }


@pytest.fixture
def auth_page(driver):
    return AuthPage(driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def account_page(driver):
    return AccountPage(driver)


@pytest.fixture(scope="session")
def registered_user():
    return {
        "name": "Ilyha Tikhonov",
        "email": "Il__tikhonov045_test@yandex.ru",
        "password": "tests9876",
    }


@pytest.fixture
def authorized_user(auth_page, registered_user):
    auth_page.open_login()
    auth_page.login(registered_user["email"], registered_user["password"])
    auth_page.wait_url_contains("/")
    assert auth_page.is_visible(MainLocators.MAIN_TITLE, timeout=8)
    return registered_user
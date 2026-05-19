from selenium import webdriver
import pytest
from data import Url


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Url.main_page)
    yield driver
    driver.quit()
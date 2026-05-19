from data import Data, Url, RandomUser
import pytest
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:
    #Успешная регистрация
    def test_registration_success(self, driver):
        driver.get(Url.registration_page)
        driver.find_element(*Locators.input_name).send_keys(RandomUser.name)
        driver.find_element(*Locators.input_email).send_keys(RandomUser.email)
        driver.find_element(*Locators.input_password).send_keys(RandomUser.password)
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.header_login))
        assert driver.find_element(*Locators.header_login).text == 'Вход'
from helpers import generate_random_credentials, generate_invalid_password
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from url import MAIN_URL
from locators import Registration_Locators

class TestRegister:

    def test_successful_registration(self, driver):
        
        name, email, password = generate_random_credentials()

        driver.get(MAIN_URL)
        
        driver.find_element(*Registration_Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Registration_Locators.REGISTER_LINK))
        
        driver.find_element(*Registration_Locators.REGISTER_LINK).click()

        driver.find_element(*Registration_Locators.NAME_FIELD).send_keys(name)
        driver.find_element(*Registration_Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Registration_Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Registration_Locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Registration_Locators.LOGIN_BUTTON))

        driver.find_element(*Registration_Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Registration_Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Registration_Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Registration_Locators.ORDER_BUTTON))
        
        assert driver.current_url == MAIN_URL

    
    def test_registration_invalid_password(self, driver):
        
        name, email, invalid_password = generate_invalid_password()

        driver.get(MAIN_URL)
        
        driver.find_element(*Registration_Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Registration_Locators.REGISTER_LINK))
        
        driver.find_element(*Registration_Locators.REGISTER_LINK).click()

        driver.find_element(*Registration_Locators.NAME_FIELD).send_keys(name)
        driver.find_element(*Registration_Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Registration_Locators.PASSWORD_FIELD).send_keys(invalid_password)
        driver.find_element(*Registration_Locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Registration_Locators.INCORRECT_PASSWORD_MESSAGE))

        assert "Некорректный пароль" in driver.find_element(*Registration_Locators.INCORRECT_PASSWORD_MESSAGE).text
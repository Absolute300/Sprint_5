from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from url import MAIN_URL
from locators import Registration_Locators


class TestLogout:
    
    # Выход из аккаунта
    def test_logout(self, driver):    

        driver.get(MAIN_URL)

        driver.find_element(*Registration_Locators.LOGIN_MAIN_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Registration_Locators.REGISTER_LINK))

        driver.find_element(*Registration_Locators.EMAIL_FIELD).send_keys(Credentials.email)
        driver.find_element(*Registration_Locators.PASSWORD_FIELD).send_keys(Credentials.password)
        driver.find_element(*Registration_Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Registration_Locators.ORDER_BUTTON))

        driver.find_element(*Registration_Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Registration_Locators.PROFILE))

        driver.find_element(*Registration_Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Registration_Locators.LOGIN_BUTTON))

        assert driver.find_element(*Registration_Locators.LOGIN_BUTTON).is_displayed()
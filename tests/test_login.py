from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from url import MAIN_URL
from locators import Registration_Locators


class TestLogin:
    
    # Вход по кнопке «Войти в аккаунт» на главной странице
    def test_login_main_button(self, driver):    

        driver.get(MAIN_URL)

        driver.find_element(*Registration_Locators.LOGIN_MAIN_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Registration_Locators.REGISTER_LINK))

        driver.find_element(*Registration_Locators.EMAIL_FIELD).send_keys(Credentials.email)
        driver.find_element(*Registration_Locators.PASSWORD_FIELD).send_keys(Credentials.password)
        driver.find_element(*Registration_Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Registration_Locators.ORDER_BUTTON))

        assert driver.find_element(*Registration_Locators.ORDER_BUTTON).is_displayed()

    
    # Вход через кнопку «Личный кабинет»
    def test_login_personal_account_button(self, driver):    

        driver.get(MAIN_URL)

        driver.find_element(*Registration_Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Registration_Locators.REGISTER_LINK))

        driver.find_element(*Registration_Locators.EMAIL_FIELD).send_keys(Credentials.email)
        driver.find_element(*Registration_Locators.PASSWORD_FIELD).send_keys(Credentials.password)
        driver.find_element(*Registration_Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Registration_Locators.ORDER_BUTTON))

        assert driver.find_element(*Registration_Locators.ORDER_BUTTON).is_displayed()
    

    # Вход через кнопку в форме регистрации
    def test_login_link_registration(self, driver):    

        driver.get(MAIN_URL)

        driver.find_element(*Registration_Locators.LOGIN_MAIN_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Registration_Locators.REGISTER_LINK))
        driver.find_element(*Registration_Locators.REGISTER_LINK).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Registration_Locators.REGISTER_BUTTON))
        driver.find_element(*Registration_Locators.LOGIN_LINK_REGISTRATION).click()

        driver.find_element(*Registration_Locators.EMAIL_FIELD).send_keys(Credentials.email)
        driver.find_element(*Registration_Locators.PASSWORD_FIELD).send_keys(Credentials.password)
        driver.find_element(*Registration_Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Registration_Locators.ORDER_BUTTON))

        assert driver.find_element(*Registration_Locators.ORDER_BUTTON).is_displayed()


    # Вход через кнопку в форме восстановления пароля
    def test_login_recovery_password_link(self, driver):    

        driver.get(MAIN_URL)

        driver.find_element(*Registration_Locators.LOGIN_MAIN_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Registration_Locators.REGISTER_LINK))
        driver.find_element(*Registration_Locators.FORGOT_PASSWORD_LINK).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Registration_Locators.LOGIN_LINK_REGISTRATION))
        driver.find_element(*Registration_Locators.LOGIN_LINK_REGISTRATION).click()

        driver.find_element(*Registration_Locators.EMAIL_FIELD).send_keys(Credentials.email)
        driver.find_element(*Registration_Locators.PASSWORD_FIELD).send_keys(Credentials.password)
        driver.find_element(*Registration_Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Registration_Locators.ORDER_BUTTON))

        assert driver.find_element(*Registration_Locators.ORDER_BUTTON).is_displayed()
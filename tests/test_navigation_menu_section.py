from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from url import MAIN_URL
from locators import Registration_Locators


class TestNavigationMenuSection:

    def switch_to_section(self, driver, section_locator, expected_text):
        """Универсальный метод переключения между разделами."""
        section_element = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(section_locator)
        )
        section_element.click()
        WebDriverWait(driver, 15).until(
            EC.text_to_be_present_in_element(Registration_Locators.SELECTED_SECTION, expected_text)
        )
    
    # Переход из раздела «Булки» в раздел «Соусы»
    def test_buns_to_sauces(self, driver):    

        driver.get(MAIN_URL)

        driver.find_element(*Registration_Locators.LOGIN_MAIN_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Registration_Locators.REGISTER_LINK))

        driver.find_element(*Registration_Locators.EMAIL_FIELD).send_keys(Credentials.email)
        driver.find_element(*Registration_Locators.PASSWORD_FIELD).send_keys(Credentials.password)
        driver.find_element(*Registration_Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Registration_Locators.ORDER_BUTTON))

    
        # Переходим на вкладку «Соусы»
        self.switch_to_section(driver, Registration_Locators.SAUCES_SECTION, "Соусы")

        # Ассерт: проверяем, что активный раздел — «Соусы»
        active_section = driver.find_element(*Registration_Locators.SELECTED_SECTION).text
        assert active_section == "Соусы", f"Ожидался раздел 'Соусы', но отображается '{active_section}'"


    # Переход из раздела «Соусы» в раздел «Начинки»
    def test_sauces_to_filling(self, driver):    

        driver.get(MAIN_URL)

        driver.find_element(*Registration_Locators.LOGIN_MAIN_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Registration_Locators.REGISTER_LINK))

        driver.find_element(*Registration_Locators.EMAIL_FIELD).send_keys(Credentials.email)
        driver.find_element(*Registration_Locators.PASSWORD_FIELD).send_keys(Credentials.password)
        driver.find_element(*Registration_Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Registration_Locators.ORDER_BUTTON))

                # Сначала убеждаемся, что мы на «Соусы»
        self.switch_to_section(driver, Registration_Locators.SAUCES_SECTION, "Соусы")
        # Затем переходим на «Начинки»
        self.switch_to_section(driver, Registration_Locators.FILLING_SECTION, "Начинки")    

         # Ассерт: проверяем, что сейчас активен раздел «Начинки»
        active_section = driver.find_element(*Registration_Locators.SELECTED_SECTION).text
        assert active_section == "Начинки", f"Ожидался раздел 'Начинки', но отображается '{active_section}'"
    
    # Переход из раздела «Начинки» в раздел «Булки» 
    def test_filling_to_buns(self, driver):    

        driver.get(MAIN_URL)

        driver.find_element(*Registration_Locators.LOGIN_MAIN_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Registration_Locators.REGISTER_LINK))

        driver.find_element(*Registration_Locators.EMAIL_FIELD).send_keys(Credentials.email)
        driver.find_element(*Registration_Locators.PASSWORD_FIELD).send_keys(Credentials.password)
        driver.find_element(*Registration_Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Registration_Locators.ORDER_BUTTON))

                # Сначала переходим на «Начинки»
        self.switch_to_section(driver, Registration_Locators.FILLING_SECTION, "Начинки")
        # Затем на «Булки»
        self.switch_to_section(driver, Registration_Locators.BUNS_SECTION, "Булки")

        # Ассерт: проверяем, что вернулись к разделу «Булки»
        active_section = driver.find_element(*Registration_Locators.SELECTED_SECTION).text
        assert active_section == "Булки", f"Ожидался раздел 'Булки', но отображается '{active_section}'"
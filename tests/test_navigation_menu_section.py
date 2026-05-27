from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from url import MAIN_URL
from locators import Registration_Locators


class TestNavigationMenuSection:

    def switch_to_section(self, driver, section_locator, expected_text):
        section_element = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(section_locator)
        )

        # Прокручиваем
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", section_element)

        # Кликаем через JS — минуя физический клик
        driver.execute_script("arguments[0].click();", section_element)

        WebDriverWait(driver, 15).until(
            EC.text_to_be_present_in_element(Registration_Locators.SELECTED_SECTION, expected_text)
        )

    # Переход из раздела «Булки» в раздел «Соусы»
    def test_buns_to_sauces(self, driver):    

        driver.get(MAIN_URL)
    
        # Переходим на вкладку «Соусы»
        self.switch_to_section(driver, Registration_Locators.SAUCES_SECTION, "Соусы")

        # Ассерт: проверяем, что активный раздел — «Соусы»
        active_section = driver.find_element(*Registration_Locators.SELECTED_SECTION).text
        assert active_section == "Соусы", f"Ожидался раздел 'Соусы', но отображается '{active_section}'"


    # Переход из раздела «Соусы» в раздел «Начинки»
    def test_sauces_to_filling(self, driver):  
              
        driver.get(MAIN_URL)  

                # Прямой переход: Булки → Соусы → Начинки
        self.switch_to_section(driver, Registration_Locators.BUNS_SECTION, "Булки")
        self.switch_to_section(driver, Registration_Locators.FILLING_SECTION, "Начинки")


         # Ассерт: проверяем, что сейчас активен раздел «Начинки»
        active_section = driver.find_element(*Registration_Locators.SELECTED_SECTION).text
        assert active_section == "Начинки", f"Ожидался раздел 'Начинки', но отображается '{active_section}'"
    
    # Переход из раздела «Начинки» в раздел «Булки» 
    def test_filling_to_buns(self, driver):    

        driver.get(MAIN_URL)

                # Сначала переходим на «Начинки»
        self.switch_to_section(driver, Registration_Locators.FILLING_SECTION, "Начинки")
        # Затем на «Соус»
        self.switch_to_section(driver, Registration_Locators. BUNS_SECTION, "Булки")

        # Ассерт: проверяем, что вернулись к разделу «Соус»
        active_section = driver.find_element(*Registration_Locators.SELECTED_SECTION).text
        assert active_section == "Булки", f"Ожидался раздел 'Булки', но отображается '{active_section}'"
from config import MAIN_PAGE
from locators.constructor_locators import ConstructorLocators
from locators.header_locators import HeaderLocators
from locators.main_locators import MainLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def open_main(self):
        self.open(MAIN_PAGE)
        self.wait_visible(MainLocators.MAIN_TITLE)

    def click_login_button(self):
        self.click(MainLocators.LOGIN_TO_ACCOUNT_BUTTON)

    def click_personal_account(self):
        self.click(HeaderLocators.PERSONAL_ACCOUNT_LINK)

    def click_constructor(self):
        self.click(HeaderLocators.CONSTRUCTOR_LINK)

    def click_logo(self):
        self.click(HeaderLocators.LOGO_LINK)

    def open_tab_buns(self):
        self.click(ConstructorLocators.BUNS_TAB)
        return self.wait_clickable(ConstructorLocators.BUNS_TAB)

    def open_tab_sauces(self):
        self.click(ConstructorLocators.SAUCES_TAB)
        return self.wait_clickable(ConstructorLocators.SAUCES_TAB)

    def open_tab_fillings(self):
        self.click(ConstructorLocators.FILLINGS_TAB)
        return self.wait_clickable(ConstructorLocators.FILLINGS_TAB)
from config import FORGOT_PASSWORD_PAGE, LOGIN_PAGE, REGISTER_PAGE
from locators.auth_locators import AuthLocators
from pages.base_page import BasePage


class AuthPage(BasePage):
    def open_login(self):
        self.open(LOGIN_PAGE)
        self.wait_visible(AuthLocators.LOGIN_TITLE)

    def open_register(self):
        self.open(REGISTER_PAGE)
        self.wait_visible(AuthLocators.REGISTER_TITLE)

    def open_forgot_password(self):
        self.open(FORGOT_PASSWORD_PAGE)
        self.wait_visible(AuthLocators.FORGOT_PASSWORD_TITLE)

    def login(self, email: str, password: str):
        self.type(AuthLocators.LOGIN_EMAIL_INPUT, email)
        self.type(AuthLocators.LOGIN_PASSWORD_INPUT, password)
        self.click(AuthLocators.LOGIN_SUBMIT_BUTTON)

    def register(self, name: str, email: str, password: str):
        self.type(AuthLocators.REGISTER_NAME_INPUT, name)
        self.type(AuthLocators.REGISTER_EMAIL_INPUT, email)
        self.type(AuthLocators.REGISTER_PASSWORD_INPUT, password)
        self.click(AuthLocators.REGISTER_SUBMIT_BUTTON)

    def go_to_register_from_login(self):
        self.click(AuthLocators.REGISTER_LINK_ON_LOGIN)
        self.wait_visible(AuthLocators.REGISTER_TITLE)

    def go_to_forgot_from_login(self):
        self.click(AuthLocators.FORGOT_LINK_ON_LOGIN)
        self.wait_visible(AuthLocators.FORGOT_PASSWORD_TITLE)

    def go_to_login_from_register(self):
        self.click(AuthLocators.LOGIN_LINK_ON_REGISTER)
        self.wait_visible(AuthLocators.LOGIN_TITLE)

    def go_to_login_from_forgot(self):
        self.click(AuthLocators.LOGIN_LINK_ON_FORGOT)
        self.wait_visible(AuthLocators.LOGIN_TITLE)
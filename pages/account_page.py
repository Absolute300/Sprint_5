from locators.account_locators import AccountLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    def assert_account_opened(self):
        self.wait_url_contains("/account")
        return self.wait_visible(AccountLocators.ACCOUNT_PROFILE_TEXT).is_displayed()

    def logout(self):
        self.click(AccountLocators.LOGOUT_BUTTON)
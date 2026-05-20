from locators.auth_locators import AuthLocators
from locators.main_locators import MainLocators


class TestNavigation:
    def test_open_personal_account_from_header(self, main_page, account_page, authorized_user):
        # Проверяет переход в личный кабинет по клику в шапке.
        main_page.click_personal_account()
        assert account_page.assert_account_opened()

    def test_return_to_constructor_from_account_via_constructor_link(self, main_page, account_page, authorized_user):
        # Проверяет возврат из личного кабинета в конструктор по ссылке "Конструктор".
        main_page.click_personal_account()
        assert account_page.assert_account_opened()
        main_page.click_constructor()
        main_page.wait_url_contains("/")
        assert main_page.wait_visible(MainLocators.MAIN_TITLE).is_displayed()

    def test_return_to_constructor_from_account_via_logo(self, main_page, account_page, authorized_user):
        # Проверяет возврат из личного кабинета в конструктор по логотипу.
        main_page.click_personal_account()
        assert account_page.assert_account_opened()
        main_page.click_logo()
        main_page.wait_url_contains("/")
        assert main_page.wait_visible(MainLocators.MAIN_TITLE).is_displayed()

    def test_logout_from_personal_account(self, main_page, account_page, authorized_user):
        # Проверяет выход из аккаунта по кнопке "Выход".
        main_page.click_personal_account()
        assert account_page.assert_account_opened()
        account_page.logout()
        account_page.wait_url_contains("/login")
        assert account_page.wait_visible(AuthLocators.LOGIN_TITLE).is_displayed()
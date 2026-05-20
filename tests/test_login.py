from locators.main_locators import MainLocators


class TestLogin:
    def test_login_via_main_page_button_success(self, main_page, auth_page, registered_user):
        # Проверяет вход через кнопку "Войти в аккаунт" на главной.
        main_page.open_main()
        main_page.click_login_button()
        auth_page.login(registered_user["email"], registered_user["password"])
        auth_page.wait_url_contains("/")
        assert auth_page.wait_visible(MainLocators.MAIN_TITLE).is_displayed()

    def test_login_via_personal_account_button_success(self, main_page, auth_page, registered_user):
        # Проверяет вход через переход из "Личного кабинета".
        main_page.open_main()
        main_page.click_personal_account()
        auth_page.login(registered_user["email"], registered_user["password"])
        auth_page.wait_url_contains("/")
        assert auth_page.wait_visible(MainLocators.MAIN_TITLE).is_displayed()

    def test_login_via_register_page_link_success(self, auth_page, registered_user):
        # Проверяет вход через ссылку "Войти" со страницы регистрации.
        auth_page.open_login()
        auth_page.go_to_register_from_login()
        auth_page.go_to_login_from_register()
        auth_page.login(registered_user["email"], registered_user["password"])
        auth_page.wait_url_contains("/")
        assert auth_page.wait_visible(MainLocators.MAIN_TITLE).is_displayed()

    def test_login_via_forgot_password_page_link_success(self, auth_page, registered_user):
        # Проверяет вход через ссылку "Войти" со страницы восстановления пароля.
        auth_page.open_login()
        auth_page.go_to_forgot_from_login()
        auth_page.go_to_login_from_forgot()
        auth_page.login(registered_user["email"], registered_user["password"])
        auth_page.wait_url_contains("/")
        assert auth_page.wait_visible(MainLocators.MAIN_TITLE).is_displayed()
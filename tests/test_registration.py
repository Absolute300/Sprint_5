from locators.auth_locators import AuthLocators


class TestRegistration:
    def test_registration_with_valid_data_redirects_to_login(
        self, auth_page, user_credentials
    ):
        # Проверяет успешную регистрацию и редирект на страницу входа.
        auth_page.open_register()
        auth_page.register(
            name=user_credentials["name"],
            email=user_credentials["email"],
            password=user_credentials["password"],
        )
        auth_page.wait_url_contains("/login")
        assert auth_page.wait_visible(AuthLocators.LOGIN_TITLE).text == "Вход"

    def test_registration_with_short_password_shows_validation_error(
        self, auth_page, user_credentials
    ):
        # Проверяет ошибку валидации для короткого пароля при регистрации.
        auth_page.open_register()
        auth_page.register(
            name=user_credentials["name"],
            email=user_credentials["email"],
            password="12345",
        )
        assert auth_page.wait_visible(
            AuthLocators.INVALID_PASSWORD_ERROR
        ).is_displayed()

    def test_registration_with_empty_name_does_not_create_user(
        self, auth_page, user_credentials
    ):
        # Проверяет, что поле "Имя" обязательно не пустое
        auth_page.open_register()
        auth_page.register(
            name="",
            email=user_credentials["email"],
            password=user_credentials["password"],
        )
        assert "/register" in auth_page.driver.current_url
        assert auth_page.wait_visible(AuthLocators.REGISTER_TITLE).is_displayed()
        assert not auth_page.is_visible(AuthLocators.LOGIN_TITLE, timeout=2)
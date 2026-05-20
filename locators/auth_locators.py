from selenium.webdriver.common.by import By


class AuthLocators:
    # Заголовок страницы "Вход"
    LOGIN_TITLE = (By.XPATH, "//h2[text()='Вход']")
    # Поле email на странице входа
    LOGIN_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Поле пароля на странице входа
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input[@type='password']")
    # Кнопка "Войти"
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # Ссылка "Зарегистрироваться" на странице входа
    REGISTER_LINK_ON_LOGIN = (By.LINK_TEXT, "Зарегистрироваться")
    # Ссылка "Восстановить пароль" на странице входа
    FORGOT_LINK_ON_LOGIN = (By.LINK_TEXT, "Восстановить пароль")

    # Заголовок страницы "Регистрация"
    REGISTER_TITLE = (By.XPATH, "//h2[text()='Регистрация']")
    # Поле "Имя" на регистрации
    REGISTER_NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    # Поле "Email" на регистрации
    REGISTER_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Поле "Пароль" на регистрации
    REGISTER_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input[@type='password']")
    # Кнопка "Зарегистрироваться"
    REGISTER_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # Ссылка "Войти" на странице регистрации
    LOGIN_LINK_ON_REGISTER = (By.LINK_TEXT, "Войти")
    # Ошибка короткого/некорректного пароля
    INVALID_PASSWORD_ERROR = (By.XPATH, "//*[contains(text(),'Некорректный пароль')]")

    # Заголовок страницы "Восстановление пароля"
    FORGOT_PASSWORD_TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")
    # Поле email на странице восстановления
    FORGOT_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Кнопка "Восстановить"
    FORGOT_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    # Ссылка "Войти" на странице восстановления
    LOGIN_LINK_ON_FORGOT = (By.LINK_TEXT, "Войти")
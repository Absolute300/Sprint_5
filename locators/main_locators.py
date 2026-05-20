from selenium.webdriver.common.by import By


class MainLocators:
    # Главный заголовок страницы конструктора
    MAIN_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    # Кнопка "Войти в аккаунт" на главной
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
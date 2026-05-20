from selenium.webdriver.common.by import By


class AccountLocators:
    # Кнопка "Выход" в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    # Маркер того, что открыт профиль
    ACCOUNT_PROFILE_TEXT = (By.XPATH, "//*[contains(text(),'Профиль')]")
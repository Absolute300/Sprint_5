from selenium.webdriver.common.by import By


class HeaderLocators:
    # Ссылка "Личный кабинет" в шапке
    PERSONAL_ACCOUNT_LINK = (By.CSS_SELECTOR, "header a[href='/account']")
    # Ссылка "Конструктор" в шапке
    CONSTRUCTOR_LINK = (By.LINK_TEXT, "Конструктор")
    # Логотип Stellar Burgers (ведет на главную)
    LOGO_LINK = (By.CSS_SELECTOR, "div[class*='header__logo'] a")
from selenium.webdriver.common.by import By

class Registration_Locators:
    
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")  # Кнопка «Личный кабинет»
    LOGIN_MAIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]") # Кнопка «Войти в аккаунт»
    REGISTER_LINK = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]") # Ссылка «Зарегистрироваться»

    NAME_FIELD = (By.XPATH, "//label[text()='Имя']/following-sibling::input") # Поле «Имя» на странице регистрации
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input") # Поле «Email» на странице регистрации
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']") # Поле «Пароль» на странице регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]") # Кнопка «Зарегистрироваться»
    
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]") # Кнопка «Войти»
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]") # Ссылка «Восстановить пароль»

    INCORRECT_PASSWORD_MESSAGE = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]") # Сообщение «Некорректный пароль»

    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]") # Кнопка «Оформить заказ»

    LOGIN_LINK_REGISTRATION = (By.XPATH, "//a[contains(text(), 'Войти')]") # Ссылка «Войти» в форме регистрации

    RECOVERY_PASSWORD_LINK = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]") # Ссылка «Восстановить пароль»

    PROFILE = (By.XPATH, "//a[contains(text(), 'Профиль')]") # Раздел Профиль

    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]") # Кнопка «Конструктор» в шапке сайта
    LOGO_BUTTON = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']") # Лого в шапке сайта

    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]") # Кнопка «Выход»

    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/ancestor::div[contains(@class, 'tab_tab')]")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/ancestor::div[contains(@class, 'tab_tab')]")
    FILLING_SECTION = (By.XPATH, "//span[text()='Начинки']/ancestor::div[contains(@class, 'tab_tab')]")
    SELECTED_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span")
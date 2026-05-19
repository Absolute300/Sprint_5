from selenium.webdriver.common.by import By


class Locators:
    login_button_main_page = By.XPATH, './/button[text()="Войти в аккаунт"]' #Кнопка "Войти в аккаунт" на главной странице
    input_email = By.XPATH, './/label[text() = "Email"]/following-sibling::input' #Поле ввода Email
    input_password = By.XPATH, './/label[text() = "Пароль"]/following-sibling::input' #Поле ввода Пароль
    login_button_login_page = By.XPATH, './/button[text() = "Войти"]' #Кнопка "Войти" на странице входа
    registration_button = By.XPATH, './/button[text() = "Зарегистрироваться"]' #Кнопка "Зарегистрироваться"
    input_name = By.XPATH, './/label[text() = "Имя"]/following-sibling::input' #Поле ввода Имя
    header_login = By.XPATH, './/h2[text() = "Вход"]' #Заголовок "Вход"
    header_registration = By.XPATH, './/h2[text() = "Регистрация"]' #Заголовок "Регистрация"
    header_incorrect_password = By.XPATH, './/p[text() = "Некорректный пароль"]' #Сообщение об ошибке "Некорректный пароль"
    header_exist_user = By.XPATH, './/p[text() = "Такой пользователь уже существует"]' #Сообщение об ошибке "Такой пользователь уже существует"
    order_button = By.XPATH, './/button[text() = "Оформить заказ"]' #Кнопка "Оформить заказ"
    account_button = By.XPATH, './/p[text() = "Личный Кабинет"]' #Кнопка "Личный кабинет"
    login_button_registration_page = By.XPATH, './/a[text() = "Войти"]' #Кнопка "Войти" на странице регистрации
    forgot_password_button = By.XPATH, './/a[text() = "Восстановить пароль"]' #Кнопка "Восстановить пароль"
    recovery_button = By.XPATH, './/button[text() = "Восстановить"]' #Кнопка "Восстановить"
    header_profile = By.XPATH, './/a[text() = "Профиль"]' #Заголовок "Профиль"
    constructor_button = By.XPATH, './/p[text() = "Конструктор"]' #Кнопка "Конструктор"
    logo = By.XPATH, './/*[@href = "/"]' #Логотип
    pack_burger = By.XPATH, './/h1[text() = "Соберите бургер"]' #Заголовок "Соберите бургер"
    logout_button = By.XPATH, './/button[text() = "Выход"]' #Кнопка "Выход"
    sauces_span = By.XPATH, './/span[text() = "Соусы"]' #Раздел "Соусы"
    fil_span = By.XPATH, './/span[text() = "Начинки"]' #Раздел "Начинки"
    buns_span = By.XPATH, './/span[text() = "Булки"]' #Раздел "Булки"
    active_div_in_constructor = By.XPATH, './/div[contains(@class, "current")]/span' #Активный раздел в конструкторе
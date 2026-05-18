from random import randint


class Data:
    name = 'Tikhonov'
    email = 'Tikhonov45ilya@yandex.ru'
    password = '987654321'


class Url:
    main_page = "https://stellarburgers.nomoreparties.site/" #URL главной страницы
    login_page = f"{main_page}login" #URL страницы авторизации
    registration_page = f"{main_page}register" #URL страницы регистрации
    profile_page = f"{main_page}account/profile" #URL страницы профиля


class RandomUser:
    name = f"Random{randint(0, 999)}Name"
    email = f"random{randint(000, 999)}@yandex.ru"
    password = f"rnd{randint(000, 999)}"
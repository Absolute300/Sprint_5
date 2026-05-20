from selenium.webdriver.common.by import By


class ConstructorLocators:
    # Таб "Булки"
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")
    # Таб "Соусы"
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")
    # Таб "Начинки"
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")

    # Карточка ингредиента из раздела "Булки" (по href с id)
    BUNS_INGREDIENT = (By.XPATH, "//a[contains(@href,'/ingredient/61c0c5a71d1f82001bdaaa6d')]")
    # Карточка ингредиента из раздела "Соусы" (по href с id)
    SAUCES_INGREDIENT = (By.XPATH, "//a[contains(@href,'/ingredient/61c0c5a71d1f82001bdaaa72')]")
    # Карточка ингредиента из раздела "Начинки" (по href с id)
    FILLINGS_INGREDIENT = (By.XPATH, "//a[contains(@href,'/ingredient/61c0c5a71d1f82001bdaaa6f')]")
from locators.constructor_locators import ConstructorLocators


class TestConstructorTabs:

    def test_constructor_tab_buns_can_be_opened(self, main_page):

    # Открываем главную страницу
         main_page.open_main()

    # Переходим на вкладку «Булки»
         main_page.open_tab_buns()

    # Проверяем, что таб «Булки» стал активным
         assert main_page.is_tab_buns_active(), (
        "Вкладка «Булки» не стала активной после переключения"
         )

    def test_constructor_tab_sauces_can_be_opened(self, main_page):
        # Проверяет открытие вкладки "Соусы" в конструкторе.
        main_page.open_main()
        main_page.open_tab_sauces()
        assert main_page.wait_visible(ConstructorLocators.SAUCES_INGREDIENT).is_displayed()

    def test_constructor_tab_fillings_can_be_opened(self, main_page):
        # Проверяет открытие вкладки "Начинки" в конструкторе.
        main_page.open_main()
        main_page.open_tab_fillings()
        assert main_page.wait_visible(ConstructorLocators.FILLINGS_INGREDIENT).is_displayed()
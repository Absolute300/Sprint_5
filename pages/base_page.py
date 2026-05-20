from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout: int = 12):
        self.driver = driver
        self.timeout = timeout

    def open(self, url: str):
        self.driver.get(url)

    def wait_visible(self, locator, timeout: int | None = None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_clickable(self, locator, timeout: int | None = None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator):
        element = self.wait_clickable(locator)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator, value: str):
        element = self.wait_clickable(locator)
        element.clear()
        element.send_keys(value)

    def wait_url_contains(self, value: str, timeout: int | None = None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(EC.url_contains(value))

    def is_visible(self, locator, timeout: int = 3) -> bool:
        try:
            self.wait_visible(locator, timeout=timeout)
            return True
        except TimeoutException:
            return False
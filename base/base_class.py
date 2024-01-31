from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By


class Base:

    def __init__(self, driver):
        self.driver = driver

    accept_city = "//span[contains(text(),'Да, верно')]"

    def get_accept_city(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.accept_city))

    def click_accept_city(self):
        self.get_accept_city().click()

    # Открытие url с использованием переданного драйвера
    @classmethod
    def open_page(cls, driver, url):
        driver.get(url)

    @classmethod
    def get_element_visibility(cls, driver, locator, timeout=20, max_attempts=5):

        attempts = 0
        while attempts < max_attempts:
            try:
                return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
            except StaleElementReferenceException:
                attempts += 1
            except TimeoutException as e:
                if attempts == max_attempts - 1:
                    raise e
                attempts += 1

        raise StaleElementReferenceException(
            "Couldn't find the element after several attempts."
        )

    @classmethod
    def get_element_clickable(cls, driver, locator, timeout=20, max_attempts=5):

        attempts = 0
        while attempts < max_attempts:
            try:
                return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
            except StaleElementReferenceException:
                attempts += 1
            except TimeoutException as e:
                if attempts == max_attempts - 1:
                    raise e
                attempts += 1

        raise StaleElementReferenceException(
            "Couldn't find the element after several attempts."
        )

    @classmethod
    def get_s_link_wrapper_locator(cls, index):
        base_locator = "(//div[@class='s-link__wrapper'])"
        return f"{base_locator}[{index}]"

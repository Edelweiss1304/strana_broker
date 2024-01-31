from base.base_class import Base
from selenium.webdriver.common.by import By
import time
from pages.header_links import Header
import testit


class Authorization(Base):
    # Locators
    login_lk_button = "//span[@class='the-header__icons-item']"
    login_client_phone_field = "//input [@type='tel']"
    get_code_btn = "//button[@type='button']"
    enter_code_field = "//input[@inputmode='numeric']"
    fin_login_btn = "//span[contains(text(),'Войти')]"
    check_lk = "//div[contains(text(),'Выбрать квартиру')]"

    first_login_broker_button = "//header//a[2]"
    email_field_agent = "email"
    password_field_agent = "//input[@type='password']"
    login_broker_btn = "//button[@type='submit']"
    broker_agent_check = "//h1[contains(text(),'Сделки')]"

    broker_header_button = "//a[contains(., 'Агентам и агентствам')]"
    broker_main_button = "//a[@href='https://broker.strana.com/']//div[@class='s-link__wrapper']"

    favorite_button = "//a[@id='header-favorite-icon']"
    login_from_favorite_button = "//span[contains(text(),'Войти в аккаунт')]"
    phone_field_favorite = "//label[@class='s-input s-input--default s-input--primary']//input[@type='tel']"
    get_code_favorite = "//span[contains(text(),'Получить код')]"
    enter_code_favorite = "//label[@class='s-input s-input--default s-input--primary']//input[@type='text']"
    final_login_favorite = "//button[.//span[@class='s-button__content' and normalize-space()='Войти']]"

    # Getters

    def get_login_lk_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.login_lk_button))

    def get_login_client_phone_field(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.login_client_phone_field))

    def get_enter_code_field(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.enter_code_field))

    def get_get_code_btn(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.get_code_btn))

    def get_fin_login_btn(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.fin_login_btn))

    def get_check_lk(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.check_lk)).text

    def get_email_field_agent(self):
        return self.get_element_clickable(self.driver, (By.NAME, self.email_field_agent))

    def get_password_field_agent(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.password_field_agent))

    def get_login_broker_btn(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.login_broker_btn))

    def get_broker_agent_check(self):
        return self.get_element_visibility(self.driver, (By.XPATH, self.broker_agent_check))

    def get_first_login_broker_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.first_login_broker_button))

    def get_broker_header_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.broker_header_button))

    def get_broker_main_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.broker_main_button))

    def get_favorite_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.favorite_button))

    def get_login_from_favorite_button(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.login_from_favorite_button))

    def get_phone_field_favorite(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.phone_field_favorite))

    def get_get_code_favorite(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.get_code_favorite))

    def get_enter_code_favorite(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.enter_code_favorite))

    def get_final_login_favorite(self):
        return self.get_element_clickable(self.driver, (By.XPATH, self.final_login_favorite))
    # Actions

    def click_login_lk_button(self):
        self.get_login_lk_button().click()
        print('Нажата кнопка входа в аккаунт в хэдере')

    def click_get_code_btn(self):
        self.get_get_code_btn().click()
        print('Нажата кнопка получить код')

    def click_fin_login_btn(self):
        self.get_fin_login_btn().click()
        print('Нажата финальная кнопка входа в аккаунт')

    def click_login_broker_btn(self):
        self.get_login_broker_btn().click()
        print('Нажата кнопка входа для брокера')

    def click_first_login_broker_button(self):
        self.get_first_login_broker_button().click()
        print('Нажата кнопка входа для брокера на посадочной странице')

    # Methods

    def login_page_broker_from_header(self):
        head = Header(self.driver)
        time.sleep(1)
        with testit.step("Открываем главную страницу"):
            head.actions.move_to_element(head.get_menu_button()).perform()
        with testit.step("Кликаем на Агентам и агентствам"):
            self.get_broker_header_button().click()
        with testit.step("Нажимаем Войти/Зарегистрироваться"):
            self.click_first_login_broker_button()

    def login_lk_broker(self, email='smiledmitriev@yandex.com', password='1234567890'):
        with testit.step("Вводим почту"):
            time.sleep(2)
            self.get_email_field_agent().send_keys(email)
        with testit.step("Вводим пароль"):
            self.get_password_field_agent().send_keys(password)
        with testit.step("Нажимаем Войти"):
            self.click_login_broker_btn()

    def login_broker_from_main_page(self):
        with testit.step("Кликаем Агентам и агентствам на главном экране"):
            self.get_broker_main_button().click()
        with testit.step("Нажимаем Войти"):
            self.click_first_login_broker_button()

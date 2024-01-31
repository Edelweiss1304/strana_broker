from pages.authorization import Authorization
from base.base_class import Base
from pages.url import URLS_MAIN
import pytest
import testit


@testit.displayName("Проверка авторизации в ЛК брокера через хедер")
@testit.description("Проверка авторизации в ЛК брокера через кнопку Агентам и агентствам в дополнительном меню")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_authorization_agent_from_header(driver, url):
    auth = Authorization(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        base_inst = Base(driver)
        base_inst.click_accept_city()
        auth.login_page_broker_from_header()
        auth.login_lk_broker()
    with testit.step("Проверяем, что вошли в ЛК брокера"):
        assert auth.get_broker_agent_check().text == "Сделки"
        print('Успешный вход в ЛК брокера, как агент')


@testit.displayName("Проверка авторизации в ЛК брокера через главную")
@testit.description("Проверка авторизации в ЛК брокера через кнопку Агентам и агентствам на главной странице")
@pytest.mark.parametrize("url", URLS_MAIN.values())
def test_authorization_agent_from_main_page(driver, url):
    auth = Authorization(driver)
    with testit.step("Открываем главную страницу"):
        Base.open_page(driver, url)
        base_inst = Base(driver)
        base_inst.click_accept_city()
        auth.login_broker_from_main_page()
        auth.login_lk_broker()
    with testit.step("Проверяем, что вошли в ЛК брокера"):
        assert auth.get_broker_agent_check().text == "Сделки"
        print('Успешный вход в ЛК брокера')

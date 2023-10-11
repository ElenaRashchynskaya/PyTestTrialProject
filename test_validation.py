from pages.mainPage import MainPage
import allure
import pytest


@allure.story('Test authorization with cookies')
@pytest.mark.critical
def test_authorization_accept_cookies(driver):
    p = MainPage(driver)
    p.click_agree_with_cookie_button()
    p.navigate_to_authorization_from_top_menu()
    p.fill_in_login_username("asdfdfsadf@gmail.com")
    p.click_next_button()
    assert p.try_again_is_find() is True


@allure.story('Test authorization without cookies')
@pytest.mark.critical
def test_authorization_not_accept_cookies(driver):
    p = MainPage(driver)
    p.navigate_to_authorization()
    p.fill_in_login_username("asdfdfsadf@gmail.com")
    p.click_next_button()
    assert p.try_again_is_find() is True

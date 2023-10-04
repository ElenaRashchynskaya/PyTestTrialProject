from pages.mainPage import MainPage


def test_authorization_Accept_cookies(driver):
    p = MainPage(driver)
    p.click_agree_with_cookie_button()
    p.navigate_to_authorization_from_top_menu()
    p.fill_in_login_username("asdfdfsadf@gmail.com")
    p.click_next_button()
    assert p.try_again_is_find() == True


def test_authorization_Not_Accept_cookies(driver):
    p = MainPage(driver)
    p.navigate_to_authorization()
    p.fill_in_login_username("asdfdfsadf@gmail.com")
    p.click_next_button()
    assert p.try_again_is_find() == True

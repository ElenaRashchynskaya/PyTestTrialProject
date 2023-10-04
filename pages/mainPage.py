from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from .common import Common



class MainPage(Common):

    AGREE_COOKIE = (By.ID, "W0wltc")
    LOGIN_BUTTON = (By.ID, "gksS1d")
    LOGIN_BUTTON_TOP = (By.CSS_SELECTOR, "span.gb_Hd")
    LOGIN_INPUT = (By.ID, "identifierId")
    NEXT_BUTTON = (By.XPATH, ".//*[@id='identifierNext']//button")
    TRY_AGAIN_BUTTON = (By.CSS_SELECTOR, "[jsname='LgbsSe']")


    def click_agree_with_cookie_button(self):
        self.wait_for(self.AGREE_COOKIE).click()

    def navigate_to_authorization_from_top_menu(self):
        self.wait_for(self.LOGIN_BUTTON_TOP).click()

    def navigate_to_authorization(self):
        self.wait_for(self.LOGIN_BUTTON).click()

    def fill_in_login_username(self, username):
        self.wait_for(self.LOGIN_INPUT).send_keys(username)

    def click_next_button(self):
        self.find(self.NEXT_BUTTON).click()

    def try_again_is_find(self):
        return self.wait_for_element(self.TRY_AGAIN_BUTTON).is_displayed()

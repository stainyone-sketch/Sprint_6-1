from .base_page import BasePage
from locators.cookie_banner import CookieBanner as CookieLocators
import allure

class CookieBanner(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CookieLocators

    @allure.step("Закрыть куки-баннер")
    def close(self):
        try:
            self.wait_clickable(self.locators.ACCEPT_BUTTON, timeout=5).click()
        except:
            pass

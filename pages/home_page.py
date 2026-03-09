import allure
from .base_page import BasePage
from locators.header import Header
from locators.main import MainPage
from locators.cookie_banner import CookieBanner
from .cookie_banner import CookieBanner

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.header = Header
        self.main = MainPage
        self.cookie = CookieBanner(driver)

    @allure.step("Открыть главную страницу")
    def open(self, url):
        self.open_url(url)

    @allure.step("Закрыть куки-баннер")
    def close_cookie_banner(self):
        self.cookie.close()

    @allure.step("Клик по верхней кнопке «Заказать»")
    def click_order_top(self):
        self.wait_clickable(self.header.ORDER_BUTTON_HEADER).click()

    @allure.step("Клик по нижней кнопке «Заказать»")
    def click_order_bottom(self):
        self.wait_clickable(self.main.ORDER_BUTTON_BOTTOM).click()

    @allure.step("Клик по логотипу Яндекса")
    def click_yandex_logo(self):
        self.wait_clickable(self.header.YANDEX_LOGO).click()

    @allure.step("Клик по логотипу «Самокат»")
    def click_scooter_logo(self):
        self.wait_clickable(self.header.SCOOTER_LOGO).click()

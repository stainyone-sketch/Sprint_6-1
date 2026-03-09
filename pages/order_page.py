from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.order import OrderPage as OrderLocators
import allure

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderLocators

    @allure.step("Заполнение первого шага формы заказа")
    def fill_first_step(self, order_data):
        self.wait_visible(self.locators.FIRST_NAME).send_keys(order_data["name"])
        self.find_element(self.locators.LAST_NAME).send_keys(order_data["surname"])
        self.find_element(self.locators.ADDRESS).send_keys(order_data["address"])

        # Выбор станции метро
        self.click(self.locators.METRO_INPUT)
        metro_option = self.wait_clickable(self.locators.metro_option(order_data["metro"]))
        metro_option.click()

        self.find_element(self.locators.PHONE).send_keys(order_data["phone"])
        self.click(self.locators.NEXT_BUTTON)

    @allure.step("Заполнение второго шага формы заказа")
    def fill_second_step(self, order_data):
        date_input = self.wait_visible(self.locators.DATE_INPUT)
        date_input.clear()
        date_input.send_keys(order_data["date"])
        date_input.send_keys(Keys.ENTER)

        # Закрыть календарь
        self.click_body()

        # Срок аренды
        self.click(self.locators.RENTAL_DROPDOWN)
        rental_option = self.wait_clickable(self.locators.rental_option(order_data["rental_period"]))
        rental_option.click()

        # Цвет
        if order_data["color"] == "black":
            self.click(self.locators.COLOR_BLACK)
        else:
            self.click(self.locators.COLOR_GREY)

        # Комментарий
        comment = self.find_element(self.locators.COMMENT)
        comment.clear()
        comment.send_keys(order_data["comment"])

    @allure.step("Клик по кнопке Заказать")
    def click_order_button(self):
        btn = self.wait_clickable(self.locators.ORDER_BUTTON)
        self.scroll_into_view(btn)
        try:
            btn.click()
        except Exception:
            self.js_click(btn)

    @allure.step("Ожидание появления окна подтверждения заказа")
    def is_confirmation_modal_visible(self):
        self.wait_visible(self.locators.CONFIRM_MODAL)
        return True

    @allure.step("Клик по кнопке Да в окне подтверждения")
    def click_confirm(self):
        self.wait_clickable(self.locators.CONFIRM_BUTTON).click()

    @allure.step("Проверка появления окна успешного заказа")
    def is_success_modal_visible(self):
        modal = self.wait_visible(self.locators.SUCCESS_MODAL)
        return modal.find_element(*self.locators.SUCCESS_MESSAGE).is_displayed()
    
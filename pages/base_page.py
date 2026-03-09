from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from constants import DEFAULT_TIMEOUT
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    @allure.step("Открыть URL: {url}")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Кликнуть на тег body")
    def click_body(self):
        body = self.driver.find_element(By.TAG_NAME, "body")
        body.click()

    @allure.step("Найти элемент {locator}")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Кликнуть по элементу {locator}")
    def click(self, locator):
        self.find_element(locator).click()

    @allure.step("Ожидание видимости элемента {locator}")
    def wait_visible(self, locator, timeout=None):
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание кликабельности элемента {locator}")
    def wait_clickable(self, locator, timeout=None):
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Прокрутка к элементу")
    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Клик через JavaScript")
    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ожидание URL: {url}")
    def wait_for_url_to_be(self, url, timeout=None):
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        wait.until(EC.url_to_be(url))

    @allure.step("Ожидание URL содержит: {partial_url}")
    def wait_for_url_contains(self, partial_url, timeout=None):
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        wait.until(EC.url_contains(partial_url))

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Получение текущего дескриптора окна")
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    @allure.step("Ожидание количества окон: {count}")
    def wait_for_number_of_windows(self, count, timeout=None):
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        wait.until(EC.number_of_windows_to_be(count))

    @allure.step("Переключение на новое окно (кроме исходного)")
    def switch_to_new_window(self, original_window):
        for handle in self.driver.window_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                return handle
        raise Exception("Новое окно не найдено")

    @allure.step("Закрыть текущее окно и переключиться на исходное")
    def close_current_window_and_switch_back(self, original_window):
        self.driver.close()
        self.driver.switch_to.window(original_window)

    def is_element_visible(self, locator, timeout=0):
        try:
            self.wait_visible(locator, timeout)
            return True
        except TimeoutException:
            return False
        
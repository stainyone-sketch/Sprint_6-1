import allure
import pytest
from constants import BASE_URL

@pytest.mark.navigation
@allure.epic("Навигация")
class TestNavigation:

    @allure.title("Проверка перехода по логотипу Самоката")
    def test_scooter_logo_navigation(self, home_page):
        home_page.click_scooter_logo()
        home_page.wait_for_url_to_be(BASE_URL)
        assert home_page.get_current_url() == BASE_URL

    @allure.title("Проверка перехода по логотипу Яндекса (открытие Дзена)")
    def test_yandex_logo_navigation(self, home_page):
        original_window = home_page.get_current_window_handle()
        home_page.click_yandex_logo()
        home_page.wait_for_number_of_windows(2)
        home_page.switch_to_new_window(original_window)
        home_page.wait_for_url_contains("dzen.ru")
        assert "dzen.ru" in home_page.get_current_url()

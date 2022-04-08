import allure
import pytest

from config import CONFIG
from pages.main_page import MainPage


@pytest.mark.smoke
@pytest.mark.news
@allure.feature('News block')
class TestNews:

    @allure.description('Проверка дефолтного количества отображаемых новостей')
    def test_default_news_count(self, browser, open_url):
        main_page = MainPage(browser)
        main_page.smart_assert(lambda x: len(main_page.get_news()) == CONFIG.news.rows_count,
                               message='Неправильное количество отображаемых новостей')

    @allure.description('Проверка кнопки "Показать еще"')
    def test_view_more_button(self, browser, open_url):
        main_page = MainPage(browser)
        main_page.click_view_more_button()
        main_page.smart_assert(lambda x: len(main_page.get_news()) == CONFIG.news.rows_count_after_click_more,
                               message='Неправильное количество новостей после нажатия кнопки "Показать еще"')

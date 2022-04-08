import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.__driver = driver
        self.__news_rows = (By.CSS_SELECTOR, '.news__item-content')
        self.__view_more_button = (By.CSS_SELECTOR, '.news__more-button')

    @allure.step('Получить список новостей')
    def get_news(self):
        return [row.text for row in self.wait_for_all_elements_visible(self.__news_rows)]

    @allure.step('Нажать кнопку "Показать еще"')
    def click_view_more_button(self):
        self.wait_for_element_clickable(self.__view_more_button).click()



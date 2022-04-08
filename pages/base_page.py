from typing import List

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config import CONFIG


class BasePage:
    __timeout = CONFIG.common_settings.timeout

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver

    def element(self, locator, timeout=__timeout) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator),
                                                         message=f"Can't find element by locator {locator}")

    def elements(self, locator, timeout=__timeout) -> List[WebElement]:
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator),
                                                         message=f"Can't find elements by locator {locator}")

    def wait_for_element_clickable(self, locator, timeout=__timeout) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_for_element_visible(self, locator, timeout=__timeout) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_all_elements_visible(self, locator, timeout=__timeout) -> List[WebElement]:
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def wait_for(self, lambda_expression, timeout=__timeout, message='') -> None:
        WebDriverWait(self.driver, timeout).until(lambda_expression, message=message)

    def smart_assert(self, lambda_expression, timeout=__timeout, message=''):
        try:
            self.wait_for(lambda_expression, timeout, message)
        except TimeoutException:
            assert False, message

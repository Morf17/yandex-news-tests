import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from config import CONFIG


def pytest_addoption(parser):
    parser.addoption('--headless', action='store_true', default=False,
                     help='browser headless mode')


@pytest.fixture(scope="function")
def browser(request):
    options = webdriver.ChromeOptions()
    if bool(request.config.getoption('headless')):
        options.headless = True
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-extensions')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--lang=ru-RU')
    else:
        options.add_argument('--start-maximized')
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
@allure.step(f'Открыть страницу {CONFIG.common_settings.url}')
def open_url(browser):
    browser.get(CONFIG.common_settings.url)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == 'call' and result.failed:
        try:
            driver = item.funcargs['browser']
            allure.attach(
                body=driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print(f'Fail to take screenshot: {e}')

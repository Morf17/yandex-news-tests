# yandex-news-tests

### Install project
```sh
$ git clone https://github.com/Morf17/yandex-news-tests.git
// python3 -m venv env
$ pip install -r requirements.txt
```

### Run
```sh
All test case with allure report:
$ pytest --alluredir report
All tests in headdless mode:
$ pytest --headless
Selected cases suite with allure report:
$ pytest -m news --alluredir report
Collect and display the report after the tests:
$ allure serve report
```
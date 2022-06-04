import os
import pytest
from selenium import webdriver
from selenium.webdriver.opera.options import ChromeOptions
from webdriver_manager.opera import OperaDriverManager


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--drivers', default=os.path.expanduser('~/Develop/drivers'))
    parser.addoption('--url', default='http://192.168.2.113')


@pytest.fixture(scope='module')
def driver(request):
    browser_name = request.config.getoption('--browser')
    drivers = request.config.getoption('--drivers')

    if browser_name == 'chrome':
        browser = webdriver.Chrome(executable_path=f'{drivers}/chromedriver')
    elif browser_name == 'firefox':
        browser = webdriver.Firefox(executable_path=f'{drivers}/geckodriver')
    elif browser_name == 'opera':
        options = ChromeOptions()
        options.add_experimental_option('w3c', True)
        browser = webdriver.Opera(executable_path=OperaDriverManager().install(), options=options)
    elif browser_name == 'safari':
        browser = webdriver.Safari(executable_path='/usr/bin/safaridriver')
    else:
        raise ValueError(f'Browser {browser_name} is not supported! Try to use chrome, firefox, opera or safari')

    browser.maximize_window()
    request.addfinalizer(browser.close)

    return browser


@pytest.fixture
def url(request):
    return request.config.getoption('--url')

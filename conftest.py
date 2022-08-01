import logging
import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.opera.options import ChromeOptions
from webdriver_manager.opera import OperaDriverManager


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--drivers', default=os.path.expanduser('~/Develop/drivers'))
    parser.addoption('--url', default='http://192.168.2.86')
    parser.addoption('--log_level', default='DEBUG')
    parser.addoption('--executor', default='192.168.2.86')
    parser.addoption('--vnc', action='store_true')
    parser.addoption('--browser_version')


@pytest.fixture(scope='module')
def driver(request):
    browser_name = request.config.getoption('--browser')
    drivers = request.config.getoption('--drivers')
    log_level = request.config.getoption('--log_level')
    executor = request.config.getoption('--executor')
    vnc = request.config.getoption('--vnc')
    browser_version = request.config.getoption('--browser_version')
    url = request.config.getoption('--url')

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler('logs.log')
    file_handler.setFormatter(logging.Formatter('%(levelname)s - %(asctime)s : %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info(f'Тесты "{request.node.name}" начали прохождение в {datetime.now()}')

    options = ChromeOptions()
    if browser_name == 'opera':
        options.add_experimental_option('w3c', True)

    if executor == 'local':
        if browser_name == 'chrome':
            browser = webdriver.Chrome(executable_path=f'{drivers}/chromedriver')
        elif browser_name == 'firefox':
            browser = webdriver.Firefox(executable_path=f'{drivers}/geckodriver')
        elif browser_name == 'opera':
            browser = webdriver.Opera(executable_path=OperaDriverManager().install(), options=options)
        elif browser_name == 'safari':
            browser = webdriver.Safari(executable_path='/usr/bin/safaridriver')
        else:
            raise ValueError(f'Browser {browser_name} is not supported! Try to use chrome, firefox, opera or safari')

    else:
        executor_url = f'http://{executor}:4444/wd/hub'
        caps = {
            'browserName': browser_name,
            'browserVersion': browser_version,
            'screenResolution': '1280x720',
            'selenoid:options': {
                'enableVNC': vnc,
            },
            'acceptSslCerts': True,
            'acceptInsecureCerts': True
        }

        browser = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps,
            options=options
        )

    browser.maximize_window()

    browser.logger = logger
    browser.url = url

    def fin():
        browser.close()
        logger.info(f'Тесты "{request.node.name}" закончили прохождение в {datetime.now()}\n')

    request.addfinalizer(fin)

    return browser

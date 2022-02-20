import pytest


def pytest_addoption(parser):
    parser.addoption("--url", default=" https://ya.ru", help="Request url")
    parser.addoption("--status_code", default=200, help="Request status code")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="session")
def status_code(request):
    return int(request.config.getoption("--status_code"))

import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(executable_path=ChromeDriverManager().install())

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# Arrange
@pytest.fixture(params=["Chrome", "Firefox", "Edge"])            # remove (params=["Chrome", "firefox", "edge"]) to run only on a specific browser
def driver(request):
    # browser = request.config.getoption("--browser")            ------------ uncomment this to run only on a specific browser
    browser = request.param
    # Open the browser
    print(f'Creating driver for {browser} browser')
    if browser == "Chrome":
        browser_driver = webdriver.Chrome(service=service)
    elif browser == "Firefox":
        browser_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "Edge":
        browser_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise TypeError(f'Expected browser to be chrome,firefox,edge got {browser}')
    yield browser_driver
    print(f'Closing driver for {browser} browser')
    browser_driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", help="provide browser as Chrome, Edge or firefox")

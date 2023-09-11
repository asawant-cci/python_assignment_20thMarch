# import required packages
import time
import pytest

# import webdriver_manager.chrome

from selenium import webdriver

# from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from page_objects.login_page import LoginPage

service = ChromeService(executable_path=ChromeDriverManager().install())


@pytest.mark.login
@pytest.mark.login_negative
@pytest.mark.parametrize("username,password,expected_error_message",
                         [("adminxyz", "admin123", "Invalid Credentials"),
                          ("admin", "admin123xyz", "Invalid Credentials"),
                          ("adminxyz", "admin123xyz", "Invalid Credentials")])
def test_invalid_username_and_password_login(driver, username, password, expected_error_message):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.perform_login(username, password)
    time.sleep(5)
    login_page.is_error_label_displayed()
    assert login_page.error_label_text() == expected_error_message, "Error message does not match"
    time.sleep(5)


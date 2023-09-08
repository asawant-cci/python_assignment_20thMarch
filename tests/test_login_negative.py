# import required packages
import time
import pytest

# import webdriver_manager.chrome

from selenium import webdriver

# from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(executable_path=ChromeDriverManager().install())


@pytest.mark.login
@pytest.mark.login_negative
@pytest.mark.parametrize("username,password,expected_error_message",
                         [("adminxyz", "admin123", "Invalid Credentials"),
                          ("admin", "admin123xyz", "Invalid Credentials"),
                          ("adminxyz", "admin123xyz", "Invalid Credentials")])
def test_invalid_username_and_password_login(driver, username, password, expected_error_message):
    """Test :A user with valid credentials should be able to Log in successfully
    URL :https://login-app-iota.vercel.app
    """
    # Act
    # Navigate to Site URL
    driver.get("https://login-app-iota.vercel.app")

    # Validate if the default URL is pointing to the login route

    time.sleep(10)

    current_url = driver.current_url
    assert current_url == "https://login-app-iota.vercel.app/login", "Default URL route should be login"

    # locate username element
    username_textbox = driver.find_element(By.ID, 'username_textbox')

    # locate password element
    password_textbox = driver.find_element(By.ID, 'password_textbox')

    # locate login button
    login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")

    # enter invalid username
    username_textbox.send_keys(username)

    # enter valid password
    password_textbox.send_keys(password)

    # Click on login button.
    login_btn.click()
    time.sleep(10)

    # Assert
    # Validate logged in URL

    logged_url = driver.current_url
    assert logged_url == "https://login-app-iota.vercel.app/login", "Default logged URL route should be login"

    # Validate login error message
    error_message = driver.find_element(By.XPATH,
                                        "//div[@id='root']/div[@class='App']/section/div//form//div[.='Invalid Credentials']")
    error_text = error_message.text
    assert error_message.is_displayed(), "Error message not displayed"
    assert error_text == expected_error_message, "Error message does not match"

# @pytest.mark.login
# @pytest.mark.login_negative
# def test_invalid_password_login(driver):
#     """Test :A user with valid credentials should be able to Log in successfully
#     URL :https://login-app-iota.vercel.app
#     """
#
#     # Navigate to Site URL
#     driver.get("https://login-app-iota.vercel.app")
#
#     # Validate if the default URL is pointing to the login route
#
#     time.sleep(10)
#
#     current_url = driver.current_url
#     assert current_url == "https://login-app-iota.vercel.app/login", "Default URL route should be login"
#
#     # locate username element
#     username_textbox = driver.find_element(By.ID, 'username_textbox')
#
#     # locate password element
#     password_textbox = driver.find_element(By.ID, 'password_textbox')
#
#     # locate login button
#     login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
#
#     # enter valid username
#     username_textbox.send_keys('admin')
#
#     # enter invalid password
#     password_textbox.send_keys('admin123xyz')
#
#     # Click on login button.
#     login_btn.click()
#     time.sleep(10)
#
#     # Validate logged in URL
#
#     logged_url = driver.current_url
#     assert logged_url == "https://login-app-iota.vercel.app/login", "Default logged URL route should be login"
#
#     # Validate login error message
#     error_message = driver.find_element(By.XPATH,
#                                         "//div[@id='root']/div[@class='App']/section/div//form//div[.='Invalid Credentials']")
#     error_text = error_message.text
#     assert error_message.is_displayed(), "Error message not displayed"
#     assert error_text == "Invalid Credentials", "Error message does not match"
#     time.sleep(4)

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
@pytest.mark.login_positive
def test_valid_user_login(driver):
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

    # enter valid username
    username_textbox.send_keys('admin')

    # enter valid password
    password_textbox.send_keys('admin123')

    # Click on login button.
    login_btn.click()
    time.sleep(10)

    # locate about link
    about_link = driver.find_element(By.XPATH, "//*[@id='navbarSupportedContent']/div/a[5]")
    about_link.click()
    time.sleep(5)

    # Validate logged in URL

    logged_url = driver.current_url
    assert logged_url == "https://login-app-iota.vercel.app/about", "Default logged URL route should be about"

    # Assert
    # Validate header title
    header_text = driver.find_element(By.TAG_NAME, "h1")
    login_text = header_text.text
    assert header_text.is_displayed(), "Welcome message not displayed"
    assert login_text == "Welcome to Selenium Learning Group", "Welcome text does not match"
    time.sleep(4)

    # locate logout button
    logout_btn = driver.find_element(By.LINK_TEXT, "Logout")

    # click on logout button
    logout_btn.click()

    # validate that login page URL is displayed
    assert driver.current_url == "https://login-app-iota.vercel.app/login"

    time.sleep(3)



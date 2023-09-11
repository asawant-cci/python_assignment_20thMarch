import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class LoginPage:
    __url = "https://login-app-iota.vercel.app/"
    __username_field = (By.ID, 'username_textbox')
    __password_field = (By.ID, 'password_textbox')
    __submit_button = (By.XPATH, "//button[@type='submit']")
    __error_label_field = (By.XPATH, "//div[text()='Invalid Credentials']")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get(self.__url)

    @property
    def current_url(self):
        return self._driver.current_url

    def perform_login(self, username, password):
        username_data = self._driver.find_element(*self.__username_field)
        password_data = self._driver.find_element(*self.__password_field)
        submit_button_field = self._driver.find_element(*self.__submit_button)

        username_data.send_keys(username)
        password_data.send_keys(password)
        time.sleep(5)
        submit_button_field.click()
        time.sleep(5)

    def error_label_text(self):
        error_label = self._driver.find_element(*self.__error_label_field)
        actual_text = error_label.text
        return actual_text

    def is_error_label_displayed(self):
        self._driver.find_element(*self.__error_label_field).is_displayed()
        # displayed_error_message = self._driver.find_element(*self.__error_label_field)
        # displayed_error_message.is_displayed()



# SauceDemoMain.py

"""
Program Description : This script implements Python Selenium automation for the SauceDemo website.
                      It includes classes for data, locators, and the main automation logic.
                      Explicit waits are used to ensure elements are loaded before interacting with them.

Programmer : Suman Gangopadhyay
Email ID : linuxgurusuman@gmail.com
Date : 24-Feb-2025
Version : 1.0
Code Library : Selenium
Prerequisites : Python, Selenium, ChromeDriver, YAML
Caveats : None
"""

# Import necessary Selenium modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # For explicit waits
from selenium.webdriver.support import expected_conditions as EC  # For expected conditions
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException

"""Data Class"""


class Data:
    """
    This class contains static data such as URLs, usernames, and passwords
    used for testing the SauceDemo website.
    """
    # URL of the SauceDemo login page
    URL = "https://www.saucedemo.com/"

    # URL of the dashboard page after successful login
    DASHBOARD_URL = "https://www.saucedemo.com/inventory.html"

    # Valid username for login
    USERNAME = "standard_user"

    # Valid password for login
    PASSWORD = "secret_sauce"


"""Locators Class"""


class Locators:
    """
    This class contains the locators (e.g., IDs, class names) for the web elements
    on the SauceDemo website.
    """
    # Locator for the username input box
    USERNAME_INPUT_BOX = "user-name"

    # Locator for the password input box
    PASSWORD_INPUT_BOX = "password"

    # Locator for the login button
    SUBMIT_BUTTON = "login-button"

    # Locator for the hamburger menu button
    HAMBURGER_BUTTON = "react-burger-menu-btn"

    # Locator for the logout button in the sidebar
    LOGOUT_BUTTON = "logout_sidebar_link"


"""Main Execution Class for Automation"""


class SauceDemoAutomation(Data, Locators):
    """
    This class contains the main automation logic for testing the SauceDemo website.
    It inherits from the Data and Locators classes to access test data and locators.
    Explicit waits are used to ensure elements are present and interactable before performing actions.
    """

    def __init__(self, web_url):
        """
        Constructor to initialize the web driver and set the URL.
        :param web_url: The URL of the website to be tested.
        """
        self.url = web_url

        # Initialize the Chrome WebDriver using webdriver_manager to handle driver installation
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        # Initialize WebDriverWait for explicit waits (10 seconds timeout)
        self.wait = WebDriverWait(self.driver, 10)

    def start(self):
        """
        Start the automation by opening the browser, maximizing the window,
        and navigating to the specified URL.
        :return: True if successful, otherwise returns the error.
        """
        try:
            self.driver.maximize_window()  # Maximize the browser window
            self.driver.get(self.url)  # Navigate to the specified URL
            return True
        except TimeoutException as error:
            return error  # Return the error if a timeout occurs

    def shutdown(self):
        """
        Shutdown the automation by closing the browser.
        :return: True if successful, otherwise returns the error.
        """
        try:
            self.driver.quit()  # Close the browser
            return True
        except WebDriverException as error:
            return error  # Return the error if an exception occurs

    def validate_username_input_box(self):
        """
        Validate if the username input box is displayed on the page using explicit wait.
        :return: True if the username input box is displayed, otherwise False.
        """
        try:
            # Wait until the username input box is visible on the page
            username_input_box = self.wait.until(
                EC.visibility_of_element_located((By.ID, self.USERNAME_INPUT_BOX))
            )
            return True
        except TimeoutException:
            return False  # Return False if the element is not visible within the timeout
        except NoSuchElementException:
            return False  # Return False if the element is not found

    def validate_password_input_box(self):
        """
        Validate if the password input box is displayed on the page using explicit wait.
        :return: True if the password input box is displayed, otherwise False.
        """
        try:
            # Wait until the password input box is visible on the page
            password_input_box = self.wait.until(
                EC.visibility_of_element_located((By.ID, self.PASSWORD_INPUT_BOX))
            )
            return True
        except TimeoutException:
            return False  # Return False if the element is not visible within the timeout
        except NoSuchElementException:
            return False  # Return False if the element is not found

    def validate_submit_button(self):
        """
        Validate if the submit button is enabled on the page using explicit wait.
        :return: True if the submit button is enabled, otherwise False.
        """
        try:
            # Wait until the submit button is clickable (enabled and visible)
            submit_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, self.SUBMIT_BUTTON))
            )
            return True
        except TimeoutException:
            return False  # Return False if the element is not clickable within the timeout
        except NoSuchElementException:
            return False  # Return False if the element is not found

    def validate_login(self):
        """
        Perform login by entering the username and password, and validate if the login is successful.
        Uses explicit waits to ensure elements are interactable before performing actions.
        :return: True if login is successful and the dashboard URL is reached, otherwise False.
        """
        try:
            # Wait for the username input box to be visible and enter the username
            self.wait.until(
                EC.visibility_of_element_located((By.ID, self.USERNAME_INPUT_BOX))
            ).send_keys(self.USERNAME)

            # Wait for the password input box to be visible and enter the password
            self.wait.until(
                EC.visibility_of_element_located((By.ID, self.PASSWORD_INPUT_BOX))
            ).send_keys(self.PASSWORD)

            # Wait for the submit button to be clickable and click it
            self.wait.until(
                EC.element_to_be_clickable((By.ID, self.SUBMIT_BUTTON))
            ).click()

            # Wait for the URL to change to the dashboard URL after login
            self.wait.until(EC.url_to_be(self.DASHBOARD_URL))
            return True
        except TimeoutException:
            return False  # Return False if the expected URL is not reached within the timeout
        except NoSuchElementException as error:
            return error  # Return the error if any element is not found

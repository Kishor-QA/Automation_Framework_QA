from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
import time

class Basepage:
    def __init__(self, driver:WebDriver):
        self.driver= driver
        self.wait = WebDriverWait(driver, 30)
    
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def find_elements(self, locator, parent_element=None):
        if parent_element:
            return parent_element.find_elements(*locator)
        return self.driver.find_elements(*locator)
    
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def click_nth_element(self, locator, n):
        elements = self.wait.until(EC.presence_of_all_elements_located(locator))
        elements[n].click()

    def select_dropdown_by_value(self, locator, value):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].removeAttribute('hidden')", element)
        dropdown = Select(element)
        dropdown.select_by_value(value)

    def select_dropdown_by_visible_text(self, locator, text):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].removeAttribute('hidden')", element)
        dropdown = Select(element)
        dropdown.select_by_visible_text(text)

    def set_radio(self, locator, should_select=True):
            element = self.wait.until(EC.element_to_be_clickable(locator))
            if element.is_selected() != should_select:
                element.click()

    def validate(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))

    def get(self, url):
        self.driver.get(url)

    def iframe(self, locator):
        iframe_element = self.find_element(locator)
        self.driver.switch_to.frame(iframe_element)

    def back_deafult(self):
        self.driver.switch_to.default_content()

    def send_keys(self, locator, value):
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            element.clear()
            time.sleep(5)
            element.send_keys(value, Keys.ENTER)

    def upload_file(self, locator, file_path, is_file_input=True):
        try:
            element = self.driver.find_element(*locator)
            if is_file_input:
                # Unhide the input if it's hidden
                self.driver.execute_script("arguments[0].classList.remove('hidden');", element)
                element.send_keys(file_path)
            else:
                # Just click the upload button
                element = self.wait.until(EC.element_to_be_clickable(locator))
                element.click()
        except Exception as e:
            raise Exception(f"Upload failed: {e}")
    def select_custom_dropdown(self, trigger_locator, options_locator, value_to_select):
        self.click_element(trigger_locator)
        time.sleep(1)  # Allow dropdown to load

        options = self.driver.find_elements(*options_locator)
        for option in options:
            if option.text.strip().lower() == value_to_select.strip().lower():
                option.click()
                break

    def toast_alert(self, locator):
        element = self.wait.until((EC.visibility_of_element_located(locator)))
        return element.text.strip()
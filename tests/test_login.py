import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import conftest
from pages.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import Log_Maker
import pandas as pd

def load_credentials(file_path="./Test_Data/login_info.csv"):
    df = pd.read_csv(file_path)
    # Convert DataFrame to list of tuples
    return list(df.itertuples(index=False, name=None))

test_data = load_credentials()

@pytest.mark.parametrize("username,password,case_type,expected", test_data)
def test_login(driver, username, password, case_type, expected, login_page):
    logger = Log_Maker.log_gen()
    logger.info("====== Starting Login Test ======")
    print("We are here")
    try:
        # 1️⃣ FIRST check if page even loads
        login_page = LoginPage(driver)
        logger.info("Opening Login Page")
        print(f"Current title is :{driver.title}")
        if "Site cannot be reached" in driver.page_source or driver.title == "":
            raise Exception("Page did not load properly")

        logger.info("Page loaded successfully.")

    except Exception as e:
        logger.error(f"Page Load Failed: {str(e)}")
        save_screenshot(driver, logger)
        raise  # test stops here
    try:
        login_page.login(username , password)

        if case_type == "success":
            actual_title = driver.title
            assert actual_title == expected, \
                f"Expected title '{expected}', got '{actual_title}'"
            logger.info(f"Login success verified: {actual_title}")

        else:
            actual_error = login_page.get_error_message()
            assert expected in actual_error, f"Expected error '{expected}', got '{actual_error}'"
            logger.info(f"Login failure verified: {actual_error}")

    except AssertionError as e:
        logger.error(f"Test Failed: {str(e)}")
        save_screenshot(driver, logger)
        raise

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        save_screenshot(driver, logger)
        raise

    def save_screenshot(driver, logger):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join("screenshots", f"screenshot_{timestamp}.png")
        driver.save_screenshot(screenshot_path)
        logger.info(f"Screenshot saved: {screenshot_path}")
#//span(text()="Required")
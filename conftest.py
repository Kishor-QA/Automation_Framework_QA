from selenium import webdriver
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utilities.read_properties import ReadConfig
from pages.login_page import LoginPage
from pages.home_page import Home
import time
import pandas as pd

def pytest_addoption(parser):  
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Specify the browser: chrome or firefox or edge"
    )
    parser.addoption(
        "--email",
        action="store",
        default="org@test.com",
        help="Login email"
    )
    parser.addoption(
        "--password",
        action="store",
        default="password",
        help="Login password"
    )

@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="class")
def credentials(request):
    email = request.config.getoption("--email")
    password = request.config.getoption("--password")
    return email, password

@pytest.fixture(scope="class")
def driver(browser):
    if browser.lower() == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser.lower() == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise ValueError(f"Unsupported browser: {browser}. Choose from chrome, firefox, or edge.")

    driver.get(ReadConfig.get_page_url())
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def get_valid_credentials(file_path="./Test_Data/login_info.csv"):
    df = pd.read_csv(file_path)
    valid_row = df[df['case_type'] == 'success'].iloc[0]   # take first valid row
    return valid_row['username'], valid_row['password']

@pytest.fixture(scope="class")
def dashboard(driver:WebDriver, get_valid_credentials):
    email, password = get_valid_credentials
    login = LoginPage(driver)
    login.login(email, password)
    return Home(driver)

# @pytest.fixture(scope="class")
# def select_client(driver, dashboard):
#     client_elements = dashboard.client()
#     client_list = [el.text for el in client_elements if el.text.strip()]
#     assert client_list, "Client list is empty."
#     client = "Ezdihar Sports"
#     #for client in client_list:
#     dashboard.get(dashboard.client_URL())
#     print(f"Selecting client: {client}")
#     dynamic_locator = ClientConfig.get_dynamic_client_locator(client)
#     time.sleep(2)
#     element = dashboard.find_element(dynamic_locator)
#     print(f"Dynamic locator for client {client}: {dynamic_locator}")
#     element.click()
#     yield
#     #break  # If you want to test with just the first client

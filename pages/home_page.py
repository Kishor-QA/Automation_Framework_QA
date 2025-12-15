import pytest
from pages.login_page import LoginPage
from utilities.custom_logger import Log_Maker
from utilities.read_properties import DashboardConfig
import pandas as pd

class Home(LoginPage):
    def __init__(self, driver):
        super().__init__(driver)

    Email = DashboardConfig.get_locator("Email")
    First_Name = DashboardConfig.get_locator("First_Name")
    Family_Name = DashboardConfig.get_locator("Family_Name")
    Middle_Name = DashboardConfig.get_locator("Middle_Name")
    Password = DashboardConfig.get_locator("Password")
    Create_Account = DashboardConfig.get_locator("Create_Account")
    Error_Alert= DashboardConfig.get_locator("Toast_Alert_Error")
    Success_Alert = DashboardConfig.get_locator("Toast_Alert_Success")

    def create_new_user(self):
        locator= DashboardConfig.get_locator("Create_New_User")
        self.click(locator)
    
    def add_new_user(self, email, first_name, family_name, midddle_name, password):
        self.send_keys(self.Email, email)
        self.send_keys(self.First_Name, first_name)
        self.send_keys(self.Family_Name, family_name)
        self.send_keys(self.Middle_Name, midddle_name)
        self.send_keys(self.Password, password)
        self.click(self.Create_Account)

    def get_error_toast(self):
        return self.toast_alert(self.Error_Alert)
    def get_success_toast(self):
        return self.toast_alert(self.Error_Alert).text
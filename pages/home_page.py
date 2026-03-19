import pytest
from pages.login_page import LoginPage
from utilities.custom_logger import Log_Maker
from utilities.read_properties import DashboardConfig
from utilities.read_properties import AssignServices
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
    # Error_Message_Div = DashboardConfig.get_locator("Error_Message_Div")
    # Error_Message_Register = DashboardConfig.get_locator("Error_Message")
    Email_Error_Message= DashboardConfig.get_locator("Email_Error_Message")
    FirstName_Error_Message = DashboardConfig.get_locator("FirstName_Error_Message")
    FamilyName_Error_Message= DashboardConfig.get_locator("FamilyName_Error_Message")
    Password_Error_Message = DashboardConfig.get_locator("Password_Error_Message")
    # Assign_Services_URL = AssignServices.get_assignservices_url("get_assignservices_url")
    All_Services = AssignServices.get_locator("All_Services")

    def create_new_user(self):
        locator= DashboardConfig.get_locator("Create_New_User")
        self.click(locator)
    
    def add_new_user(self, email, first_name, family_name, middle_name, password):
        self.send_keys(self.Email, email)
        self.send_keys(self.First_Name, first_name)
        self.send_keys(self.Family_Name, family_name)
        self.send_keys(self.Middle_Name, middle_name)
        self.send_keys(self.Password, password)
        self.click(self.Create_Account)

    def get_error_toast(self):
        return self.toast_alert(self.Error_Alert)
    
    def get_success_toast(self):
        return self.toast_alert(self.Error_Alert).text

    def get_all_errors(self):
        return {
            "email": self.error_find_element(self.Email_Error_Message),
            "first_name": self.error_find_element(self.FirstName_Error_Message),
            "family_name": self.error_find_element(self.FamilyName_Error_Message),
            "password": self.error_find_element(self.Password_Error_Message)
        }
    
    def get_assignservicesurl(self):
        return AssignServices.get_assignservices_url()
    
    def all_services(self):
        services = self.find_elements(self.All_Services)
        data = []
        for service in services:
            element = service.text
            data.append(element)

        return data
    




from pages.base_page import Basepage
from utilities.read_properties import ReadConfig

class LoginPage(Basepage):
    Page_URL = ReadConfig.get_page_url()
    Username_Input = ReadConfig.get_locator("Username_Input")
    Password_Input = ReadConfig.get_locator("Password_Input")
    Login_Button = ReadConfig.get_locator("Login_Button")
    Toast_Alert = ReadConfig.get_locator("Toast_Alert")
    #Validate_login = ReadConfig.get_locator("Validate_Login_Successful")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        self.send_keys(self.Username_Input, username)

    def enter_password(self, password):
        self.send_keys(self.Password_Input, password)

    def click_login(self):
        self.click(self.Login_Button)

    def alert_message(self):
        return self.toast_alert(self.Toast_Alert)


    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
    
    def get_error_message(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self.alert_message()

    # def is_login_success(self):
    #     # REPLACE with your real success condition
    #     return self.driver.current_url.endswith("/home")

    def is_login_failed(self):
        return self.driver.find_element(*self.error_message).is_displayed()
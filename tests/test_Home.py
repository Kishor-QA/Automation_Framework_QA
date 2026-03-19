from pages.home_page import Home
import pytest
from utilities.custom_logger import Log_Maker
import time
import pandas as pd

class TestHome():
    logger = Log_Maker.log_gen()

    def load_Account(file_path="./Test_Data/Create_User.csv"):
        df = pd.read_csv(file_path, keep_default_na=False)
        # Convert DataFrame to list of tuples
        return list(df.itertuples(index=False))

    test_data = load_Account()

    def read_service_from_csv(file_path= "./Test_Data/Create_User.csv"):
        df = pd.read_csv(file_path= "./Test_Data/Create_User.csv")
        return df.loc[0, "service"]


    @pytest.mark.parametrize("Email,FirstName,FamilyName,MiddleName,Password,Case", test_data)
    def test_Create_New_User(self,dashboard,driver,Email,FirstName,FamilyName,MiddleName,Password,Case):
        print("<<<<<<<<<<<<<<<<Here>>>>>>>>>>>>>>>>")
        dashboard.create_new_user()
        time.sleep(10)
        print("<<<<<<<<Clicked the create new user >>>>>>>>>>>>>>>>>>>>>")
        current_url = driver.current_url
        self.logger.info(f"Current_URL is {current_url}") 
        try:
            assert current_url =="https://dev.wiseai.wiseyak.com/register"
        except AssertionError as e:
            self.logger.error(f"The error is {e}")
        
        home= Home(driver)
        print("<<<<<Adding New User>>>>>>>")
        print(Email,FirstName,FamilyName,MiddleName,Password,Case)
        if Case == "invalid":
            home.add_new_user(email=Email,first_name=FirstName,family_name=FamilyName,middle_name=MiddleName,password=Password)
            print("<<<<<<<New User Adding Comcpleted>>>>>>>>>")
            get_error_message = home.get_all_errors()

            error_message = ', '.join(
                f"{k}: {', '.join([e.text for e in v]) if isinstance(v, list) else v}"
                for k, v in get_error_message.items()
            )
            print(error_message)

        else:
            home.add_new_user(email=Email,first_name=FirstName,family_name=FamilyName,middle_name=MiddleName,password=Password)
            print("I am hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            time.sleep(3)
            current_url= driver.current_url
            print(f"The current url is {current_url}")
            expected_url = home.get_assignservicesurl()
            print(f"The expected url is {expected_url}")
            assert current_url == expected_url

            services = home.all_services()
            print(services)

            # if "Text to Speech (TTS)" in services:



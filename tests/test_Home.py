from pages.home_page import Home
import pytest
from utilities.custom_logger import Log_Maker
import time
import pandas as pd

class TestHome():
    logger = Log_Maker.log_gen()

    def load_Account(file_path="./Test_Data/Create_User.csv"):
        df = pd.read_csv(file_path)
        # Convert DataFrame to list of tuples
        return list(df.itertuples(index=False))

    test_data = load_Account()

    @pytest.mark.parametrize("Email,FirstName,FamilyName,MiddleName,Password", test_data)
    def test_Create_New_User(self,dashboard, driver,Email,FirstName,FamilyName,MiddleName,Password):
        print("<<<<<<<<<<<<<<<<Here>>>>>>>>>>>>>>>>")
        dashboard.create_new_user()
        time.sleep(10)
        print("<<<<<<<<Clicked the create new user >>>>>>>>>>>>>>>>>>>>>")
        current_url = driver.current_url
        print(current_url)
        assert current_url =="http://localhost:3000/register"
        home= Home(driver)
        print("<<<<<Adding New User>>>>>>>")
        home.add_new_user(email=Email,first_name=FirstName,family_name=FamilyName,midddle_name=MiddleName,password=Password)
        print("<<<<<<<New User Adding Comcpleted>>>>>>>>>")
        get_error = home.get_error_toast()
        print(get_error)
        self.logger.info(f"The error is {get_error}")
        


        





from selenium.webdriver.common.by import By
import configparser

config = configparser.ConfigParser()
config.read("./config/config.ini")

class ReadConfig:
    @staticmethod
    def get_page_url():
        return config.get("superowner login info", "Page_URL")

    @staticmethod
    def get_locator(name):
        locator = config.get("superowner login info", name)
        locator_type, locator_value = locator.split(',', 1)  
        return (getattr(By, locator_type.strip()), locator_value.strip())

class ClientConfig:
    @staticmethod
    def get_client_url():
        return config.get("ClientSectionPage", "Client_URL")
    @staticmethod
    def get_locator(name):
        locator = config.get("ClientSectionPage", name)
        locator_type, locator_value = locator.split(',', 1)
        return (getattr(By, locator_type.strip()), locator_value.strip())

    @staticmethod
    def get_dynamic_client_locator(client_name):
        locator_template = config.get("ClientSectionPage", "Dynamic_Client_Selection")
        locator_type, locator_value = locator_template.split(',', 1)
        formatted_locator = locator_value.format(client_name)
        return (getattr(By, locator_type.strip()), formatted_locator.strip())

class TeamConfig:
    @staticmethod
    def get_team_url():
        return config.get("TeamSectionPage", "Team_URL")
    @staticmethod
    def get_invite_url():
        return config.get("TeamSectionPage","Invite_Team_URL" )
    @staticmethod
    def get_locator(name):
        locator =config.get("TeamSectionPage", name)
        locator_type, locator_value = locator.split(',', 1)
        return (getattr(By, locator_type.strip()), locator_value.strip())
    
class TrainingConfig:
    @staticmethod
    def get_training_url():
        return config.get("TrainingSectionPage", "Location_URL")
    
    @staticmethod
    def get_locator(name):
        locator = config.get("TrainingSectionPage", name)
        locator_type, locator_value = locator.split(',', 1)
        return (getattr(By, locator_type.strip()), locator_value.strip())
    
class LocationConfig:
    @staticmethod
    def get_location_url():
        return config.get("LocationPage", "Location_URL")
    
    @staticmethod
    def get_dynamic_location(country_name):
        locator_template = config.get("LocationPage", "Select_Country")
        locator_type, locator_value = locator_template.split(',', 1)
        formatted_locator = locator_value.format(country_name)
        return (getattr(By, locator_type.strip()), formatted_locator.strip())
    
    @staticmethod
    def get_locator(name):
        locator = config.get("LocationPage", name)
        locator_type, locator_value = locator.split(',', 1)
        return (getattr(By, locator_type.strip()), locator_value.strip())
    
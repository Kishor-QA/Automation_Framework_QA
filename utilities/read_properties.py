from selenium.webdriver.common.by import By
import configparser

config = configparser.ConfigParser()
config.read("./config/config.ini")

class ReadConfig:
    @staticmethod
    def get_page_url():
        return config.get("", "")

    @staticmethod
    def get_locator(name):
        locator = config.get("", name)
        locator_type, locator_value = locator.split(',', 1)  
        return (getattr(By, locator_type.strip()), locator_value.strip())

class ClientConfig:
    @staticmethod
    def get_client_url():
        return config.get("", "")
    @staticmethod
    def get_locator(name):
        locator = config.get("", name)
        locator_type, locator_value = locator.split(',', 1)
        return (getattr(By, locator_type.strip()), locator_value.strip())

    @staticmethod
    def get_dynamic_client_locator(client_name):
        locator_template = config.get("", "")
        locator_type, locator_value = locator_template.split(',', 1)
        formatted_locator = locator_value.format(client_name)
        return (getattr(By, locator_type.strip()), formatted_locator.strip())

class TeamConfig:
    @staticmethod
    def get_team_url():
        return config.get("", "")
    @staticmethod
    def get_invite_url():
        return config.get("","" )
    @staticmethod
    def get_locator(name):
        locator =config.get("", name)
        locator_type, locator_value = locator.split(',', 1)
        return (getattr(By, locator_type.strip()), locator_value.strip())
    
class TrainingConfig:
    @staticmethod
    def get_training_url():
        return config.get("", "")
    
    @staticmethod
    def get_locator(name):
        locator = config.get("", name)
        locator_type, locator_value = locator.split(',', 1)
        return (getattr(By, locator_type.strip()), locator_value.strip())
    
class LocationConfig:
    @staticmethod
    def get_location_url():
        return config.get("", "")
    
    @staticmethod
    def get_dynamic_location(country_name):
        locator_template = config.get("", "")
        locator_type, locator_value = locator_template.split(',', 1)
        formatted_locator = locator_value.format(country_name)
        return (getattr(By, locator_type.strip()), formatted_locator.strip())
    
    @staticmethod
    def get_locator(name):
        locator = config.get("", name)
        locator_type, locator_value = locator.split(',', 1)
        return (getattr(By, locator_type.strip()), locator_value.strip())
    
from selenium import webdriver
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class GuviAutomation:
    # Init Constructor, Passing url
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()

    # starting automation method 
    def start_automation(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        return True
    
    # shutdown method
    def shutdown(self):
        # quit() method close all the browser instances
        self.driver.quit()

    # fetch the title
    def fetch_title(self):
        if self.start_automation():
            return self.driver.title
        else:
            return False
        
    # fetch the URL
    def fetch_url(self):
        if self.start_automation():
            return self.driver.current_url
        else:
            return False
        

    
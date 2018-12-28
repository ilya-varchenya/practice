from selenium import webdriver

from onliner_uat.web_elements.time_class_constants import TimeOutConstants


class BaseTest:
    def setup_class(self):
        self.driver = webdriver.Chrome(executable_path="drivers\chromedriver.exe")
        self.driver.implicitly_wait(TimeOutConstants.PAGE_LOAD_TIMEOUT)

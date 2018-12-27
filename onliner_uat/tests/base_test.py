from selenium import webdriver


class BaseTest:
    def setup_class(self):
        self.driver = webdriver.Chrome(executable_path="drivers\chromedriver.exe")
        self.driver.implicitly_wait(10)

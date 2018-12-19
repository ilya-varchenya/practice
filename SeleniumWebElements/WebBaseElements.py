from selenium import webdriver


class WebBaseElement:
    def __init__(self, driver):
        self.driver = driver

    def get_driver_and_page(self, driver_path, page_url):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.get(page_url)
        self.driver.implicitly_wait(10)

    def is_present(self, *val):
        if self.driver.find_element(*val):
            return True


    def is_not_present(self, *val):
        if not(self.driver.find_element(*val)):
            return True

    def get_text(self, *val):
        return self.driver.find_element(*val).text

    def get_attribute(self, val, key):
        return self.driver.find_element(*val).get_attribute(key)

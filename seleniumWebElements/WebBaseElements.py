from selenium import webdriver


class WebBaseElement:
    def __init__(self, by, value):
        self.by = by
        self.value = value

    def __get__(self, obj):
        self.driver = obj.driver

    def get_driver_and_page(self, driver_path, page_url):
        """
        Get driver and go to some web-page
        """
        try:
            self.driver = webdriver.Chrome(executable_path=driver_path)
            self.driver.get(page_url)
            self.driver.implicitly_wait(10)
            return self.driver
        except Exception:
            return False

    def is_present(self, by, value):
        """
        Check is element present
        """
        if self.driver.find_element(by, value):
            return True
        else:
            return False

    def is_not_present(self, by, value):
        """
        Check is element not present
        """
        if not(self.driver.find_element(by, value)):
            return True
        else:
            return False

    def get_text(self, by, value):
        """
        Get text from element
        """
        return self.driver.find_element(by, value).text

    def get_attribute(self, by, value, key):
        """
        Get attribute parameter
        """
        return self.driver.find_element(by, value).get_attribute(key)

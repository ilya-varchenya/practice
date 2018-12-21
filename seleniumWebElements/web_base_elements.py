from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from seleniumWebElements.time_class_constants import TimeOutConstants
from seleniumWebElements.web_helpers import WebHelpers


class WebBaseElement:
    def __init__(self, by, value):
        self.by = by
        self.value = value

    def __get__(self, obj):
        self.driver = obj.driver

    def get_element(self, timeout=TimeOutConstants.BUTTON_TIMEOUT):
        """
        Get element from page
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located((self.by, self.value)))
            WebHelpers.scroll(self.by, self.value)
            self.driver.find_element(self.by, self.value).click()
        except NoSuchElementException:
            return False
        return element

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

    def with_text(self, text):
        self.value = self.value.format(text)
        return self

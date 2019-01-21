import logging

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from onliner_uat.web_elements.time_class_constants import TimeOutConstants


class WebBaseElement:
    def __init__(self, by, value):
        self.by = by
        self.value = value

    def __get__(self, obj, owner):
        self.driver = obj.driver
        return self

    def get_element(self, timeout=TimeOutConstants.PAGE_LOAD_TIMEOUT):
        """
        Get element from page
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located((self.by, self.value)))
            logging.getLogger(__name__).info("Element is: {}".format(element))
        except NoSuchElementException:
            return False
        return element

    def get(self, timeout=TimeOutConstants.PAGE_LOAD_TIMEOUT):
        logging.getLogger(__name__).info("Element is: {}".format(self.get_element(timeout)))
        return self.get_element(timeout)

    def is_present(self):
        """
        Check is element present
        """
        logging.getLogger(__name__).info("Element is present")
        return self.driver.find_element(self.by, self.value)

    def is_not_present(self):
        """
        Check is element not present
        """
        logging.getLogger(__name__).info("Element is not present")
        return not(self.driver.find_element(self.by, self.value))

    def get_text(self):
        """
        Get text from element
        """
        logging.getLogger(__name__).info("Element text: {}".format(self.driver.find_element(self.by, self.value).text))
        return self.driver.find_element(self.by, self.value).text

    def get_attribute(self, key):
        """
        Get attribute parameter
        :param key: attribute name
        :return: attribute value
        """
        logging.getLogger(__name__).info(
            "Element attribute: {}".format(self.driver.find_element(self.by, self.value).get_attribute(key)))
        return self.driver.find_element(self.by, self.value).get_attribute(key)

    def with_text(self, text=''):
        self.value = self.value.format(text)
        return self

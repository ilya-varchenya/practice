from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from onliner_uat.web_elements.time_class_constants import TimeOutConstants
from onliner_uat.web_elements.web_base_element import WebBaseElement


class IClick(WebBaseElement):
    def __init__(self, by, value):
        self.by = by
        self.value = value
        WebBaseElement.__init__(self, by, value)

    def __get__(self, obj, owner):
        self.driver = obj.driver
        return self

    def is_clickable(self, timeout=TimeOutConstants.BUTTON_TIMEOUT):
        """
        Check is element clickable
        :param timeout: time of waiting for load element
        :return: boolean
        """
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable((self.by, self.value)))
        except NoSuchElementException:
            return False
        return True

    def click(self, timeout=TimeOutConstants.BUTTON_TIMEOUT):
        """
        Click on element
        :param timeout: time of waiting for load element
        :return: boolean
        """
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located((self.by, self.value)))
            self.driver.find_element(self.by, self.value).click()
        except NoSuchElementException:
            return False
        return True

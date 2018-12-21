from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from seleniumWebElements.WebHelpers import WebHelpers
from seleniumWebElements.WebElements import TimeOutConstants


class IClick:
    def __init__(self, by, value):
        self.by = by
        self.value = value

    def __get__(self, obj):
        self.driver = obj.driver

    def is_clickable(self, by, value, timeout=TimeOutConstants.BUTTON_TIMEOUT):
        """
        Check is element clickable
        """
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located((by, value)))
        except NoSuchElementException:
            return False
        return True

    def click(self, by, value, timeout=TimeOutConstants.BUTTON_TIMEOUT):
        """
        Click on element
        """
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located((by, value)))
            WebHelpers.scroll(by, value)
            self.driver.find_element(by, value).click()
        except NoSuchElementException:
            return False
        return True

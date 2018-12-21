from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from seleniumWebElements.web_helpers import WebHelpers
from seleniumWebElements.web_elements import TimeOutConstants


class IClick:
    def __init__(self, driver):
        self.driver = driver

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

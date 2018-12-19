from SeleniumWebElements.WebHelpers import WebHelpers

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class IClick:
    def __init__(self, driver):
        self.driver = driver

    def is_clickable(self, val, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located((val)))
            return True
        except TimeoutException:
            return False

    def click(self,  val, timeout=5):
        WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located((val)))
        WebHelpers.scroll(*val)
        self.driver.find_element(*val).click()

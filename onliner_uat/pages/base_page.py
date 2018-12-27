from onliner_uat.web_elements.time_class_constants import TimeOutConstants
from onliner_uat.web_elements.web_helpers import WebHelpers


class BasePage(WebHelpers):
    def __init__(self, driver):
        self.driver = driver

    def scroll(self, val):
        self.scroll(val)

    def click(self, val, timeout=TimeOutConstants.BUTTON_TIMEOUT):
        self.click(val, timeout)

    def is_open(self):
        pass

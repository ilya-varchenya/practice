from onliner_uat.web_elements.web_helpers import WebHelpers


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.helpers = WebHelpers

    def is_open(self):
        pass

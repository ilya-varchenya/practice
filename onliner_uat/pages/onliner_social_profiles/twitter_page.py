from selenium.webdriver.common.by import By

from onliner_uat.pages.base_page import BasePage
from onliner_uat.web_elements.web_elements import WebLabel


class TwitterPage(BasePage):
    twitter_header = WebLabel(By.XPATH, "//a[@class='ProfileHeaderCard-nameLink u-textInheritColor js-nav']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_open(self):
        return self.twitter_header.get_element()

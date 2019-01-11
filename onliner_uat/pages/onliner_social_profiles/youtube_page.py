from selenium.webdriver.common.by import By

from onliner_uat.pages.base_page import BasePage
from onliner_uat.web_elements.web_elements import WebLabel


class YouTubePage(BasePage):
    youtube_header = WebLabel(By.XPATH, "//h1[@class='c4-tabbed-header-title']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_open(self):
        return self.youtube_header.get_element()

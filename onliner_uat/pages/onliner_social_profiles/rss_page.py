from selenium.webdriver.common.by import By

from onliner_uat.pages.base_page import BasePage
from onliner_uat.web_elements.web_elements import WebLabel


class RSSPage(BasePage):
    rss_header = WebLabel(By.XPATH, "//h2[@class='page_name']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_open(self):
        return self.rss_header.get_element()

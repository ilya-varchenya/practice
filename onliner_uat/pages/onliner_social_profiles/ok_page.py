from selenium.webdriver.common.by import By

from onliner_uat.pages.base_page import BasePage
from onliner_uat.web_elements.web_elements import WebLabel


class OKPage(BasePage):
    ok_header = WebLabel(By.XPATH, "//h1[@class='mctc_name_tx']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_open(self):
        return self.ok_header.get_element()

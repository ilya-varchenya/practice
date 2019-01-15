from selenium.webdriver.common.by import By

from onliner_uat.pages.base_page import BasePage
from onliner_uat.web_elements.web_elements import WebLabel


class CatalogCertainItemPage(BasePage):
    description_of_item = WebLabel(By.XPATH, "//div[@class = 'offers-description__specs']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_text_from_description(self):
        return self.description_of_item.get_text()

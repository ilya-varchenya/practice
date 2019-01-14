from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from onliner_uat.pages.base_page import BasePage
from onliner_uat.web_elements.time_class_constants import TimeOutConstants
from onliner_uat.web_elements.web_elements import WebLink, WebLabel
from onliner_uat.pages.news_page import NewsPage
from onliner_uat.pages.catalog_page import CatalogPage


class StartPage(BasePage):
    people = WebLabel(By.XPATH, "//*[text()='Люди']")
    news_tip = WebLink(By.XPATH, "//ul[@class = 'b-main-navigation']//span[contains(text(), 'Новости')]")
    news_tip_active = WebLink(By.XPATH, "//li[contains(@class, 'b-main-navigation__item_active')]//span[contains(text(), 'Новости')]")
    subsections_headers = WebLabel(By.XPATH, "//header[@class='b-main-page-blocks-header-2 cfix']")
    red_tip = WebLabel(By.XPATH, "//div[contains(normalize-space(@class), 'news-tidings__button_views_popular')]")

    people_tip = WebLink(By.XPATH, "//div[@class = 'b-main-navigation__dropdown-title']//a[contains(text(), 'Люди')]")
    catalog_tip = WebLink(By.XPATH, "//span[@class = 'b-main-navigation__text']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_open(self):
        return self.people.get_element()

    def is_news_able(self):
        return self.news_tip.is_clickable()

    def are_subsections_have_correct_names(self, bar_items):
        return [item.value for item in bar_items] == self.subsections_headers.get_text_from_amount_of_elements()

    def is_news_underlined(self):
        self.helpers.move_to_element(self, self.news_tip)
        return self.news_tip_active.get()

    def is_element_red(self):
        list_of_text = self.red_tip.get_text_from_amount_of_elements()
        list_of_more_30k = [i for i in list_of_text if i > 30000]

        return list_of_text == list_of_more_30k

    def go_to_people_page(self):
        self.helpers.move_to_element(self, self.news_tip)
        # wait for item
        WebDriverWait(self.driver, TimeOutConstants.BUTTON_TIMEOUT).\
            until(expected_conditions.presence_of_element_located((self.people_tip.by, self.people_tip.value)))
        self.people_tip.click()
        return NewsPage(self.driver)

    def go_to_catalog_page(self):
        self.catalog_tip.click()
        return CatalogPage(self.driver)

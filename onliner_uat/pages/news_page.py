from selenium.webdriver.common.by import By

from onliner_uat.pages.base_page import BasePage
from onliner_uat.web_elements.web_elements import WebLink, WebLabel
from onliner_uat.pages.certain_news_page import CertainNewsPage


class NewsPage(BasePage):
    active_tab = WebLabel(By.XPATH, "//li[contains(@class, 'project-navigation__item_active')]")
    predicted_text = 'люди'

    news_title = WebLink(By.XPATH, "//div[@class = 'news-tidings__subtitle']")
    title = WebLink(By.XPATH, "//div[@class = 'news-header__title']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_bar_selected(self):
        text_of_active_tab = self.active_tab.get_text().lower()

        if text_of_active_tab == self.predicted_text:
            return True
        else:
            return False

    def is_titles_similar(self):
        text_of_title_on_news_page = self.news_title.get_text().lower()
        self.news_title.click()
        text_of_title = self.title.get_text().lower()

        if text_of_title_on_news_page == text_of_title:
            return True
        else:
            return False

    def go_to_certain_news_page(self):
        self.news_title.click()
        return CertainNewsPage(self.driver)


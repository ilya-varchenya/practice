from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from onliner_uat.pages.base_page import BasePage
from onliner_uat.web_elements.web_elements import WebLink, WebLabel
from onliner_uat.pages.certain_news_page import CertainNewsPage


class NewsPage(BasePage):
    active_tab = WebLabel(By.XPATH, "//li[contains(@class, 'project-navigation__item_active')]")
    predicted_text = 'люди'

    first_news_title = WebLink(By.XPATH, "//div[@class = 'news-tidings__subtitle']")
    title = WebLink(By.XPATH, "//div[@class = 'news-header__title']")
    news_elements = WebLink(By.XPATH, "//div[@class='news-tidings__item news-tidings__item_1of3 news-tidings__item_condensed']")

    news_title = WebLink(By.XPATH, "//div[@class='news-tidings__preview']")
    news_text_preview = WebLink(By.XPATH, "//div[@class='news-tidings__speech']")
    news_image = WebLink(By.XPATH, "//div[@class='news-tidings__image']")
    news_number_of_views = WebLink(By.XPATH, "//div[@class='news-tidings__group']")
    news_number_of_comments = WebLink(By.XPATH, "//div[@class='news-tidings__comment']")
    news_publishing_date = WebLink(By.XPATH, "//div[@class='news-tidings__time']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_bar_selected(self):
        text_of_active_tab = self.active_tab.get_text().lower()

        if text_of_active_tab == self.predicted_text:
            return True
        else:
            return False

    def is_titles_similar(self):
        text_of_title_on_news_page = self.first_news_title.get_text().lower()
        self.first_news_title.click()
        text_of_title = self.title.get_text().lower()

        if text_of_title_on_news_page == text_of_title:
            return True
        else:
            return False

    def is_have_all_atr(self):
        list_of_elements = self.news_elements.get_text_from_amount_of_elements()

        list_of_attributes = [
            self.news_title,
            self.news_text_preview,
            self.news_image,
            self.news_number_of_views,
            self.news_number_of_comments,
            self.news_publishing_date
        ]
        flag = True

        for i in list_of_elements:
            for j in list_of_attributes:
                try:
                    i.find_element(j)
                except NoSuchElementException:
                    flag = False
        return flag

    def go_to_certain_news_page(self):
        self.first_news_title.click()
        return CertainNewsPage(self.driver)

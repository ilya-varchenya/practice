from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from onliner_uat.pages.base_page import BasePage
from onliner_uat.web_elements.web_elements import WebLink, WebLabel
from onliner_uat.pages.certain_news_page import CertainNewsPage


class NewsPage(BasePage):
    active_tab = WebLabel(By.XPATH, "//li[contains(@class, 'project-navigation__item_active')]")
    predicted_text_of_label = 'люди'

    first_news_link = WebLink(By.XPATH, "//a[@class = 'news-tidings__stub']")
    first_news = WebLink(By.XPATH, "//a[@class = 'news-tidings__link']//span")
    news_preview_title = WebLabel(By.XPATH, "//div[@class='news-tidings__subtitle']")
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

    def is_bar_selected(self, item):
        text_of_active_tab = self.active_tab.get_text().lower()
        return text_of_active_tab == item.value

    def get_text_of_first_news(self):
        return self.first_news.get_text().lower()

    def is_all_components_of_news_block_present(self):
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

    def is_news_block_tittle_present(self):
        list_of_elements = self.news_elements.get_text_from_amount_of_elements()

        flag = True

        for i in list_of_elements:
            try:
                i.find_element(self.news_title)
            except NoSuchElementException:
                flag = False
        return flag

    def is_news_block_text_preview_present(self):
        list_of_elements = self.news_elements.get_text_from_amount_of_elements()

        flag = True

        for i in list_of_elements:
            try:
                i.find_element(self.news_text_preview)
            except NoSuchElementException:
                flag = False
        return flag

    def is_news_block_image_present(self):
        list_of_elements = self.news_elements.get_text_from_amount_of_elements()

        flag = True

        for i in list_of_elements:
            try:
                i.find_element(self.news_image)
            except NoSuchElementException:
                flag = False
        return flag

    def is_news_block_number_of_views_present(self):
        list_of_elements = self.news_elements.get_text_from_amount_of_elements()

        flag = True

        for i in list_of_elements:
            try:
                i.find_element(self.news_number_of_views)
            except NoSuchElementException:
                flag = False
        return flag

    def is_news_block_number_of_comments_present(self):
        list_of_elements = self.news_elements.get_text_from_amount_of_elements()

        flag = True

        for i in list_of_elements:
            try:
                i.find_element(self.news_number_of_comments)
            except NoSuchElementException:
                flag = False
        return flag

    def is_news_block_publishing_date_present(self):
        list_of_elements = self.news_elements.get_text_from_amount_of_elements()

        flag = True

        for i in list_of_elements:
            try:
                i.find_element(self.news_publishing_date)
            except NoSuchElementException:
                flag = False
        return flag

    def go_to_certain_news_page(self):
        self.first_news_link.click()
        return CertainNewsPage(self.driver)


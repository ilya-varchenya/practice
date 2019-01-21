from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from onliner_uat.pages.base_page import BasePage
from onliner_uat.web_elements.web_elements import WebLink, WebButton, WebLabel
from onliner_uat.pages.onliner_social_profiles import (YouTubePage, InstagramPage, TwitterPage, OKPage,
                                                       FacebookPage, VKPage, ConnectWithRedactionPage, RSSPage)
from onliner_uat.utils.regex_utils import get_number_from_string


class CertainNewsPage(BasePage):
    comments_section = WebLink(By.XPATH, "//div[@id= 'comments']")
    more_comments_button = WebButton(By.XPATH, "//div[@class= 'news-form__control news-form__control_condensed']")
    amount_of_comments = WebLabel(By.XPATH, "//div[@class= 'news-form__title news-form__title_middle']")
    news_title = WebLabel(By.XPATH, "//div[@class='news-header__title']")
    discussion_tittle = WebLabel(By.XPATH, "//div[@class='news-comment__title news-comment__title_secondary']")
    arrow_button_up = WebButton(By.XPATH, "//span[contains(@class, 'js-scrolling-button-up')]")
    arrow_button_down = WebButton(By.XPATH, "//span[contains(@class, 'js-scrolling-button-down')]")
    onliner_social_profile_tip = WebButton(By.XPATH, "//a[@class='project-navigation__link project-navigation__link_secondary']")

    youtube_onliner_profile = WebLink(By.XPATH, "//a[@title='Youtube']")
    instagram_onliner_profile = WebLink(By.XPATH, "//a[@title='Instagram']")
    twitter_onliner_profile = WebLink(By.XPATH, "//a[@title='Twitter']")
    ok_onliner_profile = WebLink(By.XPATH, "//a[@title='OK']")
    facebook_onliner_profile = WebLink(By.XPATH, "//a[@title='Facebook']")
    vk_onliner_profile = WebLink(By.XPATH, "//a[@title='VK']")
    connect_to_redaction_onliner_profile = WebLink(By.XPATH, "//a[@title='Связаться с редакцией']")
    rss_onliner_profile = WebLink(By.XPATH, "//a[@title='RSS']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_open(self):
        return self.news_title.get_element()

    def is_comments_present(self):
        return self.comments_section.get_element()

    def is_amount_of_comments_more_then_100(self):
        try:
            self.more_comments_button.click()
        except NoSuchElementException:
            return False
        finally:
            number_list = get_number_from_string(self.amount_of_comments.get_text())
            number = int(number_list[0])
            return number > 100

    def is_expand_the_list_of_comments(self):
        try:
            self.more_comments_button.click()
            return True
        except NoSuchElementException:
            return None

    def get_text_of_tittle(self):
        return self.news_title.get_text().lower()

    def is_arrows_navigate_to_the_start_of_page(self):
        if self.helpers.move_to_element(self, self.discussion_tittle):
            return self.arrow_button_up.is_clickable()

    def is_arrows_navigate_to_the_end_of_page(self):
        if self.helpers.move_to_element(self, self.discussion_tittle):
            return self.arrow_button_down.is_clickable()

    def go_to_youtube_onliner_profile(self):
        self.youtube_onliner_profile.click()
        return YouTubePage(self.driver)

    def go_to_instagram_onliner_profile(self):
        self.instagram_onliner_profile.click()
        return InstagramPage(self.driver)

    def go_to_twitter_onliner_profile(self):
        self.twitter_onliner_profile.click()
        return TwitterPage(self.driver)

    def go_to_ok_onliner_profile(self):
        self.ok_onliner_profile.click()
        return OKPage(self.driver)

    def go_to_facebook_onliner_profile(self):
        self.facebook_onliner_profile.click()
        return FacebookPage(self.driver)

    def go_to_vk_onliner_profile(self):
        self.vk_onliner_profile.click()
        return VKPage(self.driver)

    def go_to_connect_to_redaction_onliner_profile(self):
        self.connect_to_redaction_onliner_profile.click()
        return ConnectWithRedactionPage(self.driver)

    def go_to_rss_onliner_profile(self):
        self.rss_onliner_profile.click()
        return RSSPage(self.driver)

import re

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from onliner_uat.pages.base_page import BasePage
from onliner_uat.web_elements.web_elements import WebLink, WebButton, WebLabel


class CertainNewsPage(BasePage):
    comments_section = WebLink(By.XPATH, "//div[@id= 'comments']")
    more_comments_button = WebButton(By.XPATH, "//div[@class= 'news-form__control news-form__control_condensed']")
    amount_of_comments = WebLabel(By.XPATH, "//div[@class= 'news-form__title news-form__title_middle']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_comments_present(self):
        if self.comments_section.get_element():
            return True
        else:
            return False

    def is_amount_of_comments_more_then_100(self):
        try:
            self.more_comments_button.click()
            number = re.findall(r'\b\d+\b', self.amount_of_comments.get_text())
            number = number[0]
            if number > 100:
                return True
            else:
                return False
        except NoSuchElementException:
            return False

    def is_expand_the_list_of_comments(self):
        try:
            self.more_comments_button.click()
            return True
        except NoSuchElementException:
            return False

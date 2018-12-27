from selenium.webdriver.common.by import By

from onliner_uat.pages.base_page import BasePage
from onliner_uat.web_elements.web_elements import WebLink, WebLabel

class StartPage(BasePage):
    people = (By.XPATH, "//*[text()='Люди']")
    news_tip = WebLink(By.XPATH, "//li[contains(@class, 'b-main-navigation__item b-main-navigation__item_arrow')]//span[contains(text(), 'Новости')]")
    subsections_headers = WebLabel(By.XPATH, "//header[@class='b-main-page-blocks-header-2 cfix']")


    def __init__(self, driver):
        super().__init__(driver)

    def is_open(self):
        if self.driver.find_element(*self.people):
            return True
        else:
            return False

    def is_news_able(self):
        if self.news_tip.is_clickable():
            return True
        else:
            return False

    def is_subsections_visible(self):
        list_of_subsections = ("Люди", "Мнения", "Авто", "Технологии", "Недвижимость", "Форум")
        list_of_text = self.subsections_headers.get_text_from_amount_of_elements()
        flag = True

        for i in list_of_subsections:
            if i.lower() not in list_of_text:
                flag = False
            else:
                flag = True
        return flag

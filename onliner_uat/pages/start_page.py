from selenium.webdriver.common.by import By

from onliner_uat.pages.base_page import BasePage
from onliner_uat.web_elements.web_elements import WebLink, WebLabel
from onliner_uat.pages.news_page import NewsPage


class StartPage(BasePage):
    people = WebLabel(By.XPATH, "//*[text()='Люди']")
    news_tip = WebLink(By.XPATH, "//ul[@class = 'b-main-navigation']//span[contains(text(), 'Новости')]")
    news_tip_active = WebLink(By.XPATH, "//li[contains(@class, 'b-main-navigation__item_active')]//span[contains(text(), 'Новости')]")
    subsections_headers = WebLabel(By.XPATH, "//header[@class='b-main-page-blocks-header-2 cfix']")
    ret_tip = WebLabel(By.XPATH, "//span[contains(@class, 'complementary-item views views_popular')]")

    people_tip = WebLink(By.XPATH, "//div[@class = 'b-main-navigation__dropdown-title']//a[contains(text(), 'Люди')]")

    def __init__(self, driver):
        super().__init__(driver)

    def is_open(self):
        if self.people.get_element():
            return True
        else:
            return False

    def is_news_able(self):
        if self.news_tip.is_clickable():
            return True
        else:
            return False

    def are_subsections_have_correct_names(self):
        list_of_subsections = ("Люди", "Мнения", "Авто", "Технологии", "Недвижимость", "Форум")
        list_of_text = self.subsections_headers.get_text_from_amount_of_elements()
        flag = True

        for i in list_of_subsections:
            if i.lower() not in list_of_text:
                flag = False
            else:
                flag = True
        return flag

    def is_news_underlined(self):
        self.helpers.move_to_appear(self, self.news_tip, self.news_tip_active)
        if self.news_tip_active.get():
            return True
        else:
            return False

    def is_red(self):
        list_of_text = self.ret_tip.get_text_from_amount_of_elements()
        flag = True

        for i in list_of_text:
            # delete all spaces
            if ' ' in i:
                i = i.replace(" ", "")
            # check is number more then 30k
            if int(i) < 30000:
                flag = False
            else:
                flag = True
        return flag

    def go_to_people_page(self):
        self.helpers.move_to_element(self, self.news_tip, self.people_tip)
        self.people_tip.click()
        return NewsPage(self.driver)

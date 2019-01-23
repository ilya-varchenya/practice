from selenium.webdriver.common.by import By

from onliner_uat.pages.base_page import BasePage
from onliner_uat.pages.cart_page import CartPage
from onliner_uat.pages.catalog_certain_group_page import CertainCatalogGroupPage
from onliner_uat.web_elements.web_elements import WebLink, WebLabel, WebButton


class CatalogPage(BasePage):
    cart_link = WebLink(By.XPATH, "//a[@class = 'b-top-navigation-cart__link']")
    catalog_bar_tip = WebLink(By.XPATH, "//span[@class = 'catalog-navigation-classifier__item-title']")
    catalog_subcategories = WebLabel(By.XPATH, "//div[@class = 'catalog-navigation-list__category']")
    catalog_subcategories_tip = WebLink(By.XPATH, "//div[@class = 'catalog-navigation-list__aside-title' and contains(normalize-space(text()), '{}')]")
    first_catalog_subcategories_right_tip = WebLink(By.CSS_SELECTOR, "//a[@class = 'catalog-navigation-list__dropdown-item']")
    second_catalog_subcategories_right_tip = WebLink(By.CSS_SELECTOR, "//div[@class = 'catalog-navigation-list__beside'][style = 'display: none;']")
    certain_subcategories_right_tip = WebLink(By.XPATH, "//a[@class = 'catalog-navigation-list__dropdown-item']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_concrete_catalog_item_open(self):
        return self.certain_subcategories_right_tip.is_present()

    def go_to_cart_page(self):
        self.cart_link.click()
        return CartPage(self.driver)

    def is_catalog_subtitles_visible(self, bar_items):
        list_of_elements_text = self.catalog_bar_tip.get_text_from_amount_of_elements()
        list_of_bar_items = [bar_item.value for bar_item in bar_items]
        return list_of_elements_text == list_of_bar_items

    def is_catalog_subcategories_visible(self):
        self.helpers.move_to_element(self, self.catalog_bar_tip)
        return self.catalog_subcategories.get_element()

    def is_catalog_subcategories_list_changed(self):
        self.catalog_bar_tip.click()
        if self.first_catalog_subcategories_right_tip.is_present():
            self.catalog_subcategories_tip.click()
        return self.second_catalog_subcategories_right_tip

    def is_navigate_to_concrete_catalog_item(self):
        self.catalog_bar_tip.click()
        self.catalog_subcategories_tip.click()
        return self.is_concrete_catalog_item_open()

    def go_to_certain_catalog_group(self, name_of_tip):
        self.catalog_bar_tip.click()
        self.catalog_subcategories_tip.with_text(name_of_tip).click()
        self.certain_subcategories_right_tip.click()
        return CertainCatalogGroupPage(self.driver)

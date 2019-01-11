from selenium.webdriver.common.by import By

from onliner_uat.pages.base_page import BasePage
from onliner_uat.web_elements.web_elements import WebLink, WebLabel, WebButton
from onliner_uat.pages.cart_page import CartPage


class CatalogPage(BasePage):
    cart_link = WebLink(By.XPATH, "//a[@class = 'b-top-navigation-cart__link']")
    catalog_bar_tip = WebLink(By.XPATH, "//span[@class = 'catalog-navigation-classifier__item-title']")
    catalog_subcategories = WebLabel(By.XPATH, "//div[@class = 'catalog-navigation-list__category']")
    catalog_subcategories_tip = WebButton(By.XPATH, "//div[@class = 'catalog-navigation-list__aside-item']")
    first_catalog_subcategories_right_tip = \
        WebLink(By.CSS_SELECTOR, "div[class = 'catalog-navigation-list__beside']")
    second_catalog_subcategories_right_tip = \
        WebLink(By.CSS_SELECTOR, "div[class = 'catalog-navigation-list__beside'][style = 'display: none;']")

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_cart_page(self):
        self.cart_link.click()
        return CartPage(self.driver)

    def is_catalog_subtitles_visible(self, bar_items):
        list_of_elements_text = self.catalog_bar_tip.get_text_from_amount_of_elements()
        list_of_bar_items = [bar_item.value for bar_item in bar_items]
        similarity = [bar_item == element for bar_item in list_of_bar_items for element in list_of_elements_text]
        return any(similarity)

    def is_catalog_subcategories_visible(self):
        self.helpers.move_to_element(self, self.catalog_bar_tip)
        return self.catalog_subcategories.get_element()

    def is_catalog_subcategories_list_changed(self):
        self.catalog_bar_tip.click()
        if self.first_catalog_subcategories_right_tip.is_present():
            self.catalog_subcategories_tip.click()
        return self.second_catalog_subcategories_right_tip

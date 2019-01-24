from selenium.webdriver.common.by import By

from onliner_uat.pages.base_page import BasePage
from onliner_uat.pages.catalog_certain_item_page import CatalogCertainItemPage
from onliner_uat.utils.regex_utils import get_list_of_numbers_from_string

from onliner_uat.pages.catalog_comparison_page import CatalogComparisonPage
from onliner_uat.web_elements.web_elements import WebCheckBox, WebButton, WebLabel, WebLink, WebElementList


class CertainCatalogGroupPage(BasePage):
    with_delivery_in_bel_tip = WebCheckBox(By.XPATH, "//span[@class = 'schema-filter__checkbox-text' and text() = 'С доставкой по Беларуси']")
    amount_of_results_tip = WebButton(By.XPATH, "//div[contains(@class, 'schema-filter-button__state_initial')]")
    title_of_item = WebLink(By.XPATH, "//div[@class = 'schema-product__title']")
    preview_of_item = WebLabel(By.XPATH, "//span[@data-bind='html: product.description']")
    choice_check_boxes = WebElementList(By.XPATH, "//div[@class='schema-product schema-product_narrow-sizes']//span[@class = 'i-checkbox__faux']")
    comparison_tip = WebLink(By.XPATH, "//a[@class = 'compare-button__sub compare-button__sub_main']")
    cheap_order_tip = WebButton(By.XPATH, "//div[@class = 'schema-order__item']")
    list_of_prices = WebElementList(By.XPATH, "//div[@class = 'schema-product__price']//span")
    order_tip = WebButton(By.XPATH, "//a[@class = 'schema-order__link']")


    def __init__(self, driver):
        super().__init__(driver)

    def is_filter_response(self):
        return self.with_delivery_in_bel_tip.click() and self.amount_of_results_tip.click()

    def get_text_of_preview(self):
        return self.preview_of_item.get_text()

    def go_to_certain_catalog_group(self):
        self.title_of_item.click()
        return CatalogCertainItemPage(self.driver)

    def is_list_of_items_filtered_cheap_first(self):
        self.order_tip.click()
        self.cheap_order_tip.click()
        list_of_prices = self.list_of_prices.get_text_from_amount_of_elements()
        # get list of numbers from list of strings
        list_of_numbers = []
        for i in list_of_prices:
            list_of_numbers.append(get_list_of_numbers_from_string(i)[0])

        is_list_sorted = True
        for i in range(len(list_of_numbers) - 1):
            if list_of_numbers[i] > list_of_numbers[i + 1]:
                is_list_sorted = False
                break
        return is_list_sorted

    def is_first_in_column_items_checked(self, number_of_checked_items=3):
        list_of_checked = []

        list_of_elements = self.choice_check_boxes.get_elements()
        counter = number_of_checked_items
        for i in list_of_elements:
            list_of_checked.append(i.click())
            counter -= 1
            if counter == 0:
                break
        return len(list_of_checked) == number_of_checked_items

    def go_to_comparison_page(self):
        self.is_first_in_column_items_checked()
        self.comparison_tip.click()
        return CatalogComparisonPage(self.driver)

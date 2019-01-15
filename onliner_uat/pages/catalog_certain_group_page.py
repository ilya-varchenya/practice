from selenium.webdriver.common.by import By

from onliner_uat.pages.base_page import BasePage
from onliner_uat.pages.catalog_certain_item_page import CatalogCertainItemPage
from onliner_uat.web_elements.web_elements import WebCheckBox, WebButton, WebLabel, WebLink


class CertainCatalogGroupPage(BasePage):
    with_delivery_in_bel_tip = WebCheckBox(By.XPATH, "//span[@class = 'schema-filter__checkbox-text' and text() = 'С доставкой по Беларуси']")
    amount_of_results_tip = WebButton(By.XPATH, "//div[contains(@class, 'schema-filter-button__state_initial')]")
    title_of_item = WebLink(By.XPATH, "//div[@class = 'schema-product__title']")
    preview_of_item = WebLabel(By.XPATH, "//span[@data-bind='html: product.description']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_filter_response(self):
        return self.with_delivery_in_bel_tip.click() and self.amount_of_results_tip.click()

    def get_text_of_preview(self):
        return self.preview_of_item.get_text()

    def go_to_certain_catalog_group(self):
        self.title_of_item.click()
        return CatalogCertainItemPage(self.driver)

from selenium.webdriver.common.by import By

from onliner_uat.pages.base_page import BasePage
from onliner_uat.web_elements.web_elements import WebLabel, WebElementList
from onliner_uat.utils.regular_expressions_service import get_number_from_string


class CatalogComparisonPage(BasePage):
    comparison_column = WebElementList(By.XPATH, "//td[contains(@class, 'product-table__cell')]")
    comparison_column_highlighted = WebLabel(By.XPATH, "//td[contains(normalize-space(@class), 'product-table__cell product-table__cell_accent')]")

    def __init__(self, driver):
        super().__init__(driver)

    def is_the_best_of_first_sections_highlighted(self):
        # get list of class-attribute values and text values OF ALL sells
        list_of_class_values = self.comparison_column.get_attribute('class')
        list_of_text = self.comparison_column.get_text_from_amount_of_elements()

        list_of_4_items_class_values = []
        list_of_4_items_text = []
        is_highlighted = True

        for i in range(len(list_of_class_values)):
            # get four items from lists
            list_of_4_items_class_values.append(list_of_class_values[i])
            list_of_4_items_text.append(list_of_text[i])

            # if lists_of_4_elements contains 4 elements check them for highlighted sells
            if i + 1 % 4 == 0:
                max_el = 0
                position = 0
                for item in range(len(list_of_4_items_text)):
                    number = get_number_from_string(list_of_text[item])
                    if max_el < number:
                        max_el = number
                        position = item

                if "product-table__cell_accent" not in list_of_class_values[position]:
                    is_highlighted = False
        return is_highlighted

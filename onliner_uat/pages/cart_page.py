from selenium.webdriver.common.by import By

from onliner_uat.pages.base_page import BasePage
from onliner_uat.web_elements.web_elements import WebLabel


class CartPage(BasePage):
    empty_cart_text = WebLabel(By.XPATH, "//div[@class = 'cart-message__description']")
    predicted_text = "Ваша корзина пуста"

    def __init__(self, driver):
        super().__init__(driver)

    def is_empty_cart_text_present(self):
        return self.predicted_text in self.empty_cart_text.get_text()

from SeleniumWebElements.WebBaseElements import WebBaseElement
from SeleniumWebElements.IClick import IClick
from SeleniumWebElements.WebHelpers import WebHelpers

class WebLabel(WebBaseElement):
    def __init__(self, driver):
        super().__init__(driver)

    def get_text(self, val):
        return self.driver.find_element(*val).text

    def get_text_as_int(self, val):
        return int(self.driver.find_element(*val).text)

class WebButton(WebBaseElement):
    def __init__(self, driver):
        super().__init__(driver)

    def click(self, val):
        IClick.click(val)

    def is_clickable(self, val):
        IClick.is_clickable(val)

    def pause(self, timeout):
        WebHelpers.pause(timeout)

class WebInput(WebBaseElement):
    def __init__(self, driver):
        super().__init__(driver)

    def clear(self, val):
        self.driver.find_element(*val).clear()

    def set_text(self, *val, input_text):
        self.driver.find_element(*val).send_keys(input_text)
        pass


class WebRadioButton(WebBaseElement):
    def __init__(self, driver):
        super().__init__(driver)

    def set_choice(self, val):
        self.driver.find_element(*val).click()

    def is_checked(self, val):
        if self.driver.findElements(*val).getAttribute("checked"):
            return True
        else:
            return False

class WebCheckBox(WebBaseElement):
    def __init__(self, driver):
        super().__init__(driver)

    def set_choice(self, val):
        self.driver.find_element(*val).click()

    def is_checked(self, val):
        if self.driver.findElements(*val).is_selected():
            return True
        else:
            return False


class WebLink(WebBaseElement):
    def __init__(self, driver):
        super().__init__(driver)

    def click(self, val):
        IClick.click(val)

    def is_clickable(self, val):
        IClick.is_clickable(val)

    def pause(self, timeout):
        WebHelpers.pause(timeout)

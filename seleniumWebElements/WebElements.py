from seleniumWebElements.WebBaseElements import WebBaseElement
from seleniumWebElements.IClick import IClick
from seleniumWebElements.WebHelpers import WebHelpers

class Constants:
    pageLoadTimeout = 10
    linkLoadTimeout = pageLoadTimeout
    buttonTimeout = 3

class WebLabel(WebBaseElement):
    def __init__(self, driver):
        super().__init__(driver)


    def get_text(self, val):
        return self.driver.find_element(*val).text


    def get_text_as_int(self, val):
        try:
            return int(self.driver.find_element(*val).text)
        except ValueError:
            return False


class WebButton(WebBaseElement, IClick, Constants):
    def __init__(self, driver):
        super().__init__(driver)


    def click(self,  val, timeout=Constants.buttonTimeout):
        self.click(val, timeout)


    def is_clickable(self, val, timeout=Constants.buttonTimeout):
        self.is_clickable(val, timeout)


    def pause(self, timeout):
        WebHelpers.pause(timeout)


class WebInput(WebBaseElement):
    def __init__(self, driver):
        super().__init__(driver)


    def clear(self, val):
        self.driver.find_element(*val).clear()


    def set_text(self, *val, input_text):
        self.clear(val)
        self.driver.find_element(*val).send_keys(input_text)



class WebRadioButton(WebBaseElement):
    def __init__(self, driver):
        super().__init__(driver)


    def set_choice(self, val):
        self.driver.find_element(*val).click()


    def is_checked(self, val):
        return self.driver.findElements(*val).getAttribute("checked")


class WebCheckBox(WebBaseElement):
    def __init__(self, driver):
        super().__init__(driver)


    def set_choice(self, val):
        self.driver.find_element(*val).click()


    def is_checked(self, val):
        return self.driver.findElements(*val).getAttribute('selected')


class WebLink(WebBaseElement, IClick):
    def __init__(self, driver):
        super().__init__(driver)


    def click(self,  val, timeout=Constants.linkLoadTimeout):
        self.click(val, timeout)


    def is_clickable(self, val, timeout=Constants.linkLoadTimeout):
        self.is_clickable(val, timeout)

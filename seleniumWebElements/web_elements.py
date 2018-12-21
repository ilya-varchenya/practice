from seleniumWebElements.web_base_elements import WebBaseElement
from seleniumWebElements.IClick import IClick
from seleniumWebElements.time_class_constants import TimeOutConstants


class WebLabel(WebBaseElement):
    def __init__(self, by, value):
        self.by = by
        self.value = value
        WebBaseElement.__init__(self, by, value)

    def get_text(self, by, value):
        """
        Get text from element
        """
        return self.driver.find_element(by, value).text

    def get_text_as_int(self, by, value):
        """
        Get text from element as integer
        """
        try:
            return int(self.driver.find_element(by, value).text)
        except ValueError:
            return False


class WebButton(WebBaseElement, IClick):
    def __init__(self, by, value):
        self.by = by
        self.value = value
        WebBaseElement.__init__(self, by, value)


    def click(self, by, value, timeout=TimeOutConstants.BUTTON_TIMEOUT):
        """
        Click on element
        """
        self.click(by, value, timeout)

    def is_clickable(self, by, value, timeout=TimeOutConstants.BUTTON_TIMEOUT):
        """
        Check is element clickable
        """
        self.is_clickable(by, value, timeout)


class WebInput(WebBaseElement):
    def __init__(self, by, value):
        self.by = by
        self.value = value
        WebBaseElement.__init__(self, by, value)

    def clear(self, by, value):
        """
        Clear input text fields
        """
        self.driver.find_element(by, value).clear()

    def set_text(self, by, value, input_text):
        """
        Clear input text fields and type text there
        """
        self.clear(by, value)
        self.driver.find_element(by, value).send_keys(input_text)


class WebRadioButton(WebBaseElement):
    def __init__(self, by, value):
        self.by = by
        self.value = value
        WebBaseElement.__init__(self, by, value)

    def check(self, by, value):
        """
        Check some choice
        """
        self.driver.find_element(by, value).click()

    def is_checked(self, by, value):
        """
        Check is element checked
        """
        return self.driver.findElements(by, value).getAttribute("checked")


class WebCheckBox(WebBaseElement):
    def __init__(self, by, value):
        self.by = by
        self.value = value
        WebBaseElement.__init__(self, by, value)

    def check(self, by, value):
        """
        Check some choice
        """
        self.driver.find_element(by, value).click()

    def is_checked(self, by, value):
        """
        Check is element checked
        """
        return self.driver.findElements(by, value).getAttribute('selected')


class WebLink(WebBaseElement, IClick):
    def __init__(self, by, value):
        self.by = by
        self.value = value
        WebBaseElement.__init__(self, by, value)

    def click(self, by, value, timeout=TimeOutConstants.LINK_LOAD_TIMEOUT):
        """
        Click on element
        """
        self.click(by, value, timeout)

    def is_clickable(self, by, value, timeout=TimeOutConstants.LINK_LOAD_TIMEOUT):
        """
        Check is element clickable
        """
        self.is_clickable(by, value, timeout)

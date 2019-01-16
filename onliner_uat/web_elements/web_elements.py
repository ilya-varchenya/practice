from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from onliner_uat.web_elements.time_class_constants import TimeOutConstants
from onliner_uat.web_elements.web_base_element import WebBaseElement
from onliner_uat.web_elements.IClick import IClick


class WebLabel(WebBaseElement):
    def __init__(self, by, value):
        self.by = by
        self.value = value
        WebBaseElement.__init__(self, by, value)

    def get_text(self):
        """
        Get text from element
        :return: text of element
        """
        return self.driver.find_element(self.by, self.value).text

    def get_text_as_int(self):
        """
        Get text from element as integer
        :return: integer value
        """
        try:
            return self.driver.get_text_as_int(self.by, self.value)
        except ValueError:
            return False


class WebButton(IClick):
    def __init__(self, by, value):
        self.by = by
        self.value = value
        IClick.__init__(self, by, value)


class WebInput(IClick):
    def __init__(self, by, value):
        self.by = by
        self.value = value
        IClick.__init__(self, by, value)

    def clear(self):
        """
        Clear input text fields
        """
        self.driver.find_element(self.by, self.value).clear()

    def set_text(self, input_text):
        """
        Clear input text fields and type text there
        :param input_text:
        """
        self.clear()
        self.driver.find_element(self.by, self.value).send_keys(input_text)


class WebRadioButton(IClick):
    def __init__(self, by, value):
        self.by = by
        self.value = value
        IClick.__init__(self, by, value)

    def is_checked(self):
        """
        Check is element checked
        """
        return self.driver.findElements(self.by, self.value).getAttribute("checked")


class WebCheckBox(IClick):
    def __init__(self, by, value):
        self.by = by
        self.value = value
        IClick.__init__(self, by, value)

    def is_checked(self):
        """
        Check is element checked
        """
        return self.driver.findElements(self.by, self.value).getAttribute('selected')


class WebLink(IClick):
    def __init__(self, by, value):
        self.by = by
        self.value = value
        IClick.__init__(self, by, value)


class WebElementList(IClick):
    def __init__(self, by, value):
        self.by = by
        self.value = value
        IClick.__init__(self, by, value)

    def get_elements(self, timeout=TimeOutConstants.PAGE_LOAD_TIMEOUT):
        """
        Get element from page
        """
        try:
            elements = WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_all_elements_located((self.by, self.value)))
        except NoSuchElementException:
            return False
        return elements

    def get(self, timeout=TimeOutConstants.PAGE_LOAD_TIMEOUT):
        return self.get_elements(timeout)

    def get_text_from_amount_of_elements(self):
        """
        Get text from amount of elements
        """
        return super().get_text_from_amount_of_elements()

    def get_attribute_from_amount_of_elements(self, key):
        """
        Get get attribute from amount of elements
        :param key: attribute name
        """
        return super().get_attribute_from_amount_of_elements(key)

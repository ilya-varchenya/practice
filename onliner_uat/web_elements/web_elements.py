import logging

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
        :return: text of element
        """
        logging.getLogger(__name__).info("Text of element: {}\nby = {}\nvalue = {}".format(
            self.driver.find_element(self.by, self.value).text, self.by, self.value))
        return self.driver.find_element(self.by, self.value).text

    def get_text_as_int(self):
        """
        Get text from element as integer
        :return: integer value
        """
        try:
            logging.getLogger(__name__).info("Text of element as integer: {}\nby = {}\nvalue = {}".format(
                self.driver.get_text_as_int(self.by, self.value), self.by, self.value))
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
        logging.getLogger(__name__).info("Element input field cleared\nby = {}\nvalue = {}".format(self.by, self.value))
        self.driver.find_element(self.by, self.value).clear()

    def set_text(self, input_text):
        """
        Clear input text fields and type text there
        :param input_text:
        """
        self.clear()
        logging.getLogger(__name__).info(
            "This text set to input field: {}\nby = {}\nvalue = {}".format(input_text, self.by, self.value))
        self.driver.find_element(self.by, self.value).send_keys(input_text)


class WebRadioButton(IClick):
    def __init__(self, by, value):
        self.by = by
        self.value = value
        IClick.__init__(self, by, value)

    def is_checked(self):
        logging.getLogger(__name__).info("Radiobutton is checked\nby = {}\nvalue = {}".format(self.by, self.value))
        return self.driver.findElements(self.by, self.value).getAttribute("checked")


class WebCheckBox(IClick):
    def __init__(self, by, value):
        self.by = by
        self.value = value
        IClick.__init__(self, by, value)

    def is_checked(self):
        logging.getLogger(__name__).info("CheckBox is checked\nby = {}\nvalue = {}".format(self.by, self.value))
        return self.driver.findElements(self.by, self.value).getAttribute('selected')


class WebLink(IClick):
    def __init__(self, by, value):
        self.by = by
        self.value = value
        IClick.__init__(self, by, value)


class WebElementList(WebBaseElement):
    def __init__(self, by, value):
        self.by = by
        self.value = value
        WebBaseElement.__init__(self, by, value)

    def get_elements(self, timeout=TimeOutConstants.PAGE_LOAD_TIMEOUT):
        """
        :param timeout: timeout of waiting time
        :return: list of elements
        """
        try:
            elements = WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_all_elements_located((self.by, self.value)))
            logging.getLogger(__name__).info(
                "WebElementList is: {}\nby = {}\nvalue = {}".format(elements, self.by, self.value))
        except NoSuchElementException:
            return False
        return elements

    def get(self, timeout=TimeOutConstants.PAGE_LOAD_TIMEOUT):
        logging.getLogger(__name__).info(
            "Elements are: {}\nby = {}\nvalue = {}".format(self.get_elements(timeout), self.by, self.value))
        return self.get_elements(timeout)

    def get_text_from_amount_of_elements(self):
        """
        :return:list of elements texts
        """
        els = self.driver.find_elements(self.by, self.value)
        logging.getLogger(__name__).info(
            "Text from amount of elements: {}\nby = {}\nvalue = {}".format([i.text for i in els], self.by, self.value))
        return [i.text for i in els]

    def __len__(self):
        return len(self.get())

    def get_attributes_from_amount_of_elements(self, key):
        """
        Get get attributes from amount of elements
        :param key: attribute name
        """
        l_of_attr_val = []
        els = self.driver.find_elements(self.by, self.value)
        for i in range(len(els)):
            el = els[0].find_elements(self.by, self.value)[i].get_attribute(key)
            l_of_attr_val.append(el)
        logging.getLogger(__name__).info(
            "Attributes from amount of elements: {}\nby = {}\nvalue = {}".format(l_of_attr_val, self.by, self.value))
        return l_of_attr_val

import logging

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
        logging.getLogger(__name__).info(
            "Text of element: {}".format(self.driver.find_element(self.by, self.value).text))
        return self.driver.find_element(self.by, self.value).text

    def get_text_as_int(self):
        """
        Get text from element as integer
        :return: integer value
        """
        try:
            logging.getLogger(__name__).info(
                "Text of element as integer: {}".format(self.driver.get_text_as_int(self.by, self.value)))
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
        logging.getLogger(__name__).info("This text set to input field: {}".format(input_text))
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


class WebElementList(WebBaseElement):
    def __init__(self, by, value):
        self.by = by
        self.value = value
        WebBaseElement.__init__(self, by, value)

    def get_text_from_amount_of_elements(self):
        """
        Get text from amount of elements
        """
        logging.getLogger(__name__).info(
            "Text from amount of elements: {}".format(super().get_text_from_amount_of_elements()))
        return super().get_text_from_amount_of_elements()

    def get_attributes_from_amount_of_elements(self, key):
        """
        Get get attributes from amount of elements
        :param key: attribute name
        """
        logging.getLogger(__name__).info(
            "Attributes from amount of elements: {}".format(super().get_attributes_from_amount_of_elements(key)))
        return super().get_attributes_from_amount_of_elements(key)

from onliner_uat.web_elements.web_base_element import WebBaseElement
from onliner_uat.web_elements.IClick import IClick
from onliner_uat.web_elements.time_class_constants import TimeOutConstants
from onliner_uat.web_elements.web_helpers import WebHelpers


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


class WebElementList(WebBaseElement):
    def __init__(self, by, value):
        self.by = by
        self.value = value
        WebBaseElement.__init__(self, by, value)

    def get_text_from_amount_of_elements(self, timeout=TimeOutConstants.BUTTON_TIMEOUT):
        """
        Get text from amount of elements
        """
        WebHelpers.pause(timeout)
        els = self.driver.find_elements(self.by, self.value)
        return [i.text for i in els]

    def get_attribute_from_amount_of_elements(self, key):
        """
        Get get attribute from amount of elements
        :param key: attribute name
        """
        l_of_attr_val = []
        els = self.driver.find_elements(self.by, self.value)
        for i in range(len(els)):
            el = els[0].find_elements(self.by, self.value)[i].get_attribute(key)
            l_of_attr_val.append(el)
        return l_of_attr_val

from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains


class WebHelpers:
    def __get__(self, obj):
        self.driver = obj.driver

    def scroll(self, val):
        """
        Scroll page to element
        """
        try:
            actions = ActionChains(self.driver)
            target = self.driver.find_element(*val)
            actions.move_to_element(target)
            actions.perform()
        except NoSuchElementException:
            return False

    @staticmethod
    def pause(timeout=1):
        """
        Pause break for given seconds
        """
        sleep(timeout)

    def drag_and_drop(self, from_el, to_el):
        """
        Take element, drag it to another
        """
        try:
            source_el = self.driver.find_element(from_el)
            dest_el = self.driver.find_element(to_el)
            ActionChains(self.driver).drag_and_drop(source_el, dest_el).perform()
        except NoSuchElementException:
            return False
        return True

    def double_click(self, val):
        """
        Double click on element
        """
        try:
            el = self.driver.find_element(*val)
            ActionChains(self.driver).double_click(el).perform()
        except NoSuchElementException:
            return False
        return True

    def right_click(self, val):
        """
        Click on element with right mouse button
        """
        try:
            el = self.driver.find_element(*val)
            ActionChains(self.driver).context_click(el).perform()
        except NoSuchElementException:
            return False
        return True

    def long_click(self, val):
        """
        Long click on element
        """
        try:
            el = self.driver.find_element(*val)
            ActionChains(self.driver).click_and_hold(el).perform()
        except NoSuchElementException:
            return False
        return True

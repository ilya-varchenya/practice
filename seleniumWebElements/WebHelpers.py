from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains


class WebHelpers:
    def __init__(self, driver):
        self.driver = driver


    def scroll(self, *val):
        try:
            actions = ActionChains(self.driver)
            target = self.driver.find_element(*val)
            actions.move_to_element(target)
            actions.perform()
        except NoSuchElementException:
            return False


    @staticmethod
    def pause(timeout=1):
        sleep(timeout)


    def drag_and_drop(self, el1, el2):
        try:
            source_el = self.driver.find_element(*el1)
            dest_el = self.driver.find_element(el2)
            ActionChains(self.driver).drag_and_drop(source_el, dest_el).perform()
        except NoSuchElementException:
            return False
        return True


    def double_click(self, val):
        try:
            el = self.driver.find_element(*val)
            ActionChains(self.driver).double_click(el).perform()
        except NoSuchElementException:
            return False
        return True


    def right_click(self, val):
        try:
            el = self.driver.find_element(*val)
            ActionChains(self.driver).context_click(el).perform()
        except NoSuchElementException:
            return False
        return True


    def long_click(self, val):
        try:
            el = self.driver.find_element(*val)
            ActionChains(self.driver).click_and_hold(el).perform()
        except NoSuchElementException:
            return False
        return True

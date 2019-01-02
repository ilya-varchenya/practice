from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from onliner_uat.web_elements.time_class_constants import TimeOutConstants


class WebHelpers:
    def __init__(self, driver):
        self.driver = driver

    def scroll(self, element):
        """
        Scroll page to element
        """
        try:
            actions = ActionChains(self.driver)
            target = self.driver.find_element(element.by, element.value)
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

    def double_click(self, element):
        """
        Double click on element
        """
        try:
            el = self.driver.find_element(element.by, element.value)
            ActionChains(self.driver).double_click(el).perform()
        except NoSuchElementException:
            return False
        return True

    def right_click(self, element):
        """
        Click on element with right mouse button
        """
        try:
            el = self.driver.find_element(element.by, element.value)
            ActionChains(self.driver).context_click(el).perform()
        except NoSuchElementException:
            return False
        return True

    def long_click(self, element):
        """
        Long click on element
        """
        try:
            el = self.driver.find_element(element.by, element.value)
            ActionChains(self.driver).click_and_hold(el).perform()
        except NoSuchElementException:
            return False
        return True

    def move_to_element(self, element, element_appear):
        """
        Move to element
        """
        try:
            el1 = self.driver.find_element(element.by, element.value)
            ActionChains(self.driver).move_to_element(el1).perform()

            # wait for menu item to appear
            WebDriverWait(self.driver, TimeOutConstants.BUTTON_TIMEOUT).\
                until(expected_conditions.presence_of_element_located((element_appear.by, element_appear.value)))
        except NoSuchElementException:
            return False
        return True

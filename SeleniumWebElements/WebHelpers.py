from time import sleep
from selenium.webdriver import ActionChains


class WebHelpers:
    def __init__(self, driver):
        self.driver = driver

    def scroll(self, *val):
        target = self.driver.find_element(*val)
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        actions.perform()

    def pause(self, timeout=1):
        sleep(timeout)

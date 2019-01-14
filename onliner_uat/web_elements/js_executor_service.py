class JSExecutorService:
    def __init__(self, driver):
        self.driver = driver

    def click_by_coordinates(self, x, y):
        """
        JS click on element
        """
        return self.driver.execute_script("document.elementFromPoint({}, {}).click();".format(x, y))

    def get_text_by_coordinates(self, x, y):
        """
        JS get text from element
        """
        return self.driver.execute_script("document.elementFromPoint({}, {}).textContent".format(x, y))

    def scroll_to_element_by_coordinates(self, x, y):
        """
        JS scroll to element element
        """
        return self.driver.execute_script("document.elementFromPoint({}, {}).scrollToElement()".format(x, y))

    def alert(self, text):
        """
        JS alert
        """
        return self.driver.execute_script("alert('{}')".format(text))

    def confirm(self, text):
        """
        JS confirm
        """
        return self.driver.execute_script("confirm('{}')".format(text))

    def prompt(self, text):
        """
        JS prompt
        """
        return self.driver.execute_script("prompt('{}')".format(text))

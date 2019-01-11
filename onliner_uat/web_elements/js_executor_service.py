class JSExecutorService:
    def __init__(self, driver):
        self.driver = driver

    def js_click(self, x, y):
        """
        JS click on element
        """
        return self.driver.execute_script("document.elementFromPoint({}, {}).click();".format(x, y))

    def js_get_text(self, x, y):
        """
        JS get text from element
        """
        return self.driver.execute_script("document.elementFromPoint({}, {}).textContent".format(x, y))

    def js_scroll_to_element(self, x, y):
        """
        JS scroll to element element
        """
        return self.driver.execute_script("document.elementFromPoint({}, {}).scrollToElement()".format(x, y))

    def js_alert(self, text):
        """
        JS alert
        """
        return self.driver.execute_script("alert('{}')".format(text))

    def js_confirm(self, text):
        """
        JS confirm
        """
        return self.driver.execute_script("confirm('{}')".format(text))

    def js_prompt(self, text):
        """
        JS prompt
        """
        return self.driver.execute_script("prompt('{}')".format(text))

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def scroll(self, *val):
        target = self.driver.find_element(*val)
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        actions.perform()


    def click(self, val, timeout=5):
        WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located((val)))
        self.scroll(*val)
        self.driver.find_element(*val).click()


    def is_open(self):
        pass


class StartPage(BasePage):
    people = (By.XPATH, "//*[text()='Люди']")

    right_button = (By.CLASS_NAME, "header-style__underlay")
    autobaraholka_tip = (By.XPATH, "//*[text()='Автобарахолка']")
    auto_tip = (By.LINK_TEXT, "Авто")

    def __init__(self, driver):
        super().__init__(driver)

    def is_open(self):
        if self.driver.find_element(*self.people):
            return True
        else:
            return False

    def go_to_auto_page(self):
        self.click(self.right_button)
        self.click(self.autobaraholka_tip)
        self.click(self.auto_tip)
        return AutoPage(self.driver)


class AutoPage(BasePage):
    car_name = 'Toyota Camry'
    autobaraholka = (By.XPATH, "//*[text()='Автобарахолка']")
    descr = (By.XPATH, "//*[contains(@id, 'car')]/td/p")
    sedan = (By.XPATH, "//li[@class='body_type-1']//input")
    hatchback = (By.XPATH, "//li[@class='body_type-3']//input")
    automatic_transmission = (By.XPATH, "//li[@class='transmission-1']//input")
    front_weel_drive = (By.XPATH, "//li[@class='drivetrain-1']//input")
    mark = (By.XPATH, "//select[@class='manufacture']//option[contains(text(), 'Toyota')]")

    year_sort_mark = (By.XPATH, "//*[@class = 'flr autoba-sorters-year']")
    years_xpath = (By.XPATH, "//span[contains(@class, 'year')]")

    first_car = (By.XPATH, "//td[@class = 'txt']//*[contains(text(), '{}')]".format(car_name))

    car_text = ''

    def __init__(self, driver):
        super().__init__(driver)

    def is_open(self):
        if self.driver.find_element(*self.autobaraholka):
            return True
        else:
            return False

    cars_names = (By.XPATH, "//td[@class = 'txt']//h2")
    cars_descriptions = (By.XPATH, "//td[@class = 'txt']//p")

    def is_filtered(self):
        cars_names_set = set()
        # cars_descriptions_set = set()

        cars_names_set.add(self.driver.find_elements(self.cars_names))
        #
        # need to create check of ONE element in cars_names_set
        #
        # need to create check of car's body types
        #    ||
        #    ||
        #    ||
        # ---  ---
        #  \    /
        #   \  /
        #    \/

        #
        # # find description
        # description = self.driver.find_elements(*self.descr)
        # for i in range(49):
        #     description_string = description[i].text
        #     if description_string.find("седан") == -1 and description_string.find("хетчбэк") == -1:
        #         return False
        #     elif description_string.find("автомат") == -1:
        #         return False
        #     elif description_string.find("передний") == -1:
        #         return False
        #     else:
        #         return True

    def make_filter(self):
        # choice of Toyota
        self.click(self.mark)
        # choice of "седан" and "хэчбэк"
        self.click(self.sedan)
        self.click(self.hatchback)
        # choice automatic transmission
        self.click(self.automatic_transmission)
        # choice of front-wheel drive
        self.click(self.front_weel_drive)

    def is_sorted_by_year(self):
        years = self.driver.find_elements(*self.years_xpath)
        for i in range(48):
            year = years[i].text
            next_year = years[i + 1].text
            return year < next_year

    def sort_by_year(self):
        self.click(self.year_sort_mark)

    def go_to_car_page(self):
        self.click(self.first_car)
        return CarPage(self.driver)

class CarPage(AutoPage):
    car_name = "Toyota Camry"
    car_tittle = (By.XPATH, "//h1[contains(text(), '{}')]".format(car_name))
    car_description = (By.XPATH, "//div[@class ='autoba-msglongcont font-boosting-fix']/p[2]")

    def __init__(self, driver):
        super().__init__(driver)

    def is_open(self):
        return self.driver.find_element(*self.car_tittle)

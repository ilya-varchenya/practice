from pages import *
from selenium import webdriver


class TestForCars:
    def setup(self):
        self.driver = webdriver.Chrome(executable_path="drivers\chromedriver.exe")
        # self.driver.set_window_size(1200, 1000)
        self.driver.get("https://www.onliner.by/")
        self.driver.implicitly_wait(10)
        # self.car_name = "Toyota Camry"

    def teardown(self):
        self.driver.quit()

    def test_pages_jump(self):
        start = StartPage(self.driver)

        # check start page
        assert start.is_open()

        # check title of second page
        auto_page = start.go_to_auto_page()
        assert auto_page.is_open()


    def test_tips(self):
        start = StartPage(self.driver)
        auto_page = start.go_to_auto_page()

        # check filter correct
        auto_page.make_filter()
        assert auto_page.is_filtered()

        # check sort by year
        auto_page.sort_by_year()
        assert auto_page.is_sorted_by_year()

    def test_car(self):
        start = StartPage(self.driver)
        auto_page = start.go_to_auto_page()

        auto_page.make_filter()
        auto_page.sort_by_year()

        car = auto_page.go_to_car_page()
        assert car.is_open()



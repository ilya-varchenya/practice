import pytest

from onliner_uat.tests.base_test import BaseTest
from onliner_uat.pages.start_page import StartPage


class TestStartPage(BaseTest):
    url = "https://www.onliner.by/"

    def setup(self):
        self.driver.set_window_size(1400, 1000)
        self.driver.get(self.url)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.ON1
    def test_ON1(self):
        """
        Guest user should be able to News Section
        """
        start = StartPage(self.driver)

        # check start page
        assert start.is_open()

        # is news link able to guest user
        assert start.is_news_able()

    @pytest.mark.ON2
    def test_ON2(self):
        """
        Tab "Новости" should be checked while user
        navigates to "Люди", "Мнения", "Авто", "Технологии", "Недвижимость" subsections
        """
        start = StartPage(self.driver)

        # check start page
        assert start.is_open()

        # is is subsections visible
        assert start.is_subsections_visible()

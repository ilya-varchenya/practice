import pytest

from onliner_uat.tests.base_test import BaseTest
from onliner_uat.pages.start_page import StartPage
from onliner_uat.models.catalog_bar_items import CatalogBarItems


class TestCatalogPages(BaseTest):
    url = "https://www.onliner.by/"

    def setup(self):
        self.driver.set_window_size(1400, 1000)
        self.driver.get(self.url)
        self.start = StartPage(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.OC1
    def test_cart_is_empty_text_should_be_visible(self):
        catalog_page = self.start.go_to_catalog_page()
        cart_page = catalog_page.go_to_cart_page()

        assert cart_page.is_empty_cart_text_present()

    @pytest.mark.OC2
    def test_catalog_subtitles_should_be_visible(self):
        catalog_page = self.start.go_to_catalog_page()

        assert catalog_page.is_catalog_subtitles_visible(CatalogBarItems)

    @pytest.mark.OC3
    def test_catalog_subtitles_subcategories_should_be_visible(self):
        catalog_page = self.start.go_to_catalog_page()

        assert catalog_page.is_catalog_subcategories_visible()

    @pytest.mark.OC4
    def test_list_of_items_in_subcategories_list_shold_be_changed_when_user_click(self):
        catalog_page = self.start.go_to_catalog_page()

        assert catalog_page.is_catalog_subcategories_list_changed()

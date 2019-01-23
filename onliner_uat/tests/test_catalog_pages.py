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
    def test_list_of_items_in_subcategories_list_should_be_changed_when_user_click(self):
        catalog_page = self.start.go_to_catalog_page()

        assert catalog_page.is_catalog_subcategories_list_changed()

    @pytest.mark.OC5
    def test_user_can_navigate_to_concrete_catalog_item(self):
        catalog_page = self.start.go_to_catalog_page()

        assert catalog_page.is_navigate_to_concrete_catalog_item()

    @pytest.mark.OC6
    def test_user_should_be_able_to_apply_some_filters_on_item_list(self):
        catalog_page = self.start.go_to_catalog_page()
        certain_catalog_group_page = catalog_page.go_to_certain_catalog_group('Мобильные телефоны')

        assert certain_catalog_group_page.is_filter_response()

    @pytest.mark.OC7
    def test_info_in_item_preview_should_be_the_same_with_info_under_title_of_item_page(self):
        catalog_page = self.start.go_to_catalog_page()
        certain_catalog_group_page = catalog_page.go_to_certain_catalog_group('Мобильные телефоны')

        text_of_preview = certain_catalog_group_page.get_text_of_preview()

        certain_catalog_item_page = certain_catalog_group_page.go_to_certain_catalog_group('Мобильные телефоны')

        text_of_description = certain_catalog_item_page.get_text_from_description()
        assert text_of_preview == text_of_description

    @pytest.mark.OC8
<<<<<<< HEAD
    def test_user_should_be_able_to_apply_some_filters_on_item_list(self):
        catalog_page = self.start.go_to_catalog_page()
        certain_catalog_group_page = catalog_page.go_to_certain_catalog_group()

        assert certain_catalog_group_page.is_list_of_items_filtered_cheap_first()
=======
    def test_user_can_check_item_tips_for_add_items_to_comparison_list(self):
        catalog_page = self.start.go_to_catalog_page()
        certain_catalog_group_page = catalog_page.go_to_certain_catalog_group('Мобильные телефоны')

        assert certain_catalog_group_page.is_first_in_column_items_checked()

    @pytest.mark.OC9
    def test_best_choice_option_should_be_highlighted(self):
        catalog_page = self.start.go_to_catalog_page()
        certain_catalog_group_page = catalog_page.go_to_certain_catalog_group('Мобильные телефоны')

        catalog_comparison_page = certain_catalog_group_page.go_to_comparison_page()

        assert catalog_comparison_page.is_the_best_of_first_sections_highlighted()
>>>>>>> 3442affb9e7becab1630c7f4f812818c54cec80c

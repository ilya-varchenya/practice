import pytest

from onliner_uat.tests.base_test import BaseTest
from onliner_uat.pages.start_page import StartPage


class TestPages(BaseTest):
    url = "https://www.onliner.by/"

    def setup(self):
        self.driver.set_window_size(1400, 1000)
        self.driver.get(self.url)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.ON1
    def test_guest_should_be_able_to_news(self):
        start = StartPage(self.driver)

        # check start page
        assert start.is_open()

        # is news link able to guest user
        assert start.is_news_able()

    @pytest.mark.ON2
    def test_subsections_should_be_visible_on_main_page(self):
        start = StartPage(self.driver)

        # is subsections visible
        assert start.are_subsections_have_correct_names()

    @pytest.mark.ON3
    def test_tab_should_be_checked_while_user_navigates_to_subsections(self):
        start = StartPage(self.driver)

        # is subsections underlined with CSS class
        assert start.is_news_underlined()

    @pytest.mark.ON4
    def test_when_user_clicks_subsection_tab_bar_should_be_visible_and_bar_should_be_selected(self):
        start = StartPage(self.driver)
        news_page = start.go_to_people_page()

        # is "Люди" bar selected
        assert news_page.is_bar_selected()

    @pytest.mark.ON5
    def test_shoud_contain_following_info(self):
        start = StartPage(self.driver)

        news_page = start.go_to_people_page()
        # is titles similar
        assert news_page.is_all_components_of_news_block_present()

    @pytest.mark.ON6
    def test_the_most_viewed_news_should_be_highlighted_by_red(self):
        start = StartPage(self.driver)

        # is highlighted by red color
        assert start.is_element_red()

    @pytest.mark.ON7
    def test_title_should_be_equal_with_title_on_preview(self):
        start = StartPage(self.driver)

        # go to News page
        news_page = start.go_to_people_page()
        # get title from preview
        text_of_preview_title = news_page.get_text_of_first_news()

        # go to certain News page
        certain_news_page = news_page.go_to_certain_news_page()
        # get title from certain News page
        text_of_title_on_certain_news_page = certain_news_page.get_text_of_tittle()

        # is titles similar
        assert text_of_title_on_certain_news_page == text_of_preview_title

    @pytest.mark.ON8
    def test_comments_should_be_present_for_each_article(self):
        start = StartPage(self.driver)

        # go to News page
        news_page = start.go_to_people_page()
        # go to certain News page
        certain_news_page = news_page.go_to_certain_news_page()

        # is titles similar
        assert certain_news_page.is_comments_present()

        # does article have 100+ comments
        assert certain_news_page.is_amount_of_comments_more_then_100()

    @pytest.mark.ON9
    def test_user_can_expand_the_list_of_comments(self):
        start = StartPage(self.driver)

        # go to News page
        news_page = start.go_to_people_page()
        certain_news_page = news_page.go_to_certain_news_page()

        # does list of comments expand
        assert certain_news_page.is_expand_the_list_of_comments()

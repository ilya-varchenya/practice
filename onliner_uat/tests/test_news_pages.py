import pytest

from onliner_uat.tests.base_test import BaseTest
from onliner_uat.pages.start_page import StartPage
from onliner_uat.models.bar_items import BarItems


class TestNewsPages(BaseTest):
    url = "https://www.onliner.by/"

    def setup(self):
        self.driver.set_window_size(1400, 1000)
        self.driver.get(self.url)
        self.start = StartPage(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.ON1
    def test_guest_should_be_able_to_news(self):
        assert self.start.is_open()

        # is news link able to guest user
        assert self.start.is_news_able()

    @pytest.mark.ON2
    def test_subsections_should_be_visible_on_main_page(self):
        assert self.start.are_subsections_have_correct_names(BarItems)

    @pytest.mark.ON3
    def test_tab_should_be_checked_while_user_navigates_to_subsections(self):
        assert self.start.is_news_underlined()

    @pytest.mark.ON4
    def test_when_user_clicks_subsection_tab_bar_should_be_visible_and_bar_should_be_selected(self):
        news_page = self.start.go_to_people_page()

        assert news_page.is_bar_selected(BarItems.PEOPLE)

    @pytest.mark.ON5
    def test_should_contain_following_info(self):
        news_page = self.start.go_to_people_page()

        assert news_page.is_news_block_tittle_present()

        assert news_page.is_news_block_text_preview_present()

        assert news_page.is_news_block_image_present()

        assert news_page.is_news_block_number_of_views_present()

        assert news_page.is_news_block_number_of_comments_present()

        assert news_page.is_news_block_publishing_date_present()

    @pytest.mark.ON6
    def test_the_most_viewed_news_should_be_highlighted_by_red(self):
        assert self.start.is_element_red()

    @pytest.mark.ON7
    def test_title_should_be_equal_with_title_on_preview(self):
        news_page = self.start.go_to_people_page()
        # get title from preview
        text_of_preview_title = news_page.get_text_of_first_news()

        certain_news_page = news_page.go_to_certain_news_page()
        # get title from certain News page
        text_of_title_on_certain_news_page = certain_news_page.get_text_of_tittle()

        assert text_of_title_on_certain_news_page == text_of_preview_title

    @pytest.mark.ON8
    def test_comments_should_be_present_for_each_article(self):
        news_page = self.start.go_to_people_page()
        certain_news_page = news_page.go_to_certain_news_page()

        assert certain_news_page.is_comments_present()

        assert certain_news_page.is_amount_of_comments_more_then_100()

    @pytest.mark.ON9
    def test_user_can_expand_the_list_of_comments(self):
        news_page = self.start.go_to_people_page()
        certain_news_page = news_page.go_to_certain_news_page()

        assert certain_news_page.is_expand_the_list_of_comments()

    @pytest.mark.ON10
    def test_guest_should_be_able_to_navigate_to_an_article(self):
        news_page = self.start.go_to_people_page()
        certain_news_page = news_page.go_to_certain_news_page()

        assert certain_news_page.is_open()

    @pytest.mark.ON11
    def test_user_can_navigate_via_clicking_on_arrow_buttons(self):
        news_page = self.start.go_to_people_page()
        certain_news_page = news_page.go_to_certain_news_page()

        assert certain_news_page.is_arrows_navigate_to_the_start_of_page()

        assert certain_news_page.is_arrows_navigate_to_the_end_of_page()

    @pytest.mark.ON12
    def test_social_icons_should_navigate_to_an_onliner_profile(self):
        news_page = self.start.go_to_people_page()
        certain_news_page = news_page.go_to_certain_news_page()

        # try to visit pages

        # YouTube page doesn't load
        # youtube_page = certain_news_page.go_to_youtube_onliner_profile()
        # assert youtube_page.is_open()

        # youtube_page.helpers.back_to_previous()
        instagram_page = certain_news_page.go_to_instagram_onliner_profile()
        assert instagram_page.is_open()

        instagram_page.helpers.go_back(self)
        twitter_page = certain_news_page.go_to_twitter_onliner_profile()
        assert twitter_page.is_open()

        twitter_page.helpers.go_back(self)
        ok_page = certain_news_page.go_to_ok_onliner_profile()
        assert ok_page.is_open()

        ok_page.helpers.go_back(self)
        facebook_page = certain_news_page.go_to_facebook_onliner_profile()
        assert facebook_page.is_open()

        facebook_page.helpers.go_back(self)
        vk_page = certain_news_page.go_to_vk_onliner_profile()
        assert vk_page.is_open()

        vk_page.helpers.go_back(self)
        connect_to_redaction = certain_news_page.go_to_connect_to_redaction_onliner_profile()
        assert connect_to_redaction.is_open()

        # Error 404 on this page
        # # connect_to_redaction.helpers.back_to_previous(self)
        # rss_page = certain_news_page.go_to_rss_onliner_profile()
        # assert rss_page.is_open()

import time

import allure
import pytest
from config import run_id_tasks as run_id
from utils import get_start_and_end_dates
from pages.locators import OfferDependencyLocators as OD
from pages.locators import OfferPageLocators as SC
from pages.locators import TaskPageLocators as TotalLocators
from pages.task_page import TaskPage
from test_data import results_codes as results
from testrail_methods import add_result_for_case

offer_url = '/offer'
offer_dependency_url = '/offer-dependency'
offer_name = 'offer' + str(time.time())
start_date, end_date = get_start_and_end_dates()


class TestOfferDependecy:
    @pytest.fixture
    def create_offer(self, browser):
        page = TaskPage(browser, offer_url)
        page.go_to_site()
        page.get_cookies()
        page.click_on_the_button(TotalLocators.BUTTON)
        page.enter_field(SC.OFFER_NAME, offer_name)
        page.enter_field(SC.OFFER_COMMENT, 'test_comment')
        page.click_on_the_button(SC.OFFER_CONTEXT)
        page.enter_type(SC.OFFER_TYPE, 1)
        page.enter_date(SC.OFFER_START_DATE, start_date)
        page.enter_date(SC.OFFER_FINISH_DATE, end_date)
        page.click_on_the_button(TotalLocators.BUTTON)

        assert page.check_current_title(offer_name)

    def test_create_offer_dependency_with_empty_name(self, create_offer, browser):
        page = TaskPage(browser, offer_dependency_url)
        page.go_to_site()
        page.get_cookies()
        page.click_on_the_button(TotalLocators.BUTTON)
        current_url = browser.current_url
        page.click_on_the_button(TotalLocators.BUTTON)

        assert current_url == browser.current_url

    def test_create_offer_dependency(self, browser):
        page = TaskPage(browser, offer_dependency_url)
        page.go_to_site()
        page.get_cookies()
        page.click_on_the_button(TotalLocators.BUTTON)
        page.enter_type_of_value(OD.OFFER, offer_name)
        page.enter_type_of_value(OD.PRODUCT, 'КЕНО')
        page.click_on_the_button(TotalLocators.BUTTON)

        assert page.check_current_title(offer_name)

    def test_check_values_offer_dependency(self, browser):
        page = TaskPage(browser, offer_dependency_url)
        page.go_to_site()
        page.get_cookies()
        page.check_values_from_table(offer_name)

        assert page.check_field_values_from_table()

    @pytest.mark.skip()
    def test_edit_offer(self, browser):
        page = TaskPage(browser, offer_dependency_url)
        page.go_to_site()
        page.get_cookies()
        page.check_values_from_table(offer_name)

        assert page.check_edit(SC.OFFER_COMMENT, 'Комментарий')

    def test_remove_offer_dependency_step_one(self, browser):
        page = TaskPage(browser, offer_dependency_url)
        page.go_to_site()
        page.get_cookies()
        page.check_values_from_table(offer_name)
        page.remove_type_step_one()

        assert page.get_remove_flag()

    def test_remove_offer_dependency_step_two(self, browser):
        page = TaskPage(browser, offer_dependency_url)
        page.go_to_site()
        page.get_cookies()
        page.check_values_from_table(offer_name)
        page.remove_type_step_two()

        assert page.get_name_from_table() != offer_name

import allure

from config import run_id_tasks as run_id
from pages.locators import OfferPageLocators as SC
from pages.locators import TaskPageLocators as TotalLocators
from pages.task_page import TaskPage
from test_data import results_codes as results
from testrail_methods import add_result_for_case
from utils import get_start_and_end_dates

type_offer_name = 'Test creation new offer'
url = '/offer'
start_date, end_date = get_start_and_end_dates()


@allure.epic('Страница "Предложения"')
class TestOfferPage:
    # 1
    @allure.feature('Создание предложения')
    @allure.title('Проверка валидации')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/735199')
    def test_create_offer_empty_name(self, browser):
        case_id = 735199
        page = TaskPage(browser, url)
        page.go_to_site()
        page.get_cookies()
        page.click_on_the_button(TotalLocators.BUTTON)
        current_url = browser.current_url
        page.click_on_the_button(TotalLocators.BUTTON)

        assert current_url == browser.current_url, add_result_for_case(
            run_id, case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 2
    @allure.feature('Создание предложения')
    @allure.title('Успешное создание')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/735197')
    def test_create_offer(self, browser):
        case_id = 735197
        page = TaskPage(browser, url)
        page.go_to_site()
        page.click_on_the_button(TotalLocators.BUTTON)
        page.enter_field(SC.OFFER_NAME, type_offer_name)
        page.enter_field(SC.OFFER_COMMENT, 'test_comment')
        page.click_on_the_button(SC.OFFER_CONTEXT)
        page.enter_type(SC.OFFER_TYPE, 1)
        page.enter_date(SC.OFFER_START_DATE, start_date)
        page.enter_date(SC.OFFER_FINISH_DATE, end_date)
        page.click_on_the_button(TotalLocators.BUTTON)

        assert page.check_current_title(type_offer_name), add_result_for_case(
            run_id, case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 3
    @allure.feature('Проверка полей предложения')
    @allure.title('Проверка полей')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/735198')
    def test_check_values_offer(self, browser):
        case_id = 735198
        page = TaskPage(browser, url)
        page.go_to_site()
        page.get_cookies()
        page.check_values_from_table(type_offer_name)

        assert page.check_field_values_from_table(), add_result_for_case(run_id,
                                                                         case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 4
    @allure.feature('Редактирование предложения')
    @allure.title('Редактирование полей')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/735200')
    def test_edit_offer(self, browser):
        case_id = 735200
        page = TaskPage(browser, url)
        page.go_to_site()
        page.get_cookies()
        page.check_values_from_table(type_offer_name)

        assert page.check_edit(SC.OFFER_COMMENT, 'Комментарий'), add_result_for_case(
            run_id, case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 5
    @allure.feature('Удаление предложения')
    @allure.title('Шаг 1')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/735201')
    def test_remove_offer_step_one(self, browser):
        case_id = 735201
        page = TaskPage(browser, url)
        page.go_to_site()
        page.get_cookies()
        page.check_values_from_table(type_offer_name)
        page.remove_type_step_one()

        assert page.get_remove_flag(), add_result_for_case(
            run_id, case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 6
    @allure.feature('Удаление предложения')
    @allure.title('Шаг 2')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/735202')
    def test_remove_offer_step_two(self, browser):
        case_id = 735202
        page = TaskPage(browser, url)
        page.go_to_site()
        page.get_cookies()
        page.check_values_from_table(type_offer_name)
        page.remove_type_step_two()

        assert page.get_name_from_table() != type_offer_name, add_result_for_case(
            run_id, case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

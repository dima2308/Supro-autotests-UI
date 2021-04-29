import allure

from config import run_id_tasks as run_id
from pages.locators import ClientSegmentsLocators as SC
from pages.locators import TaskPageLocators as TotalLocators
from pages.task_page import TaskPage
from test_data import results_codes as results
from testrail_methods import add_result_for_case

segment_name = 'Test creation segment'
url = '/client-segment'


class TestClientSegments:
    # 1
    @allure.feature('Создание клиентского сегмента')
    @allure.title('Проверка валидации')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/890423')
    def test_create_client_segment_empty_name(self, browser):
        case_id = 890423
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
    @allure.feature('Создание клиентского сегмента')
    @allure.title('Успешное создание')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/890422')
    def test_create_client_segment(self, browser):
        case_id = 890422
        page = TaskPage(browser, url)
        page.go_to_site()
        page.click_on_the_button(TotalLocators.BUTTON)
        page.enter_field(SC.SEGMENT_NAME, segment_name)
        page.enter_field(SC.SEGMENT_COMMENT, "test_comment")
        page.click_on_the_button(TotalLocators.BUTTON)

        assert page.check_current_title(segment_name), add_result_for_case(
            run_id, case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 3
    @allure.feature('Проверка полей клиентского сегмента')
    @allure.title('Проверка полей')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/890425')
    def test_check_values_client_segment(self, browser):
        case_id = 890425
        page = TaskPage(browser, url)
        page.go_to_site()
        page.get_cookies()
        page.check_values_from_table(segment_name)

        assert page.check_field_values_from_table(), add_result_for_case(run_id,
                                                                         case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 4
    @allure.feature('Редактирование клиентского сегмента')
    @allure.title('Редактирование полей')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/890424')
    def test_edit_client_segment(self, browser):
        case_id = 890424
        page = TaskPage(browser, url)
        page.go_to_site()
        page.get_cookies()
        page.check_values_from_table(segment_name)

        assert page.check_edit(SC.SEGMENT_COMMENT, 'Комментарий'), add_result_for_case(
            run_id, case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 5
    @allure.feature('Удаление клиентского сегмента')
    @allure.title('Шаг 1')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/890426')
    def test_remove_client_segment_step_one(self, browser):
        case_id = 890426
        page = TaskPage(browser, url)
        page.go_to_site()
        page.get_cookies()
        page.check_values_from_table(segment_name)
        page.remove_type_step_one()

        assert page.get_remove_flag(), add_result_for_case(
            run_id, case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 6
    @allure.feature('Удаление клиентского сегмента')
    @allure.title('Шаг 2')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/890427')
    def test_remove_client_segment_step_two(self, browser):
        case_id = 890427
        page = TaskPage(browser, url)
        page.go_to_site()
        page.get_cookies()
        page.check_values_from_table(segment_name)
        page.remove_type_step_two()

        assert page.get_name_from_table() != segment_name, add_result_for_case(
            run_id, case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

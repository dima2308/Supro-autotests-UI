import allure

from pages.task_page import TaskPage
from pages.locators import TypeOfferPageLocators as SC, TaskPageLocators as TotalLocators
from testrail_methods import add_result_for_case
from config import run_id_tasks as run_id
from test_data import results_codes as results

type_offer_name = 'Test creation new type offer'
url = '/offer-type'


@allure.epic('Страница "Виды предложений"')
class TestTypeOfferPage:
    # 1
    @allure.feature('Создание вида предложения')
    @allure.title('Пустое поле "Имя"')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/735192')
    def test_create_type_offer_empty_name(self, browser):
        case_id = 735192
        page = TaskPage(browser, url)
        page.go_to_site()
        page.get_cookies()
        page.click_on_the_button(TotalLocators.BUTTON)
        page.click_on_the_button(TotalLocators.BUTTON)

        assert page.check_name_text_error(SC.NAME_ERROR, 'Необходимо заполнить «Имя».'), add_result_for_case(run_id,
                                                                                                             case_id,
                                                                                                             results[
                                                                                                                 'failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 2
    @allure.feature('Создание вида предложения')
    @allure.title('Успешное создание')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/735191')
    def test_create_type_offer(self, browser):
        case_id = 735191
        page = TaskPage(browser, url)
        page.go_to_site()
        page.click_on_the_button(TotalLocators.BUTTON)
        page.enter_field(SC.OFFER_TYPE_NAME, type_offer_name)
        page.enter_field(SC.OFFER_TYPE_COMMENT, 'test_comment')
        page.click_on_the_button(TotalLocators.BUTTON)

        assert page.check_current_title(type_offer_name), add_result_for_case(run_id, case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 3
    @allure.feature('Проверка полей вида предложения')
    @allure.title('Проверка полей')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/735193')
    def test_check_values_type_offer(self, browser):
        case_id = 735193
        page = TaskPage(browser, url)
        page.go_to_site()
        page.check_values_from_table(type_offer_name)

        assert page.check_field_values_from_table(), add_result_for_case(run_id, case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 4
    @allure.feature('Редактирование вида предложения')
    @allure.title('Редактирование полей')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/735194')
    def test_edit_type_offer(self, browser):
        case_id = 735194
        page = TaskPage(browser, url)
        page.go_to_site()
        page.check_values_from_table(type_offer_name)
        assert page.check_edit(SC.OFFER_TYPE_COMMENT, 'Комментарий'), add_result_for_case(run_id, case_id,
                                                                                          results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 5
    @allure.feature('Удаление вида предложения')
    @allure.title('Шаг 1')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/735195')
    def test_remove_type_step_one(self, browser):
        case_id = 735195
        page = TaskPage(browser, url)
        page.go_to_site()
        page.check_values_from_table(type_offer_name)
        page.remove_type_step_one()

        assert page.get_remove_flag(), add_result_for_case(run_id, case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 6
    @allure.feature('Удаление вида предложения')
    @allure.title('Шаг 2')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/735196')
    def test_remove_type_step_two(self, browser):
        case_id = 735196
        page = TaskPage(browser, url)
        page.go_to_site()
        page.check_values_from_table(type_offer_name)
        page.remove_type_step_two()

        assert page.get_name_from_table() != type_offer_name, add_result_for_case(run_id, case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

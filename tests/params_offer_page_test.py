import allure

from pages.task_page import TaskPage
from pages.locators import TaskPageLocators as TotalLocators, ParamsPageLocators as SC
from testrail_methods import add_result_for_case
from config import run_id_tasks as run_id
from test_data import results_codes as results

param_name = 'New param'
url = '/offer-product-param'
product_url = '/offer-product'


@allure.epic('Страница "Параметры предлагаемых продуктов"')
class TestProductParamPage:
    # 1
    @allure.feature('Добавление параметра к продукту')
    @allure.title('Проверка валидации')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/735770')
    def test_create_product_param_empty_name(self, browser):
        case_id = 735770
        page = TaskPage(browser, product_url)
        page.go_to_site()
        page.get_cookies()
        page.click_on_the_button(TotalLocators.LOOK_BUTTON_FROM_TABLE)
        page.click_on_the_button(TotalLocators.CREATE_PARAM_BUTTON)

        current_url = browser.current_url
        page.click_on_the_button(TotalLocators.BUTTON)

        assert current_url == browser.current_url, add_result_for_case(run_id, case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 2
    @allure.feature('Добавление параметра к продукту')
    @allure.title('Успешное создание')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/735769')
    def test_create_product_param(self, browser):
        case_id = 735769
        page = TaskPage(browser, product_url)
        page.go_to_site()
        page.get_cookies()
        page.click_on_the_button(TotalLocators.LOOK_BUTTON_FROM_TABLE)
        page.click_on_the_button(TotalLocators.CREATE_PARAM_BUTTON)
        page.enter_type(SC.PARAM_TYPE, 1)
        page.enter_field(SC.PARAM_VALUE, 120)
        name = page.get_text(SC.OFFER_NAME, SC.PRODUCT_NAME)
        page.click_on_the_button(TotalLocators.BUTTON)

        assert page.check_current_title(name), add_result_for_case(run_id, case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 3
    @allure.feature('Проверка полей параметра')
    @allure.title('Проверка полей')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/735771')
    def test_check_values_product_param(self, browser):
        case_id = 735771
        page = TaskPage(browser, url)
        page.go_to_site()
        page.get_cookies()

        assert page.check_field_values_from_table(), add_result_for_case(run_id, case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 4
    @allure.feature('Редактирование параметра')
    @allure.title('Редактирование полей')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/735772')
    def test_edit_product_param(self, browser):
        case_id = 735772
        page = TaskPage(browser, url)
        page.go_to_site()
        page.get_cookies()
        assert page.check_edit(SC.PARAM_VALUE, 'Значение'), add_result_for_case(run_id, case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 5
    @allure.feature('Удаление параметра')
    @allure.title('Шаг 1')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/735773')
    def test_remove_product_param_step_one(self, browser):
        case_id = 735773
        page = TaskPage(browser, url)
        page.go_to_site()
        page.get_cookies()
        page.remove_type_step_one()

        assert page.get_remove_flag(), add_result_for_case(run_id, case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 6
    @allure.feature('Удаление параметра')
    @allure.title('Шаг 2')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/735774')
    def test_remove_product_param_step_two(self, browser):
        case_id = 735774
        page = TaskPage(browser, url)
        page.go_to_site()
        page.get_cookies()
        page.remove_type_step_two()

        assert page.get_name_from_table() != param_name, add_result_for_case(run_id, case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

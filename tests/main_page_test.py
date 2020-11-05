import pytest
import allure

from pages.main_page import MainPage
from pages.locators import MainPageLocators
from config import run_id_main as run_id
from test_data import links_locators, links_names, results_codes as results
from testrail_methods import add_result_for_case

tests_results = []


@allure.epic('Главная страница')
@allure.feature('Интерфейс')
class TestMainPage:
    # 1
    @allure.title('Проверка элементов главной страницы')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/735300')
    def test_check_main_panel_info(self, browser):
        case_id = 735300
        main_page = MainPage(browser)
        main_page.go_to_site()
        main_page.get_cookies()

        assert main_page.get_info_boxes_info(), add_result_for_case(
            run_id, case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 2
    @allure.title('Проверка элементов верхней панели')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/735296')
    def test_check_header_elements(self, browser):
        case_id = 735296
        main_page = MainPage(browser)
        main_page.go_to_site()

        assert main_page.get_header_elements(), add_result_for_case(
            run_id, case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 3
    @allure.title('Проверка перехода на главную страницу')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/735295')
    def test_check_go_to_main_page(self, browser):
        case_id = 735295
        main_page = MainPage(browser)
        main_page.go_to_site()
        main_page.click_on_the_button(MainPageLocators.LOGO_LINK)

        assert main_page.check_current_title('Панель управления'), add_result_for_case(run_id, case_id,
                                                                                       results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 4
    @allure.title('Меню пользователя')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/735297')
    def test_check_user_menu(self, browser):
        case_id = 735297
        main_page = MainPage(browser)
        main_page.go_to_site()

        assert main_page.get_user_menu_elements(), add_result_for_case(run_id,
                                                                       case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 5
    @allure.title('Проверка ссылок')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/735299')
    @pytest.mark.parametrize('locator, title', links_locators, ids=links_names)
    def test_check_links(self, browser, locator, title):
        main_page = MainPage(browser)
        main_page.go_to_site()
        main_page.click_on_link(locator)

        assert main_page.check_current_title(
            title), tests_results.append(False)

    # 6
    @allure.title('Выход из системы')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/735298')
    def test_log_out(self, browser):
        case_id = 735298
        main_page = MainPage(browser)
        main_page.go_to_site()
        browser.delete_all_cookies()
        main_page.go_to_profile(MainPageLocators.LOG_OUT_BUTTON)

        assert main_page.check_current_title('СУПРО'), add_result_for_case(
            run_id, case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])


@allure.title('Служебная функция для добавления резлуьтатов тестов')
@pytest.mark.unfunctional
def test_add_results(browser):
    case_id = 735299
    if not tests_results:
        add_result_for_case(run_id, case_id, results['passed'])
    else:
        add_result_for_case(run_id, case_id, results['failed'])

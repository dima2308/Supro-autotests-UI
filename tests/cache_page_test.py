import pytest
import allure

from pages.task_page import TaskPage
from pages.cache_page import CachePage
from pages.locators import CachePageLocators as SC, TaskPageLocators as TC
from testrail_methods import add_result_for_case
from config import run_id_tasks as run_id
from test_data import results_codes as results

url = '/cache'


@allure.epic('Страница "Кэширование"')
class TestCachePage:
    # 1 
    @allure.title('Кэш отсутствует')
    def test_check_empty_cache(self, browser):
        page = CachePage(browser, url)
        page.go_to_site()
        page.get_cookies()
        page.remove_all_cache()

        assert page.is_element_present(TC.TABLE_EMPTY_BODY)
    
    # 2 
    @allure.title('Кэш присутствует')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/756201')
    def test_check_cache(self, browser, get_suggestions):
        case_id = 756201
        page = TaskPage(browser, url)
        page.go_to_site()
        page.get_cookies()

        assert not (page.is_element_present(TC.TABLE_EMPTY_BODY)), add_result_for_case(run_id, case_id,
                                                                                       results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 3 
    @allure.title('Удаление кэша')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/756203')
    def test_remove_cache_suggest(self, browser, get_suggestions):
        case_id = 756203
        page = CachePage(browser, url)
        page.go_to_site()
        page.get_cookies()
        current_key = page.get_value_from_table(SC.CACHE_KEY)
        page.remove_cache()

        assert current_key != page.get_value_from_table(SC.CACHE_KEY), add_result_for_case(run_id, case_id,
                                                                                           results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 4 
    @allure.title('Изменение времени жизни кэша')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/756202')
    def test_edit_cache_suggest(self, browser, get_suggestions):
        case_id = 756202
        page = CachePage(browser, url)
        page.go_to_site()
        page.get_cookies()
        current_ttl = page.get_value_from_table(SC.CASHE_TTL)
        page.edit_cache()

        assert current_ttl == page.get_value_from_table(SC.CASHE_TTL), add_result_for_case(run_id, case_id,
                                                                                           results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 5
    @allure.title('Просмотр кэша')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/756204')
    def test_view_cache_suggest(self, browser, get_suggestions):
        case_id = 756204
        page = CachePage(browser, url)
        page.go_to_site()
        page.get_cookies()
        current_key = page.get_value_from_table(SC.CACHE_KEY)
        page.check_cache()
        box_title_key = page.get_value_from_table(SC.CACHE_BOX_TITLE).split()[2]

        assert box_title_key == current_key, add_result_for_case(run_id, case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 6
    @allure.title('Проверка полей вида предложения')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/756205')
    def test_check_values_cache_suggest(self, browser, get_suggestions):
        case_id = 756205
        page = CachePage(browser, url)
        page.go_to_site()
        page.get_cookies()
        page = TaskPage(browser, url)

        assert page.check_field_values_from_table(), add_result_for_case(run_id, case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

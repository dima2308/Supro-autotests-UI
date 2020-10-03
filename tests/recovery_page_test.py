import pytest
import allure

from pages.recovery_page import RecoveryPage
from pages.locators import RecoveryPageLocators
from testrail_methods import add_result_for_case
from config import run_id_auth as run_id
from test_data import results_codes as results, invalid_emails, test_data_recovery as test_data

tests_results = []
test_cases_id = [724583, 724584, 724585, 724588, 724589, 724590]
test_titles = ['Забыли пароль?', 'Повторная отправка письма']


@pytest.mark.parametrize('url, locator', test_data, ids=test_titles)
@allure.epic('Страница восстановления')
@allure.feature('Проверка валидации')
class TestRecoveryPage:

    # 1 
    @allure.title('Некорректный ввод email')
    def test_enter_invalid_emails(self, browser, url, locator):
        error_text = 'Значение «Email» не является правильным email адресом.'
        page = RecoveryPage(browser, url)
        page.go_to_site()
        email_field = page.get_email(locator)
        for i in invalid_emails:
            email_field.clear()
            page.enter_email(locator, i)
            page.click_on_the_button(RecoveryPageLocators.SUBMIT_BUTTON)
            assert page.check_text_element(RecoveryPageLocators.ERROR, error_text)

        tests_results.append(True)

    # 2
    @allure.title('Пустой email')
    def test_enter_empty_email(self, browser, url, locator):
        page = RecoveryPage(browser, url)
        page.go_to_site()
        current_url = browser.current_url
        page.click_on_the_button(RecoveryPageLocators.SUBMIT_BUTTON)

        assert current_url == browser.current_url, tests_results.append(False)
        tests_results.append(True)

    # 3
    @allure.title('Корректный email')
    # @pytest.mark.skip(reason="В целях тестов")
    @pytest.mark.important
    def test_enter_success_email(self, browser, url, locator):
        page = RecoveryPage(browser, url)
        page.go_to_site()
        page.enter_email(locator, 'd@mail.abasd')
        page.click_on_the_button(RecoveryPageLocators.SUBMIT_BUTTON)

        assert page.get_button(RecoveryPageLocators.SUCCESS_BUTTON), tests_results.append(False)
        tests_results.append(True)


@allure.title('Служебная функция для добавления резлуьтатов тестов')
@pytest.mark.unfunctional
def test_add_results(browser):
    for i in range(len(tests_results)):
        if tests_results[i]:
            add_result_for_case(run_id, test_cases_id[i], results['passed'])
        else:
            add_result_for_case(run_id, test_cases_id[i], results['failed'])

import pytest
import allure
import pickle

from pages.login_page import LoginPage
from pages.locators import LoginPageLocators
from testrail_methods import add_result_for_case
from config import email, password, run_id_auth as run_id
from test_data import results_codes as results
from allure_commons.types import AttachmentType


@allure.epic('Авторизация')
@allure.feature('Негативные тесты')
class TestNegativeLoginPage:
    # 1
    @allure.title('Пустые поля')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/724564')
    def test_enter_empty_fields(self, browser):
        case_id = 724564
        page = LoginPage(browser)
        page.go_to_site()
        page.click_on_the_button(LoginPageLocators.LOGIN_BUTTON)

        assert page.check_text_element(LoginPageLocators.LOGIN_ERROR,
                                       "Необходимо заполнить «Логин»."), add_result_for_case(run_id, case_id,
                                                                                             results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 2
    @allure.title('Пустое поле "Логин"')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/724565')
    def test_enter_empty_login(self, browser):
        case_id = 724565
        page = LoginPage(browser)
        page.go_to_site()
        page.enter_field(LoginPageLocators.PASSWORD_FIELD, 'Test')
        page.click_on_the_button(LoginPageLocators.LOGIN_BUTTON)

        assert page.check_text_element(LoginPageLocators.LOGIN_ERROR,
                                       "Необходимо заполнить «Логин»."), add_result_for_case(run_id, case_id,
                                                                                             results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 3
    @allure.title('Пустое поле "Пароль"')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/724569')
    def test_enter_empty_password(self, browser):
        case_id = 724569
        page = LoginPage(browser)
        page.go_to_site()
        page.enter_field(LoginPageLocators.LOGIN_FIELD, 'Test')
        page.click_on_the_button(LoginPageLocators.LOGIN_BUTTON)

        assert page.check_text_element(LoginPageLocators.PASSWORD_ERROR,
                                       "Необходимо заполнить «Пароль»."), add_result_for_case(run_id, case_id,
                                                                                              results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 4
    @allure.title('Неверно заполненные поля')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/724561')
    def test_enter_invalid_values(self, browser):
        case_id = 724561
        page = LoginPage(browser)
        page.go_to_site()
        page.enter_field(LoginPageLocators.LOGIN_FIELD, 'Test')
        page.enter_field(LoginPageLocators.PASSWORD_FIELD, 'Test')
        page.click_on_the_button(LoginPageLocators.LOGIN_BUTTON)

        assert page.check_text_element(LoginPageLocators.PASSWORD_ERROR,
                                       "Неправильный логин или пароль"), add_result_for_case(run_id, case_id,
                                                                                             results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])


@allure.epic('Авторизация')
@allure.feature('Позитивные тесты')
class TestPositiveLoginPage:
    # 5
    @allure.title('Проверка чекбокса "Запомнить меня"')
    def test_check_remember_button(self, browser):
        page = LoginPage(browser)
        page.go_to_site()
        page.click_on_the_checkbox()

        if page.get_the_checkbox().is_selected():
            print('\nЧекбокс активен')

        page.click_on_the_checkbox()

        if not (page.get_the_checkbox().is_selected()):
            print('Чекбокс неактивен')

        assert not (page.get_the_checkbox().is_selected())

    # 6
    @allure.title('Проверка ссылки "Забыли пароль?"')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/724582')
    def test_check_forget_button(self, browser):
        case_id = 724582
        page = LoginPage(browser)
        page.go_to_site()
        page.click_on_the_button(LoginPageLocators.FORGET_PASSWORD_BUTTON)

        assert browser.current_url == 'http://tfi-supro-back.tfi.supro.orglot.office/user/forgot', add_result_for_case(
            run_id, case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 7
    @allure.title('Проверка кнопки "Не пришло письмо?"')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/724587')
    def test_check_not_letter_button(self, browser):
        case_id = 724587
        page = LoginPage(browser)
        page.go_to_site()
        page.click_on_the_button(LoginPageLocators.NOT_RECEIVED_LETTER_BUTTON)

        assert browser.current_url == 'http://tfi-supro-back.tfi.supro.orglot.office/user/resend', add_result_for_case(
            run_id, case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

    # 8
    @allure.title('Успешная авторизация')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/724570')
    @pytest.mark.important
    def test_log_in(self, browser):
        case_id = 724570
        page = LoginPage(browser)
        page.go_to_site()
        page.enter_field(LoginPageLocators.LOGIN_FIELD, email)
        page.enter_field(LoginPageLocators.PASSWORD_FIELD, password)
        page.click_on_the_checkbox()
        page.click_on_the_button(LoginPageLocators.LOGIN_BUTTON)

        assert page.check_current_title('Панель управления'), add_result_for_case(
            run_id, case_id, results['failed'])
        add_result_for_case(run_id, case_id, results['passed'])

        with allure.step('Cкриншот'):
            allure.attach(browser.get_screenshot_as_png(),
                          name='Screen', attachment_type=AttachmentType.PNG)
        pickle.dump(browser.get_cookies(), open("cookies.pkl", "wb"))

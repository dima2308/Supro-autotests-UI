from config import main_url
from pages.base_page import BasePage
from pages.locators import TaskPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time
import random

fields_values = {}


class TaskPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver)
        self.base_url = main_url + url

    def enter_field(self, locator, value):
        field = self.find_element(locator)
        field.send_keys(value)
        return field

    def check_name_text_error(self, locator, text):
        return self.check_text_element(locator, text)

    def get_name_from_table(self):
        return self.find_element(TaskPageLocators.NAME_FROM_TABLE).text

    def get_remove_flag(self):
        return self.check_text_element(TaskPageLocators.REMOVE_FLAG, 'Да')

    def check_values_from_table(self, title):
        assert self.get_name_from_table() == title

    def get_fields_values_from_table(self):
        st = self.find_elements(TaskPageLocators.TABLE_TR)
        thead = self.find_elements(TaskPageLocators.THEAD)
        for i in range(len(st) - 2):
            fields_values[thead[i + 1].text] = st[i + 1].text
        return fields_values

    def check_field_values_from_table(self):
        fields_values = self.get_fields_values_from_table()
        for i in fields_values:
            assert fields_values[i]
        return True

    def edit_field(self, locator):
        fields_values = self.get_fields_values_from_table()
        self.find_element(TaskPageLocators.EDIT_BUTTON_FROM_TABLE).click()
        self.find_element(locator).clear()
        self.enter_field(locator, 'New comment-{}'.format(random.randint(0, 100)))
        self.click_on_the_button(TaskPageLocators.BUTTON)

        return fields_values

    def check_edit(self, locator, row):
        info = self.edit_field(locator)

        old_value = info[row]
        old_edited_date = info['Исправлено']
        time.sleep(1)
        self.go_to_site()
        edited_info = self.get_fields_values_from_table()

        assert (edited_info[row] != old_value)
        assert (edited_info['Исправлено'] != old_edited_date)

        return True

    def remove_type_step_one(self):
        self.find_element(TaskPageLocators.REMOVE_BUTTON_FROM_TABLE).click()
        return self.driver.switch_to.alert.accept()

    def remove_type_step_two(self):
        flag = self.find_element(TaskPageLocators.REMOVE_FLAG).text
        if flag == 'Да':
            self.remove_type_step_one()
        else:
            raise AssertionError

    def enter_date(self, locator, value):
        offer_start_date = self.find_element(locator)
        offer_start_date.send_keys(value)
        for i in range(3):
            offer_start_date.send_keys(Keys.RETURN)

    def enter_type(self, locator, value):
        offer_type = Select(self.find_element(locator))
        offer_type.select_by_index(value)
        return offer_type

    def get_text(self, locator_offer, locator_product):
        text_offer = self.find_element(locator_offer).text
        text_product = self.find_element(locator_product).text
        return text_offer.split(': ')[1] + '.' + text_product.split(': ')[1]

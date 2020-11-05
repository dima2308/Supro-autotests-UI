from pages.base_page import BasePage
from pages.locators import TaskPageLocators, CachePageLocators
from selenium.common.exceptions import TimeoutException
from config import main_url


class CachePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver)
        self.base_url = main_url + url

    def get_value_from_table(self, locator):
        return self.find_element(locator).text

    def remove_cache(self):
        self.find_element(TaskPageLocators.REMOVE_BUTTON_FROM_TABLE).click()
        return self.driver.switch_to.alert.accept()

    def edit_cache(self):
        return self.find_element(TaskPageLocators.EDIT_BUTTON_FROM_TABLE).click()

    def check_cache(self):
        return self.find_element(TaskPageLocators.LOOK_BUTTON_FROM_TABLE).click()

    def remove_all_cache(self):
        try:
            cache_strings = self.find_elements(CachePageLocators.CACHE_STRINGS)
            for cache in cache_strings:
                self.remove_cache()
        except TimeoutException:
            pass

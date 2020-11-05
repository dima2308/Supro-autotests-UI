from pages.base_page import BasePage


class RecoveryPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver)
        self.base_url = url

    def enter_email(self, locator, value):
        email = self.find_element(locator)
        email.send_keys(value)
        return email

    def get_email(self, locator):
        email = self.find_element(locator)
        return email

    def get_text_error(self, locator):
        return self.find_element(locator).text

    def get_button(self, locator):
        return self.find_element(locator)

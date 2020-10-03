from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def enter_field(self, locator, value):
        field = self.find_element(locator)
        field.send_keys(value)
        return field

    def get_text(self, locator):
        return self.find_element(locator).text

    def get_the_checkbox(self):
        return self.find_element(LoginPageLocators.CHECKBOX_REMEMBER)
    
    def click_on_the_checkbox(self):
        return self.get_the_checkbox().click()
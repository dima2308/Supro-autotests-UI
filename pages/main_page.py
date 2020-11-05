from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def go_to_profile(self, locator):
        self.find_element(MainPageLocators.DROPDOWN_TOGGLE).click()
        return self.find_element(locator).click()

    def get_user_info(self, locator):
        return self.find_element(locator).text

    def click_on_link(self, locator):
        return self.find_element(locator).click()

    def get_info_boxes_info(self):
        elems = self.find_elements(MainPageLocators.INFO_BOXES)
        elems_text = []
        for i in elems:
            elems_text.append(i.text)
        return elems_text

    def get_table(self):
        return self.find_element(MainPageLocators.PRODUCTS_TABLE)

    def get_quick_buttons(self):
        self.find_element(MainPageLocators.NEW_SUGGEST_BUTTON)
        self.find_element(MainPageLocators.NEW_PRODUCT_BUTTON)
        self.find_element(MainPageLocators.NEW_BANNER_BUTTON)
        return True

    def get_header_elements(self):
        self.find_element(MainPageLocators.LOGO_LINK)
        self.find_element(MainPageLocators.SIDEBAR_TOGGLE)
        self.find_elements(MainPageLocators.DROPDOWN_TOGGLE)
        return True

    def get_user_menu_elements(self):
        self.find_element(MainPageLocators.DROPDOWN_TOGGLE).click()
        self.find_element(MainPageLocators.PROFILE_BUTTON)
        self.find_element(MainPageLocators.LOG_OUT_BUTTON)
        return True

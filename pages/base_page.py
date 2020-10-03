import os.path
import pickle
from config import main_url
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = main_url

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def check_current_title(self, title, time=5):
        return WebDriverWait(self.driver, time).until(EC.title_contains(title),
                                                      message="Current title " + self.driver.title + f" not equal {title}")

    def check_text_element(self, locator, text, time=5):
        return WebDriverWait(self.driver, time).until(EC.text_to_be_present_in_element(locator, text),
                                                      message=f"Can't find text {text} by locator {locator}")
    
    def get_cookies(self):
        if os.path.isfile("cookies.pkl"):
            with open("cookies.pkl", "rb") as file:
                cookies = pickle.load(file)
        else:
            raise Exception('Cookies not found')
        
        for cookie in cookies:
            if 'expiry' in cookie:
                cookie['expiry'] = int(cookie['expiry'])
            self.driver.add_cookie(cookie)

        self.go_to_site()

    def is_element_present(self, locator):
        try:
            self.find_element(locator)
        except TimeoutException:
            return False
        return True

    def click_on_the_button(self, locator):
        return self.find_element(locator).click()       

import pytest
import requests
from selenium import webdriver
from config import api_url


@pytest.fixture(scope="module")
def browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def get_suggestions():
    s = requests.session()
    req_data = {
        'terminal_id': 1,
        'user_id': 1,
        'basket': [4420, 7103]
    }

    return s.post(api_url + '/get-dependent-offers', json=req_data)

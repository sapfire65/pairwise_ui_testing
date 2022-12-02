import time
from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class TestMyPage:
    def test_open_site(self, browser):
        URL = 'https://rus.auto24.lv/'
        page = BasePage(browser, URL)
        page.open()







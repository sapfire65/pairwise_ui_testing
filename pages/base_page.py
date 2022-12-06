import math
import time
import logging

import pytest
from selenium import webdriver
from locators import Locators
from selenium.webdriver import Remote as RemoteWebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Родительский класс
class BasePage:
    # Создаем конструкцию взаимодействия передачи ссылки в браузер
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url


    # Создаем метод открытия и перехода по ссылке page.open()
    def open(self):
        self.browser.get(self.url)

    def click(self, locator):
        try:
           WebDriverWait(self, 5).until(EC.element_to_be_clickable((By.XPATH, locator))).click()

        except TimeoutException:
            return False
        return True


    def status_search(self, locator_found):
        try:
            WebDriverWait(self, 5).until(EC.visibility_of_element_located((By.XPATH, locator_found)))

        except TimeoutException:
            return False
        return True






    def element_located(self, what):
        try:
            WebDriverWait(self, 10).until(EC.presence_of_element_located((By.XPATH, what)))

        except TimeoutException:
            return False
        return True

    '''Метод скролинга до элемента'''

    @staticmethod
    def scroll_in_too(browser, what):
        try:
            # Скролим до элемента
            position = browser.find_element(By.XPATH, what)
            browser.execute_script("return arguments[0].scrollIntoView();", position)
            time.sleep(0.9)
        except NoSuchElementException:
            print(f'Элемент не найден')
            return False
        except TimeoutException:
            print(f'Элемент не виден')
            return False
        return True




    # Если элемент найден, возвращаем True,
    # иначе - перехватываем ошибку 'NoSuchElementException'
    # и присваиваем False
    # def is_element_present(self, how, what):
    #     try:
    #         self.browser.find_element(how, what)
    #     except NoSuchElementException:
    #         return False
    #     return True
    #
    #
    # # Кликаем по ссылке логин / регистрация
    # def go_to_login_page(self):
    #     link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
    #     link.click()





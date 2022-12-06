import time
import pytest
import colorama
from colorama import Fore, Style
from base_page import BasePage
from parsing import ListParsingTabs
from locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture
def open_site(browser):
    BasePage(browser, 'https://rus.auto24.lv/').open()
    BasePage.click(browser, Locators.AGREE_TO_ACCEPT_COOKIES)


pairwise_list = ListParsingTabs.dic_list()
@pytest.mark.parametrize("pairwise_", pairwise_list)
def test_1(browser, open_site, pairwise_):
    print(Fore.LIGHTWHITE_EX, f'Тип автомобиля:', Style.RESET_ALL, Fore.LIGHTGREEN_EX, pairwise_[0], Style.RESET_ALL, end='\n')
    '''Выбор типа автомобиля'''

    assert BasePage.scroll_in_too(browser,
                                  '(//div[@class="custom-select"])[1]'), 'Скрол до элемента: {pairwise_[0], не работает'
    assert BasePage.click(browser, '(//div[@class="custom-select"])[1]'), 'не выбрал Тип автомобиля'
    assert BasePage.scroll_in_too(browser,
                                  f"//span[text()='{pairwise_[0]}']"), 'Скрол до элемента: {pairwise_[0], не работает'
    assert BasePage.click(browser, f"//span[text()='{pairwise_[0]}']"), f'не кликнул в списке по {pairwise_[0]}'


    print(Fore.LIGHTWHITE_EX, f'Выбор типа кузова автомобиля:', Style.RESET_ALL, Fore.LIGHTGREEN_EX, pairwise_[1],
          Style.RESET_ALL, end='\n')
    '''Выбор типа кузова автомобиля'''
    assert BasePage.scroll_in_too(browser, '(//div[@class="custom-select"])[2]'), 'Скрол до элемента: {pairwise_[1], не работает'
    assert BasePage.click(browser, '(//div[@class="custom-select"])[2]'), 'не выбрал Тип кузова'

    assert BasePage.scroll_in_too(browser, f"//div[text()='{pairwise_[0]}']/following::div/span[text()='{pairwise_[1]}']"), 'Скрол до элемента: {pairwise_[1], не работает'
    assert BasePage.click(browser, f"//div[text()='{pairwise_[0]}']/following::div/span[text()='{pairwise_[1]}']"), f'не кликнул в списке по {pairwise_[1]}'


    print(Fore.LIGHTWHITE_EX, f'Тип топлива автомобиля:', Style.RESET_ALL, Fore.LIGHTGREEN_EX, pairwise_[3],
          Style.RESET_ALL, end='\n')
    '''Выбор типа топлива автомобиля:'''
    assert BasePage.click(browser, '(//div[@class="custom-select"])[5]'), 'типа топлива автомобиля, не выбран'
    assert BasePage.scroll_in_too(browser,
                                  '(//div[@class="custom-select"])[5]'), 'Скрол до элемента: {pairwise_[3], не работает'
    assert BasePage.click(browser, f"//span[text()='{pairwise_[3]}']"), f'не кликнул в списке по {pairwise_[3]}'


    print(Fore.LIGHTWHITE_EX, f'Тип КПП автомобиля:', Style.RESET_ALL, Fore.LIGHTGREEN_EX, pairwise_[4],
          Style.RESET_ALL, end='\n')
    '''Выбор типа КПП автомобиля:'''
    assert BasePage.click(browser, '(//div[@class="custom-select"])[6]'), 'типа КПП автомобиля, не выбран'
    assert BasePage.scroll_in_too(browser,
                                  '(//div[@class="custom-select"])[6]'), 'Скрол до элемента: {pairwise_[3], не работает'
    assert BasePage.click(browser, f"//span[text()='{pairwise_[4]}']"), f'не кликнул в списке по {pairwise_[4]}'


    print(Fore.LIGHTWHITE_EX, f'Цвет автомобиля:', Style.RESET_ALL, Fore.LIGHTGREEN_EX, pairwise_[5],
          Style.RESET_ALL, end='\n')
    '''Цвет автомобиля:'''
    assert BasePage.click(browser, '(//div[@class="custom-select"])[7]'), 'Цвет автомобиля не выбран'
    assert BasePage.scroll_in_too(browser,
                                  '(//div[@class="custom-select"])[7]'), 'Скрол до элемента: {pairwise_[3], не работает'
    assert BasePage.click(browser, f"//span[text()='{pairwise_[5]}']"), f'не кликнул в списке по {pairwise_[5]}'


    print(Fore.LIGHTWHITE_EX, f'Поиск по всем локациям', Style.RESET_ALL, Fore.LIGHTGREEN_EX,
          Style.RESET_ALL, end='\n')
    '''Выбор всех локаций'''
    assert BasePage.click(browser, Locators.FILTER_DELL), 'Филтр локаций не очищен'



    assert BasePage.click(browser, Locators.BUTTON_START_SEARCH), 'Кнопка не нажата'
    assert BasePage.status_search(browser, Locators.FOUND_AUTO), f'Нет машин на эти варианты: {pairwise_[0]} {pairwise_[1]}'














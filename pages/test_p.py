import time
import pytest
import colorama
from colorama import Fore, Style
from base_page import BasePage
from parsing import ListParsingTabs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture
def open_site(browser):
    BasePage(browser, 'https://rus.auto24.lv/').open()
    BasePage.click(browser, '//button[@id="onetrust-accept-btn-handler"]')

pairwise_list = ListParsingTabs.dic_list()
@pytest.mark.parametrize("pairwise", pairwise_list)
def test_1(browser, open_site, pairwise):
    print(Fore.LIGHTWHITE_EX, f'Тип автомобиля:', Style.RESET_ALL, Fore.LIGHTGREEN_EX, pairwise[0], Style.RESET_ALL, end='\n')
    '''Выбор типа автомобиля'''

    assert BasePage.click(browser, '(//div[@class="custom-select"])[1]'), 'не выбрал Тип автомобиля'
    assert BasePage.scroll_in_too(browser, '(//div[@class="custom-select"])[1]'), 'Скрол до элемента: {pairwise[0], не работает'
    assert BasePage.click(browser, f"//span[text()='{pairwise[0]}']"), f'не кликнул в списке по {pairwise[0]}'


    print(Fore.LIGHTWHITE_EX, f'Выбор типа кузова автомобиля:', Style.RESET_ALL, Fore.LIGHTGREEN_EX, pairwise[1],
          Style.RESET_ALL, end='\n')
    '''Выбор типа кузова автомобиля'''
    assert BasePage.click(browser, '(//div[@class="custom-select"])[2]'), 'не выбрал Тип кузова'
    assert BasePage.scroll_in_too(browser, '(//div[@class="custom-select"])[2]'), 'Скрол до элемента: {pairwise[1], не работает'
    assert BasePage.click(browser, f"//span[text()='{pairwise[1]}']"), f'не кликнул в списке по {pairwise[1]}'


    print(Fore.LIGHTWHITE_EX, f'Выбор марки автомобиля:', Style.RESET_ALL, Fore.LIGHTGREEN_EX, pairwise[2],
          Style.RESET_ALL, end='\n')
    '''Выбор марки автомобиля'''
    assert BasePage.click(browser, '(//div[@class="custom-select"])[3]'), 'не выбрана марка авто'
    assert BasePage.scroll_in_too(browser, '(//div[@class="custom-select"])[3]'), 'Скрол до элемента: {pairwise[2], не работает'
    assert BasePage.click(browser, f"//span[text()='{pairwise[2]}']"), f'не кликнул в списке по {pairwise[2]}'


    print(Fore.LIGHTWHITE_EX, f'Тип топлива автомобиля:', Style.RESET_ALL, Fore.LIGHTGREEN_EX, pairwise[3],
          Style.RESET_ALL, end='\n')
    '''Выбор типа топлива автомобиля:'''
    assert BasePage.click(browser, '(//div[@class="custom-select"])[5]'), 'типа топлива автомобиля, не выбран'
    assert BasePage.scroll_in_too(browser,
                                  '(//div[@class="custom-select"])[5]'), 'Скрол до элемента: {pairwise[3], не работает'
    assert BasePage.click(browser, f"//span[text()='{pairwise[3]}']"), f'не кликнул в списке по {pairwise[3]}'


    print(Fore.LIGHTWHITE_EX, f'Тип КПП автомобиля:', Style.RESET_ALL, Fore.LIGHTGREEN_EX, pairwise[4],
          Style.RESET_ALL, end='\n')
    '''Выбор типа КПП автомобиля:'''
    assert BasePage.click(browser, '(//div[@class="custom-select"])[6]'), 'типа КПП автомобиля, не выбран'
    assert BasePage.scroll_in_too(browser,
                                  '(//div[@class="custom-select"])[6]'), 'Скрол до элемента: {pairwise[3], не работает'
    assert BasePage.click(browser, f"//span[text()='{pairwise[4]}']"), f'не кликнул в списке по {pairwise[4]}'


    print(Fore.LIGHTWHITE_EX, f'Цвет автомобиля:', Style.RESET_ALL, Fore.LIGHTGREEN_EX, pairwise[5],
          Style.RESET_ALL, end='\n')
    '''Цвет автомобиля:'''
    assert BasePage.click(browser, '(//div[@class="custom-select"])[7]'), 'Цвет автомобиля не выбран'
    assert BasePage.scroll_in_too(browser,
                                  '(//div[@class="custom-select"])[7]'), 'Скрол до элемента: {pairwise[3], не работает'
    assert BasePage.click(browser, f"//span[text()='{pairwise[5]}']"), f'не кликнул в списке по {pairwise[5]}'

    time.sleep(5)











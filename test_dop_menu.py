import time

import pytest
import selenium
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

from pages.avtorization_page import Avtorization_page
from pages.dop_menu import Dop_menu_page
from pages.information_pages import Information_page

from pages.service_pages import Service_link


allure.description("test_dop_menu")
def test_dop_menu():
    driver_service = Service(executable_path='C:\\Users\\Nikita\\PycharmProjects\\resource\\chromedriver.exe')
    # driver = webdriver.Chrome(executable_path='C:\\Users\\Nikita\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(service=driver_service)
    print("Start 1 ")

    d_m = Dop_menu_page(driver)
    d_m.dop_menu_inform()

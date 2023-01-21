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

from pages.service_pages import Service_link


allure.description("test_menu_service_help")
def test_menu_service():
    driver_service = Service(executable_path='C:\\Users\\Nikita\\PycharmProjects\\resource\\chromedriver.exe')
    # driver = webdriver.Chrome(executable_path='C:\\Users\\Nikita\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(service=driver_service)
    print("Start 1 ")
    a_p = Avtorization_page(driver)
    a_p.avtorization()
    s_m = Service_link(driver)
    s_m.menu_service_help()
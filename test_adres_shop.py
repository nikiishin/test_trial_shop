import time

import pytest
import selenium
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

from pages.adres_shop import Adres_shop
from pages.avtorization_page import Avtorization_page
from pages.discount_cart import Discount_cart


allure.description("test_discount_cart")
def test_discount_cart():
    driver_service = Service(executable_path='C:\\Users\\Nikita\\PycharmProjects\\resource\\chromedriver.exe')
    # driver = webdriver.Chrome(executable_path='C:\\Users\\Nikita\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(service=driver_service)
    print("Start 1 ")
    a_p = Avtorization_page(driver)
    a_p.avtorization()
    a_s = Adres_shop(driver)
    a_s.slection_shop()

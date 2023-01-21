import time

import pytest
import selenium
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

from pages.add_to_cart import Add_to_cart
from pages.avtorization_page import Avtorization_page
from pages.cdek_link import Cdek_link
from pages.delivery_pages import Delivery_pages
from pages.finish_order import Finish_order
from pages.finishh_add import Finish_add
from pages.login_page import Login_page
from pages.pley_market_link import Play_marcet_link
from pages.select_city import Select_city
from pages.select_product import Select_product
from pages.select_ski import Select_ski
from pages.sorted_page import Sorted_page
from pages.sorted_price_page import Sorted_price_page

allure.description("test_cdek_link")
def test_cdek_link():
    driver_service = Service(executable_path='C:\\Users\\Nikita\\PycharmProjects\\resource\\chromedriver.exe')
    # driver = webdriver.Chrome(executable_path='C:\\Users\\Nikita\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(service=driver_service)
    print("Start 1 ")
    a_p = Avtorization_page(driver)
    a_p.avtorization()
    p_m = Play_marcet_link(driver)
    p_m.play_marc_link()
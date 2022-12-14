import time

import pytest
import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

from pages.add_to_cart import Add_to_cart
from pages.delivery_pages import Delivery_pages
from pages.finish_order import Finish_order
from pages.finishh_add import Finish_add
from pages.login_page import Login_page
from pages.select_city import Select_city
from pages.select_product import Select_product
from pages.select_ski import Select_ski
from pages.sorted_page import Sorted_page
from pages.sorted_price_page import Sorted_price_page


def test_buy_product_1():
    driver_service = Service(executable_path='C:\\Users\\Nikita\\PycharmProjects\\resource\\chromedriver.exe')
    # driver = webdriver.Chrome(executable_path='C:\\Users\\Nikita\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(service=driver_service)
    print("Start 1 ")

    s_k = Select_ski(driver)
    s_k.selections()
    s_p = Sorted_page(driver)
    s_p.click_sorted_brand()
    sort_price = Sorted_price_page(driver)
    sort_price.click_sorted_button()
    select_prod = Select_product(driver)
    select_prod.click_select_prof_ros()
    a_to_c = Add_to_cart(driver)
    a_to_c.click_add_cart()
    login = Login_page(driver)
    login.authorization()
    f_c = Finish_add(driver)
    f_c.click_finish_go_cart()
    sel_c = Select_city(driver)
    sel_c.selctions_city()
    f_b = Finish_order(driver)
    f_b.click_finish_order()
    dil_p = Delivery_pages(driver)
    dil_p.inform_user()



    print("Finish")
    driver.quit()

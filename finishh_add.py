import time

import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Finish_add(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    finish_go_cart = "/html/body/div[4]/div[9]/div[5]/div[2]/div[3]/div[2]/div[2]/div[2]/a[2]" # переходим в карзину уже авторизовавшись

    # sorted_price_hi = "//*[@id='select1-group']/ul/li[3]/a"

    # login_button = "//input[@id='login-button']"
    # main_word = "//*[@id='header_container']/div[2]/span"

    # getters

    def get_finish_go_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_go_cart)))

    # def get_sorted_price_hi(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sorted_price_hi)))

    # #Action

    def click_finish_go_cart(self):
        with allure.step("click_finish_go_cart"):
            self.get_finish_go_cart().click()
            time.sleep(3)
            # self.get_sorted_price_hi().click()
            # time.sleep(5)

            # time.sleep(10)
            print("sorted_price")
    #
    #
    #
    #
    # def filter(self):
    #
    #     self.input_price_filter("50000")
    #     time.sleep(10)

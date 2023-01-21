import time

import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Add_to_cart(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    add_cart = "/html/body/div[4]/div[3]/div[6]/div[1]/div[2]/div[3]/div[1]/a[1]/span"  #добавляем в корзину
    size_to_cart = "//*[@id='ui-undefined']/span[2]"
    select_size = "//*[@id='select1-group']/ul/li[2]/a"     # выбираем размер в корзине
    click_to_cart = "/html/body/div[4]/div[6]/div[11]/div[2]/div[2]/form/div/div/div/input"




    # getters

    def get_add_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_cart)))

    def get_size_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.size_to_cart)))

    def get_select_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_size)))

    def get_click_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.click_to_cart)))


    # #Action

    def click_add_cart(self):
        with allure.step("click_add_cart"):
            self.get_add_cart().click()
            time.sleep(3)
            self.get_size_to_cart().click()
            time.sleep(5)
            self.get_select_size().click()
            self.get_click_to_cart().click()
            time.sleep(3)






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




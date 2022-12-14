import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Finish_order(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    order_button_fin = "//*[@id='frm']/div/div[3]/table/tbody/tr[3]/td[5]/div/div/input"


    # getters

    def get_order_button_fin(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_button_fin)))

    # def get_size_to_cart(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.size_to_cart)))
    #
    # def get_select_size(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_size)))
    #
    # def get_click_to_cart(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.click_to_cart)))

    # #Action

    def click_finish_order(self):
        self.get_order_button_fin().click()
        time.sleep(3)


        # time.sleep(10)
        print("Click order button")

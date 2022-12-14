import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Sorted_price_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    sorted_button = "//*[@id='ui-sort_select']/span[2]"     # кнопка сортировки по стоимости
    sorted_price_hi = "//*[@id='select1-group']/ul/li[3]/a"     # от дорогого к дешевому



    def get_sorted_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sorted_button)))

    def get_sorted_price_hi(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sorted_price_hi)))


    # #Action

    def click_sorted_button(self):
        self.get_sorted_button().click()

        self.get_sorted_price_hi().click()
        time.sleep(5)
        print("sorted_price")




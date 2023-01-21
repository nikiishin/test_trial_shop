import time

import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Sorted_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    sorted_brand = "//*[@id='filter_form']/div[1]/div[3]/div[5]"    # сортируем по бренду
    select_rosing = "//*[@id='filter_form']/div[1]/div[3]/div[5]/div[4]/label"      # выбираем Rossignol
    sorted_size = "//*[@id='filter_form']/div[1]/div[3]/div[4]"     #сортируем по размеру
    sorted_size_190 = "//*[@id='filter_form']/div[1]/div[3]/div[4]/div[15]/label"       #выбираем 180
    pokaz = "//*[@id='filter_form']/div[1]/div[3]/div[14]/div/input" # применяем фильтры


    # getters

    def get_sorted_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sorted_brand)))

    def get_select_rosing(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_rosing)))

    def get_sorted_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sorted_size)))

    def get_sorted_size_190(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sorted_size_190)))
    def get_pokaz (self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pokaz)))

    # #Action

    def click_sorted_brand(self):
        with allure.step("click_sorted_brand"):
            self.get_sorted_brand().click()

            self.get_select_rosing().click()
            self.get_sorted_size().click()
            self.get_sorted_size_190().click()
            self.get_pokaz().click()





        # time.sleep(10)
        print("sorted compleat")





import time

import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Sravnenie_page(Base):
    url = 'https://trial-sport.ru/'

        # Location


    searh = "//*[@id='asc']/div[2]/div/div/input"
    search_button = "//*[@id='srchFrm']/div[1]/div[1]/input"
    button_sr_1 = "//*[@id='obj2175034']/span[2]/span[6]/span[1]"
    button_sr_2 = "//*[@id='obj1524936']/span[2]/span[5]/span[1]"
    srav_button = "//*[@id='asc']/div[1]/div/div[2]/a[1]"
    srav_word = "/html/body/div[4]/div[3]/div[5]/div/div[1]/h1"

    def get_searh(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.searh)))

    def get_search_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_button)))

    def get_button_sr_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_sr_1)))

    def get_button_sr_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_sr_2)))

    def get_srav_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.srav_button)))

    def get_srav_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.srav_word)))

    def sravnivem(self):
        with allure.step("discount cart"):
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.get_searh().send_keys("Rossignol X-IUM SKATING WCS -S2 -IFP")
            self.get_search_button().click()
            self.get_button_sr_1().click()
            self.get_button_sr_2().click()
            self.get_srav_button().click()
            self.assert_word(self.get_srav_word(), "Сравнение товаров")
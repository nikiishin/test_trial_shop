import time

import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Select_city(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
        # Выбираем город для доставки
    city_input = "//*[@id='frm']/div/div[3]/table/tbody/tr[1]/td[3]/div[2]/input[1]"
    select_city = "//*[@id='frm']/div/div[3]/table/tbody/tr[1]/td[3]/div[2]/div/span[2]"


    # getters

    def get_city_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_input)))



    def get_select_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_city)))



    #
    # def get_main_word(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Action

    def input_city_input(self, city_input):
        self.get_city_input().send_keys(city_input)
        print("Input user_name")

    def click_select_city(self):
        self.get_select_city().click()
        print("Click login button")



    def selctions_city(self):
        with allure.step("selctions_city"):
            self.input_city_input("Москва")

            self.click_select_city()
            self.get_screenshot()
            time.sleep(3)


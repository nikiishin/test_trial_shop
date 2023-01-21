import time

import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Cdek_link(Base):
    url = 'https://trial-sport.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    deliv = "/html/body/div[4]/div[9]/div/div/div[1]/div[2]/div[2]/a"    # клик на каталог
    cdek = "/html/body/div[4]/div[3]/div[6]/span[3]/a"     # выбираем беговые лыжи

    # getters

    def get_deliv(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.deliv)))

    def get_cdek(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cdek)))

    def deliv_cdek(self):
        with allure.step("deliv_cdek"):
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.get_deliv().click()
            self.get_cdek().click()
            time.sleep(5)
            # self.get_current_url()




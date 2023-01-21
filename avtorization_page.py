import time

import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Avtorization_page(Base):
    url = 'https://trial-sport.ru/'

        # Location

    vhod_button = "//*[@id='asc']/div[1]/div/div[2]/div/span"
    login = "//*[@id='idLogForm']/table/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/div/input"
    pasword = "//*[@id='idLogForm']/table/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/div/input"
    go_button = "//*[@id='idLogForm']/table/tbody/tr/td[1]/table/tbody/tr[5]/td[2]/div/div/input"

    def get_vhod_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.vhod_button)))

    def get_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login)))

    def get_pasword(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pasword)))

    def get_go_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_button)))

    def avtorization(self):
        with allure.step("discount cart"):
            self.driver.get(self.url)
            self.driver.maximize_window()
            # self.get_current_url()
            self.get_vhod_button().click()
            self.get_login().send_keys("niksonik596959@gmail.com")
            self.get_pasword().send_keys("qwert12345")
            self.get_go_button().click()

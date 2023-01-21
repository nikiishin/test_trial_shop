import time

import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Adres_shop(Base):
    url = 'https://trial-sport.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # locators

    shop_link = "//*[@id='item5']/span"
    city_select = "//*[@id='ui-city_select']"
    select_oryl = "//*[@id='select1-group']/ul/li[38]/a"
    adres = "/html/body/div[4]/div[4]/div[4]/div[3]/div/div[1]/div/div[1]/div[1]/div"

    def get_shop_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shop_link)))

    def get_city_select(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_select)))

    def get_select_oryl(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_oryl)))

    def get_adres(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.adres)))


    def slection_shop(self):
        with allure.step("deliv_cdek"):
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.get_shop_link().click()
            self.get_city_select().click()
            self.get_select_oryl().click()
            self.assert_word(self.get_adres(), "ул. Розы Люксембург, д. 4")




import time

import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Select_ceeper_blin_hoccey(Base):
    url = 'https://trial-sport.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    catalog = "//*[@id='item1']"  # клик на каталог
    blin = "/html/body/div[4]/div[3]/div[6]/div/div[2]/span[1]/a"  # выбираем беговые лыжи
    dr_x6 = "//*[@id='obj1179889']/span[2]/a/span"
    main_word = "/html/body/div[4]/div[3]/div[6]/div[1]/div[2]/h2"
    pictire = "//*[@id='dslidermain']/div[1]/div/div[1]/div/a/img"
    right = "//*[@id='fancybox-right-ico']"
    left = "//*[@id='fancybox-left-ico']"

    # getters

    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_blin(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.blin)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_dr_x6(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dr_x6)))
    def get_pictire(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pictire)))

    def get_right(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.right)))

    def get_left(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.left)))

    # Action

    def selections_blin(self):
        with allure.step("selections_blin"):
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.get_catalog().click()
            self.get_blin().click()
            self.get_dr_x6().click()
            self.assert_word(self.get_main_word(), 'Блин вратаря DR X6 GOALIE BLOKER')

            self.get_pictire().click()
            self.get_right().click()
            self.get_left().click()

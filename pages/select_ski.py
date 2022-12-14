import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Select_ski(Base):
    url = 'https://trial-sport.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    catalog = "//*[@id='item1']"    # клик на каталог
    ski = "/html/body/div[4]/div[3]/div[6]/div/div[14]/span[3]"     # выбираем беговые лыжи

    main_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"



    # getters

    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_ski(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ski)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))



    # Action



    def selections(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.get_catalog().click()
        self.get_ski().click()
        self.assert_word(self.get_main_word(), 'Беговые лыжи')



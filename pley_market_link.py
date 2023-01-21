import time
from lib2to3.pgen2 import driver

import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Play_marcet_link(Base):
    url = 'https://play.google.com/store/apps/details?id=ru.amio.trialsport'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    play_marc = "/html/body/div[4]/div[9]/div/div/div[3]/div[2]/div[1]/a[1]/img"    # клик на каталог
    # cdek = "/html/body/div[4]/div[3]/div[6]/span[3]/a"     # выбираем беговые лыжи

    # getters

    def get_play_marc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.play_marc)))

    # def get_cdek(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cdek)))

    def play_marc_link(self):
        with allure.step("deliv_cdek"):
            self.driver.get('https://trial-sport.ru/')
            self.driver.maximize_window()
            # self.get_current_url()
            self.get_play_marc().click()
            time.sleep(5)
            self.driver.switch_to.window()





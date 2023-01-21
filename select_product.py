import time

import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Select_product(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    select_prof_ros = "//*[@id='obj2175034']/span[2]/a[1]"   #выбираем Беговые лыжи Rossignol X-IUM SKATING WCS -S2 -IFP
    main_word = "/html/body/div[4]/div[3]/div[6]/div[1]/div[2]/h2"



    # getters

    def get_select_prof_ros(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_prof_ros)))
    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))


    # #Action

    def click_select_prof_ros(self):
        with allure.step("click_select_prof_ros"):
            self.get_select_prof_ros().click()
            self.assert_word(self.get_main_word(), 'Беговые лыжи Rossignol X-IUM SKATING WCS -S2 -IFP')
            time.sleep(3)
            self.get_screenshot()



        print("sorted_price")


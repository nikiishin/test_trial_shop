import time

import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Discount_cart(Base):
    url = 'https://trial-sport.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    cart = "//*[@id='item7']/span"    # клик на каталог
    reg = "/html/body/div[4]/div[3]/div[6]/div/div[8]/a"     # выбираем беговые лыжи
    mail = "//*[@id='frmProfile']/table[1]/tbody/tr[1]/td[1]/div[2]/input"
    password = "//*[@id='frmProfile']/table[1]/tbody/tr[1]/td[3]/div[2]/input"
    last_name = "//*[@id='frmProfile']/table[1]/tbody/tr[3]/td[1]/div[2]/input"
    ferst_name = "//*[@id='frmProfile']/table[1]/tbody/tr[3]/td[3]/div[2]/input"
    bbd = "//*[@id='frmProfile']/table[1]/tbody/tr[5]/td[1]/div[2]/input"
    phone = "//*[@id='mobPhoneFld']/div[3]/div[2]/input"






    # getters

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_reg(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.reg)))

    def get_mail(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mail)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_ferst_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ferst_name)))

    def get_bbd(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.bbd)))

    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def info_dk(self):
        with allure.step("discount cart"):
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.get_cart().click()
            self.get_reg().click()
            time.sleep(5)
            self.get_current_url()
            self.get_mail().send_keys("anna@1991.com")
            self.get_password().send_keys("qwerty123456")
            self.get_last_name().send_keys("Туркова")
            self.get_ferst_name().send_keys("Анна")
            time.sleep(8)
            self.get_bbd().send_keys("13021991")
            self.get_phone().send_keys("+7 (999) 999-99-99")




import time

import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    cart = "//*[@id='item7']/span"  # кард
    reg = "/html/body/div[4]/div[3]/div[6]/div/div[8]/a"
    mail = "//*[@id='frmProfile']/table[1]/tbody/tr[1]/td[1]/div[2]/input"  # вводим пароль
    pasword = "//*[@id='frmProfile']/table[1]/tbody/tr[1]/td[3]/div[2]/input"  # вводим пароль
    mail = "//*[@id='frmProfile']/table[1]/tbody/tr[3]/td[1]/div[2]/input"  # вводим пароль
    mail = "//*[@id='frmProfile']/table[1]/tbody/tr[1]/td[1]/div[2]/input"  # вводим пароль
    mail = "//*[@id='frmProfile']/table[1]/tbody/tr[1]/td[1]/div[2]/input"  # вводим пароль
    mail = "//*[@id='frmProfile']/table[1]/tbody/tr[1]/td[1]/div[2]/input"  # вводим пароль

    login_button = "//*[@id='logcartfrm']/table/tbody/tr/td[1]/table/tbody/tr[5]/td[2]/div/div/input"
    # main_word = "//*[@id='header_container']/div[2]/span"


    #getters

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_reg(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.reg)))

    def get_mail(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mail)))

    def get_pasword(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pasword)))

    def get_mail(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mail)))

    def get_mail(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mail)))

    def get_mail(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mail)))

    def get_mail(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mail)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))
    #
    # def get_main_word(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))


    #Action

    def click_cart(self):
        self.get_cart().click()
        print("click_cart")

    def click_reg(self):
        self.get_reg().click()
        print("click_reg")

    def input_mail(self, mail):
        self.get_mail().send_keys(mail)
        print("Input mail")

    def input_pasword(self, pasword):
        self.get_pasword().send_keys(pasword)
        print("Input pasword")
    def input_mail(self, mail):
        self.get_mail().send_keys(mail)
        print("Input mail")
    def input_mail(self, mail):
        self.get_mail().send_keys(mail)
        print("Input mail")
    def input_mail(self, mail):
        self.get_mail().send_keys(mail)
        print("Input mail")
    def input_mail(self, mail):
        self.get_mail().send_keys(mail)
        print("Input mail")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")








    def authorization(self):
        with allure.step("authorization"):

            self.click_cart()
            self.click_reg()
            time.sleep(5)
            self.input_mail('anna@677.com')
            self.input_pasword('qwerty123456')

            self.click_login_button()
            # self.assert_word(self.get_main_word(), 'PRODUCTS')




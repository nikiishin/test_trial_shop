import time

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
    user_name = "//*[@id='logcartfrm']/table/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/div/input"  # воодим логин
    password = "//*[@id='logcartfrm']/table/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/div/input"  # вводим пароль
    login_button = "//*[@id='logcartfrm']/table/tbody/tr/td[1]/table/tbody/tr[5]/td[2]/div/div/input"
    # main_word = "//*[@id='header_container']/div[2]/span"


    #getters

    def get_username(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))
    #
    # def get_main_word(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))


    #Action

    def input_user_name(self, user_name):
        self.get_username().send_keys(user_name)
        print("Input user_name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")








    def authorization(self):

        self.input_user_name("axakg@mailto.plus")
        time.sleep(5)
        self.input_password('qwerty123456')
        self.click_login_button()
        # self.assert_word(self.get_main_word(), 'PRODUCTS')




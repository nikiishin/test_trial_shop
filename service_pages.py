import time

import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Service_link(Base):
    url = 'https://trial-sport.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    towar = "/html/body/div[4]/div[9]/div/div/div[1]/div[2]/div[1]/a"
    towar_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"
    deliv = "/html/body/div[4]/div[4]/div/div/div[1]/div[2]/div[2]/a"
    deliv_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"
    return_order = "/html/body/div[4]/div[4]/div/div/div[1]/div[2]/div[3]/a"
    return_order_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"
    pay = "/html/body/div[4]/div[4]/div/div/div[1]/div[2]/div[4]/a"
    pay_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"
    size_table = "/html/body/div[4]/div[4]/div/div/div[1]/div[2]/div[5]/a"
    size_table_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"
    instruction = "/html/body/div[4]/div[4]/div/div/div[1]/div[2]/div[6]/a"
    instruction_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"
    garantia = "/html/body/div[4]/div[4]/div/div/div[1]/div[2]/div[7]/a"
    garantia_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"
    carta_suit = "/html/body/div[4]/div[4]/div/div/div[1]/div[2]/div[8]/a"
    carta_suit_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"



    # getters

    def get_towar(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.towar)))

    def get_towar_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.towar_word)))
    def get_deliv(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.deliv)))

    def get_deliv_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.deliv_word)))
    def get_return_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.return_order)))

    def get_return_order_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.return_order_word)))
    def get_pay(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pay)))

    def get_pay_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pay_word)))
    def get_size_table(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.size_table)))

    def get_size_table_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.size_table_word)))
    def get_instruction(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.instruction)))

    def get_instruction_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.instruction_word)))
    def get_garantia(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.garantia)))

    def get_garantia_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.garantia_word)))
    def get_carta_suit(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.carta_suit)))

    def get_carta_suit_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.carta_suit_word)))



    def menu_service_help(self):
        with allure.step("Help i sevice"):
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.get_towar().click()
            self.assert_word(self.get_towar_word(), "Как заказать товар")
            self.get_deliv().click()
            self.assert_word(self.get_deliv_word(), "Условия доставки")
            self.get_return_order().click()
            self.assert_word(self.get_return_order_word(), "Возврат и обмен")
            self.get_pay().click()
            self.assert_word(self.get_pay_word(), "Оплата")
            self.get_size_table().click()
            self.assert_word(self.get_size_table_word(), "Таблицы размеров")
            self.get_instruction().click()
            self.assert_word(self.get_instruction_word(), "Инструкции к товарам")
            self.get_garantia().click()
            self.assert_word(self.get_garantia_word(), "Гарантийные обязательства")
            self.get_carta_suit().click()
            self.assert_word(self.get_carta_suit_word(), "Карта сайта")





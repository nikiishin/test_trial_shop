import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Delivery_pages(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    # Вводим информацию о доставки
    index = "//*[@id='for_delivery2']/table/tbody/tr[3]/td[2]/div/input"
    street = "//*[@id='for_delivery2']/table/tbody/tr[5]/td[2]/div/input"
    home = "//*[@id='for_delivery2']/table/tbody/tr[7]/td[2]/div/input"
    corp = "//*[@id='for_delivery2']/table/tbody/tr[9]/td[2]/div/input"
    kvartira = "//*[@id='for_delivery2']/table/tbody/tr[11]/td[2]/div/input"
    fio = "//*[@id='for_delivery2']/table/tbody/tr[13]/td[2]/div/input"
    phone_number = "//*[@id='for_delivery2']/table/tbody/tr[15]/td[2]/div/input"
    nomber_discount = "//*[@id='for_delivery2']/table/tbody/tr[17]/td[2]/div/input"
    koment = "//*[@id='for_delivery2']/table/tbody/tr[19]/td[2]/div/textarea"
    call_operator = "//*[@id='frm']/div/div/table[1]/tbody/tr/td[2]/div/div[3]"
    #переходим на оплату
    conti_order = "//*[@id='frm']/div/div/table[2]/tbody/tr/td[3]/div/div/input"

    # getters

    def get_index(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.index)))

    def get_street(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.street)))

    def get_home(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.home)))

    def get_corp(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.corp)))

    def get_kvartira(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.kvartira)))

    def get_fio(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.fio)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_nomber_discount(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.nomber_discount)))

    def get_koment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.koment)))

    def get_call_operator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.call_operator)))

    def get_conti_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.conti_order)))

    # Action

    def input_index(self, index):
        self.get_index().send_keys(index)
        print("Input index")

    def input_street(self, street):
        self.get_street().send_keys(street)
        print("Input street ")

    def input_home(self, home):
        self.get_home().send_keys(home)
        print("input home")

    def input_corp(self, corp):
        self.get_corp().send_keys(corp)
        print("input corp")

    def input_kvartira(self, kvartira):
        self.get_kvartira().send_keys(kvartira)
        print("Input kvartira")

    def input_fio(self, fio):
        self.get_fio().send_keys(fio)
        print("Input fio ")

    def input_phone_number(self, phone_number):
        self.get_phone_number().send_keys(phone_number)
        print("input home")

    def input_nomber_discount(self, nomber_discount):
        self.get_nomber_discount().send_keys(nomber_discount)
        print("input nomber_discount")

    def input_koment(self, koment):
        self.get_koment().send_keys(koment)
        print("input koment")

    def click_call_operator(self):
        self.get_call_operator().click()
        print("Click call_operator")

    def click_conti_order(self):
        self.get_conti_order().click()
        print("Click conti_order")

    # method

    def inform_user(self):
        self.get_screenshot()
        self.input_index("130234")
        self.input_street("Ленина")
        self.input_home("35")
        self.input_corp("3")
        self.input_kvartira("56")
        self.input_fio("Алексеев Алексей Алексеич")
        self.input_phone_number("+7 (999) 999-99-99")
        self.input_nomber_discount("78565115")
        self.input_koment("Вес лыжника 98кг рос 188")
        self.click_call_operator()
        self.click_conti_order()
        self.get_screenshot()
        time.sleep(10)

        # self.click_continue_button()

import time

import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Information_page(Base):
    url = 'https://trial-sport.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    adrees_phone_number = "/html/body/div[4]/div[9]/div/div/div[2]/div[2]/div[1]/a"
    adrees_phone_number_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"
    adress_service = "/html/body/div[4]/div[6]/div/div/div[2]/div[2]/div[2]/a"
    adress_service_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"
    work_trial = "/html/body/div[4]/div[4]/div/div/div[2]/div[2]/div[3]/a"
    work_trial_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"
    team = "/html/body/div[4]/div[4]/div/div/div[2]/div[2]/div[4]/a"
    team_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"
    link = "/html/body/div[4]/div[4]/div/div/div[2]/div[2]/div[5]/a"
    link_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"
    feadbeak = "/html/body/div[4]/div[4]/div/div/div[2]/div[2]/div[6]/a"
    feadbeak_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"
    opt = "/html/body/div[4]/div[4]/div/div/div[2]/div[2]/div[7]/a"
    opt_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"
    arenda = "/html/body/div[4]/div[4]/div/div/div[2]/div[2]/div[8]/a"
    arenda_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"
    privace = "/html/body/div[4]/div[4]/div/div/div[2]/div[2]/div[9]/a"
    privace_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"
    moshenik = "/html/body/div[4]/div[4]/div/div/div[2]/div[2]/div[10]/a"
    moshenik_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"



    # getters

    def get_adrees_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.adrees_phone_number)))

    def get_adrees_phone_number_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.adrees_phone_number_word)))
    def get_adress_service(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.adress_service)))

    def get_adress_service_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.adress_service_word)))
    def get_work_trial(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.work_trial)))

    def get_work_trial_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.work_trial_word)))
    def get_team(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.team)))

    def get_team_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.team_word)))
    def get_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link)))

    def get_link_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_word)))
    def get_feadbeak(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.feadbeak)))

    def get_feadbeak_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.feadbeak_word)))
    def get_opt(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.opt)))

    def get_opt_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.opt_word)))
    def get_arenda(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.arenda)))

    def get_arenda_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.arenda_word)))

    def get_privace(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.privace)))

    def get_privace_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.privace_word)))

    def get_moshenik(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.moshenik)))

    def get_moshenik_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.moshenik_word)))



    def menu_information(self):
        with allure.step("Information menu"):
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.get_adrees_phone_number().click()
            self.assert_word(self.get_adrees_phone_number_word(), "Адреса магазинов")
            self.get_adress_service().click()
            self.assert_word(self.get_adress_service_word(), "Сервисные центры")
            self.get_work_trial().click()
            self.assert_word(self.get_work_trial_word(), "Работа в Триал-Спорт")
            self.get_team().click()
            self.assert_word(self.get_team_word(), "Команда")
            self.get_link().click()
            self.assert_word(self.get_link_word(), "Ссылки")
            self.get_feadbeak().click()
            self.assert_word(self.get_feadbeak_word(), "Обратная связь")
            self.get_opt().click()
            self.assert_word(self.get_opt_word(), "Оптовые поставки")
            self.get_arenda().click()
            self.assert_word(self.get_arenda_word(), "Арендодателям")
            self.get_privace().click()
            self.assert_word(self.get_privace_word(), "Пользовательское соглашение о конфиденциальности")
            self.get_moshenik().click()
            self.assert_word(self.get_moshenik_word(), "Осторожно, мошенники!")





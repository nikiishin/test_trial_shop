import time

import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Dop_menu_page(Base):
    url = 'https://trial-sport.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    catalog = "//*[@id='item1']"  # клик на каталог
    catalog_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"


    sale = "//*[@id='item2']/span"
    sale_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"
    news = "//*[@id='item3']/span"
    news_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"
    media = "//*[@id='item4']/span"
    photo = "//*[@id='mm1']/span"

    photo_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"
    video = "//*[@id='mm2']/span"
    video_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"
    statia = "//*[@id='mm3']/span"
    statia_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"
    adresa_shop = "//*[@id='item5']/span"
    adresa_shop_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"
    contakt = "//*[@id='item6']/span"
    obratnya_svaz = "//*[@id='com1']/span"
    obratnya_svaz_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"
    opt = "//*[@id='com2']/span"
    opt_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"


    arenda = "//*[@id='com3']/span"
    arenda_word = "/html/body/div[4]/div[3]/div[5]/div[1]/div[1]/h1"
    discount_cart = "//*[@id='item7']/span"
    discount_cart_word = "/html/body/div[4]/div[3]/div[6]/div/h2"




    # getters

    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_catalog_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_word)))
    def get_sale(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sale)))

    def get_sale_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sale_word)))
    def get_news(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.news)))

    def get_news_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.news_word)))
    def get_media(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.media)))

    def get_photo(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.photo)))

    def get_photo_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.photo_word)))
    def get_video(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.video)))

    def get_video_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.video_word)))
    def get_statia(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.statia)))

    def get_statia_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.statia_word)))
    def get_adresa_shop(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.adresa_shop)))

    def get_adresa_shop_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.adresa_shop_word)))
    def get_contakt(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.contakt)))
    def get_obratnya_svaz(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.obratnya_svaz)))

    def get_obratnya_svaz_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.obratnya_svaz_word)))

    def get_opt(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.opt)))

    def get_opt_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.opt_word)))

    def get_arenda(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.arenda)))

    def get_arenda_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.arenda_word)))

    def get_discount_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.discount_cart)))

    def get_discount_cart_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.discount_cart_word)))



    def dop_menu_inform(self):
        with allure.step("Dop menu"):
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.get_catalog().click()
            self.assert_word(self.get_catalog_word(), "Каталог")
            self.get_sale().click()
            self.assert_word(self.get_sale_word(), "Акции и скидки")
            self.get_news().click()
            self.assert_word(self.get_news_word(), "Новости")
            self.get_media().click()
            self.get_photo().click()

            self.assert_word(self.get_photo_word(), "Фото")
            self.get_media().click()

            self.get_video().click()
            self.assert_word(self.get_video_word(), "Видео")
            self.get_media().click()

            self.get_statia().click()
            self.assert_word(self.get_statia_word(), "Статьи")
            self.get_adresa_shop().click()
            self.assert_word(self.get_adresa_shop_word(), "Адреса магазинов")
            self.get_contakt().click()
            self.get_obratnya_svaz().click()

            self.assert_word(self.get_obratnya_svaz_word(), "Обратная связь")
            self.get_contakt().click()

            self.get_opt().click()
            self.assert_word(self.get_opt_word(), "Оптовые поставки")
            self.get_contakt().click()

            self.get_arenda().click()
            self.assert_word(self.get_arenda_word(), "Арендодателям")
            self.get_discount_cart().click()
            self.assert_word(self.get_discount_cart_word(), 'Дисконтная карта "Триал-Cпорт"')





from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from selenium.webdriver.common.action_chains import ActionChains




class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.action = ActionChains(driver)
        self.driver = driver




    # Locators

    slider_size = "//*[@id='mfilter-box-1']/div/ul/li[2]/div[2]/div[1]/div[1]/div[3]/div/div[3]" # ползунок для фильтра по размерам
    checkbox_size = "//input[@value='30-размер']"                                                # чек-бокс 30 размер в фильтре
    checkbox_brand = "//input[@value='Котофей']"                                                 # чек-бокс торговая марка 'Котофей'
    buy_button = "(//button[@type='button'])[6]"                                                 # кнопка 'купить'
    shopping_cart_button = "//div[@id='cart']"                                                   # выпадающее меню 'корзина'
    go_shopping_cart = "(//i[@class='fa fa-shopping-cart'])[3]"                                  # кнопка 'перейти в корзину' в выпадающем меню

   
    # Getters


    def get_slider_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slider_size)))

    def get_checkbox_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_size)))

    def get_checkbox_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_brand)))

    def get_buy_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_button)))

    def get_shopping_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shopping_cart_button)))


    def get_go_shopping_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_shopping_cart)))


    # Actions


    def clic_slider_size(self):
        self.action.click_and_hold(self.get_slider_size()).move_by_offset(0, 50).release().perform()
        print("click and hold slider size")

    def clic_checkbox_size(self):
        self.get_checkbox_size().click()
        print("Clic checkbox size")

    def clic_checkbox_brand(self):
        self.get_checkbox_brand().click()
        print("Clic checkbox brand")

    def clic_buy_button(self):
        self.get_buy_button().click()
        print("Clic buy button")

    def clic_shopping_cart_button(self):
        self.get_shopping_cart_button().click()
        print("Clic shopping cart button")

    def clic_go_shopping_cart(self):
        self.get_go_shopping_cart().click()
        print("Clic go shopping cart")



    # Methods

    def select_products_1(self):         # метод с фильтрами переноса товара в корзину

        self.get_current_url()           # получаем текущую URL
        self.clic_checkbox_size()        # тянем ползунок фильтра по размерам вниз
        self.clic_checkbox_brand()       # ставим галочку в фильтре по брендам
        self.clic_buy_button()           # нажимаем кнопку 'купить'
        self.clic_shopping_cart_button() # нажимаем выпадающее меню 'корзина'
        self.clic_go_shopping_cart()     # нажимаем надпись 'перейти в корзину'


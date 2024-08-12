from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Cart_page(Base): # страница корзины

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    word_model = "(//td[@class='text-left'])[6]"    # модель обуви - текст
    making_order = "//a[@class='btn btn-primary']"  # кнопка 'оформление заказа'



    # Getters

    def get_word_model(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_model)))

    def get_making_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.making_order)))



    # Actions

    def clic_making_order(self):
        self.get_making_order().click()
        print("Clic making order")



    # Methods


    def product_confirmation(self):                                # Метод подтверждения продукта в корзине
        self.get_current_url()                                     # Получаем текущую URL
        self.assert_word(self.get_word_model(), "464067-42") # Сравниваем артикул обуви с ожидаемым текстом
        self.clic_making_order()                                   # Нажимаем кнопку 'оформление заказа'
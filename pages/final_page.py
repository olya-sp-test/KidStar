import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Final_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.actions = ActionChains(driver)
        self.driver = driver

    # Locators

    word_verification = "//h1[contains(text(), 'Оформление заказа')]" # ключевое слово для сравнения с ожидаемым
    pickup = "//input[@id='pickup.pickup']"                           # radio-button 'самовывоз из магазина'
    order_confirmation = "(//input[@id='button-confirm'])[2]"         # кнопка 'подтверждение заказа'




    # Getters

    def get_word_verification(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_verification)))

    def get_pickup(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pickup)))

    def get_order_confirmation(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_confirmation)))






    # Actions

    def clic_pickup(self):
        self.actions.move_to_element(self.get_pickup()).perform()
        self.get_pickup().click()
        print("Clic pickup")

    def clic_order_confirmation(self):

        self.get_order_confirmation().click()
        print("Clic order confirmation")










    # Methods

    def final_design(self):                                                        # метод на финальной странице
        self.assert_word(self.get_word_verification(), "Оформление заказа")  # сравниваем текст с ожидаемым
        self.clic_pickup()                                                         # ставим галочку на 'самовывоз из магазина'
        self.get_order_confirmation()                                              # нажимаем кнопку 'подтверждение заказа'
        time.sleep(5)
        self.get_screenshot()                                                      # делаем скриншот



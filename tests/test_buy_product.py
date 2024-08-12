import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.Main_page import Main_page
from pages.cart_page import Cart_page
from pages.final_page import Final_page
# from pages.cart_page import Cart_page
# from pages.client_information_page import Client_information_page
# from pages.finish_page import Finish_page
from pages.login_page import LoginPage
# from pages.main_page import Main_page
# from pages.payment_page import Payment_page


# @pytest.mark.run(order=1) # очередность прохождения теста
def test_buy_product_1():                                      # тест полного пути покупки товара
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    print("Start Test 1")

    login = LoginPage(driver)
    login.authorization()                                      # авторизация

    mp = Main_page(driver)
    mp.select_products_1()                                     # фильтры и отправка товара в корзину

    cp = Cart_page(driver)
    cp.product_confirmation()                                  # действия в корзине

    fp = Final_page(driver)                                    # действия на финальной странице -
    fp.final_design()                                          # - с подтверждением и оформлением заказа

    print("Finish Test 1")
    driver.quit()










from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
class LoginPage(Base):

    url = 'https://xn--80ahlh7aeh.xn--p1ai/detskaya_obuv/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # Locators

    personal_account = "//a[@title='Личный кабинет']"                  # выпадающее меню личный кабинет
    authorization_locator = "//*[@id='top-links']/ul/li[2]/ul/li[2]/a" # авторизация в выпадающем меню
    mail_locator = "//input[@id='input-email']"                        # поле для почты
    password = "//input[@id='input-password']"                         # поле для пароля
    login_button = "//input[@value='Войти']"                           # кнопка 'войти'
    button_shoes = "//ul[@class='nav navbar-nav']"                     # кнопка 'обувь'
    main_word = "//div[@class='col-sm-10']"                            # текст для сравнения с ожидаемым



    # Getters

    def get_personal_account(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.personal_account)))

    def get_authorization_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.authorization_locator)))

    def get_mail_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mail_locator)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_button_shoes(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_shoes)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))



    # Actions

    def clic_personal_account(self):

        self.get_personal_account().click()
        print("Clic personal account")

    def clic_authorization_locator(self):

        self.get_authorization_locator().click()
        print("Clic authorization locator")

    def input_mail_locator(self, mail_locator):
        self.get_mail_locator().send_keys(mail_locator)
        print("Input mail")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def clic_login_button(self):
        self.get_login_button().click()
        print("Clic login button")

    def clic_button_shoes(self):
        self.get_button_shoes().click()
        print("Clic button shoes")



    # Methods

    def authorization(self):                             # метод авторизации в системе

        self.driver.get(self.url)                        # заходим на сайт
        self.driver.maximize_window()                    # увеличиваем окно браузера
        self.get_current_url()                           # печатаем URL
        self.clic_personal_account()                     # вызывам выпадающее меню 'личный кабинет'
        self.clic_authorization_locator()                # нажимаем 'авторизация'
        self.input_mail_locator("latyshieva.83@mail.ru") # заполняем поле 'E-Mail'
        self.input_password("1234")                      # заполняем поле 'пароль'
        self.clic_login_button()                         # нажимаем кнопку 'войти'
        self.clic_button_shoes()                         # нажимаем надпись-кнопку 'обувь'
        self.assert_word(self.get_main_word(), "Детская обувь. с гарантией лучшей цены в 120% от лучших производителей")
                                                         # сверяем надпись с ожидаемой
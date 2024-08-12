import datetime

class Base():

    def __init__(self, driver):
        self.driver = driver


    """Метод получения URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)


    """Метод сравнения текста с ожидаемым"""

    def assert_word(selfs, word, result):
        """Проверка значения текста"""
        value_word = word.text
        assert value_word == result
        print("Значение текста верно")



    """Метод получения скриншота"""

    def get_screenshot(self):
        now_data = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_data + '.png'
        self.driver.save_screenshot(f"./Screen/{name_screenshot}")
        print("Скриншот выполнен")



    """Метод сравнения текущей URL с ожидаемой"""

    def aseert_url(self, result):
        """Проверка корректности URL"""
        get_url = self.driver.current_url
        assert get_url == result
        print("Корректная URL")

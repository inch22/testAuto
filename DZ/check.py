
from selenium import webdriver
from selenium.webdriver.common.by import By

# создайте класс Check класс принимают 1 аргумент при инициализации (Loc)
class Check:
    def __init__(self, loc):
        self.loc = loc


    def exist(self, url): #создаем метод exist, который принимает 2 аргумента self, url
            #реализуем переход на url,
            driver = webdriver.Chrome()
            driver.get(url)
            #поиск элемента по локатору
            input_username = driver.find_element(By.CSS_SELECTOR, self.loc)
            #вывод в консоль ответа, найден элемент или нет
            if input_username is None:
                    print("Элемент не найден")
            else:
                    print("Элемент найден")



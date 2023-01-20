from selenium import webdriver
from selenium.webdriver.common.by import By

class Check:
    def __init__(self, url):
        self.url = url

    def exist(self):
            driver = webdriver.Chrome()
            driver.exist(self. url)

home =  Check("https://guruvkusa.ru/")
home.exist()
input_username = driver.find_element(By.CSS_SELECTOR,'body > div.page_layout.page_layout-clear > header > div.layout.widget-type_widget_v4_header_4_6b677bbb4943ee7655d464f5e60d70e2 > div > div.header.header_no-languages > div.header-mobile-panel > div > div.header-mobile-panel__bottom > button')
if input_username is None:
    print("Элемент не найден")
else:
    print("Элемент найден")

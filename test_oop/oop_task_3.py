from selenium import webdriver
class Page:

    def __init__(self, url):
        self.url = url

    def get(self):
        driver = webdriver.Chrome()
        driver.get(self. url)

home =  Page("https://stepik.org/")
home.get()


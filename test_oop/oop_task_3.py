from selenium import webdriver
class Page:

    def __init__(self, url):
        self.url = url

    def get(self):
        driver = webdriver.Chrome()
        driver.get(self. url)

hom =  Page("https://stepik.org/")
hom.get()


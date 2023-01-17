from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://selenium.dev/selenium/web/web-form.html/")
input_username = driver.find_element(By.XPATH,'//*[@id="my-text-id"]')
if input_username is None:
    print("Элемент не найден")
else:
    print("Элемент найден")

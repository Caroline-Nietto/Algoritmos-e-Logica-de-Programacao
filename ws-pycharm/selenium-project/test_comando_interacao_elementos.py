import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://www.saucedemo.com/v1/")


#find element() encontro os campos que quero acessar
username = browser.find_element(By.ID, "user-name")
password= browser.find_element(By.ID, "password")
btn_login = browser.find_element(By.ID, "login-button")


# send_keys() preenchimento do login e senha
username.send_keys("standard_user")
password.send_keys("secret_sauce")

# click() clicar no botao login que mapiei
btn_login.click()

# text
products_title = browser.find_element(By.XPATH, "//div[@class='product_label']")
print(products_title.text)
assert products_title.text == "Products"

# get_attribute()
img_backpack = browser.find_element(By.XPATH, "(//img[@class='inventory_item_img'])[1]")
print(img_backpack.get_attribute("src"))

name = browser.find_element(By.XPATH, "//select[@class='product_sort_container']")
print(name.get_attribute("class"))
assert name.get_attribute("class") == "product_sort_container"
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Abre o navegador e entra na pagina de login
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.saucedemo.com/v1/")

# Faz o login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Seleciona um produto e add ao carrinho
driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']").click()
driver.find_element(By.XPATH, "//*[@class='btn_primary btn_inventory']").click()

# Clica no carrinho para verificar se o produto foi add
driver.find_element(By.XPATH, "//*[@class='shopping_cart_container']").click()
assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

# Volta para pagina de Produtos
driver.find_element(By.XPATH, "//*[@class='btn_secondary']").click()

# Seleciona outro produto e add ao carrinho
driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").click()
driver.find_element(By.XPATH, "//*[@class='btn_primary btn_inventory']").click()

# Clica no carrinho para verificar se os dois produtos foram add
driver.find_element(By.XPATH, "//*[@class='shopping_cart_container']").click()
assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed()
assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
time.sleep(3)

# Clica no botão Checkout
driver.find_element(By.XPATH, "//*[@class='btn_action checkout_button']").click()

# Preenche suas informaçoes e clica no botão Continuar
driver.find_element(By.ID, "first-name").send_keys("jao")
driver.find_element(By.ID, "last-name").send_keys("silva")
driver.find_element(By.ID, "postal-code").send_keys("123")
driver.find_element(By.XPATH, "//*[@class='btn_primary cart_button']").click()
time.sleep(3)

# Na pagina Overview clico em finish para finalizar minha compra
driver.find_element(By.XPATH, "//*[@class='btn_action cart_button']").click()
time.sleep(3)

# Verifico se a msg 'Thank for your order' está aparecendo na tela
assert driver.find_element(By.XPATH, "//*[@class='complete-header']").is_displayed()
time.sleep(3)



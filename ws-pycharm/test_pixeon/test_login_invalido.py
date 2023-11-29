import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# Abre a página para login
driver.get("https://the-internet.herokuapp.com/login")

# Encontra e preenche os campos com usuário e senha
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword")

# Clica no botão de fazer login
driver.find_element(By.XPATH, "//*[@class='fa fa-2x fa-sign-in']").click()

# Verifica se o login é valido
assert driver.find_element(By.XPATH, "//*[@id='flash']").is_displayed()
driver.quit()
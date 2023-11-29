import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# Acessa a página
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

# Encontra o botão Start e clica nele
driver.find_element(By.XPATH, "//div[@id='start']/button").click()
time.sleep(10)

# Verifica se a mensagem 'Hello word' está aparecendo na tela
assert driver.find_element(By.XPATH, "//div[@id='finish']/h4").is_displayed()

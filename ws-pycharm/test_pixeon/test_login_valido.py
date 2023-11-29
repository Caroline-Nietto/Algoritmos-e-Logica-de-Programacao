import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.XPATH, "//*[@class='fa fa-2x fa-sign-in']").click()

assert driver.find_element(By.XPATH, "//*[@class='subheader']").is_displayed(), f"Login efetuado com sucesso"
driver.quit()
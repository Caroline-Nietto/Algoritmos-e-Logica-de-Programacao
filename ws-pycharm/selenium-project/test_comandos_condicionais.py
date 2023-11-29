import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://demo.applitools.com/")

username = browser.find_element(By.ID, "username")
checkbox_remember_me = browser.find_element(By.XPATH, "//*[@class='form-check-label']")

# is_displayed()
print(username.is_displayed())
assert username.is_displayed()

# is_enabled()
print(username.is_enabled())
assert username.is_enabled()

# is_select()
print(checkbox_remember_me.is_selected())
assert not checkbox_remember_me.is_selected()

# clicando no cheackbox
time.sleep(2)
checkbox_remember_me.click()
time.sleep(2)

print(checkbox_remember_me.is_selected())
assert checkbox_remember_me.is_selected()
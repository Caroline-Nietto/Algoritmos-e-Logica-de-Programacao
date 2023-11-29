import time
from selenium import webdriver

browser = webdriver.Chrome()


# maximize_window()
browser.maximize_window()

# get()
browser.get("https://google.com")
time.sleep(2)

# refresh()
browser.refresh()
time.sleep(2)

# get()
browser.get("https://www.saucedemo.com/v1/")
time.sleep(2)

# back()
browser.back()
time.sleep(3)

# forward()
browser.forward()
time.sleep(3)

browser.switch_to.new_window("tab")
time.sleep(4)

# close()
browser.close()
time.sleep(3)

# quit()
browser.switch_to.new_window("tab")
browser.switch_to.new_window("tab")
time.sleep(3)
browser.quit()
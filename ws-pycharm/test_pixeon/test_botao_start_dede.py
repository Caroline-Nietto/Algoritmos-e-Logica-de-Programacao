import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# create a new instance of the Chrome driver
driver = webdriver.Chrome()

# navigate to the webpage with the button element
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

# find the button element with text "start"
button = driver.find_element_by_xpath("//button[contains(text(), 'start')]")

# capture the button element
button_screenshot = button.screenshot_as_png

# save the screenshot as an image file
with open("button.png", "wb") as file:
    file.write(button_screenshot)
time.sleep(5)
# close the browser
driver.quit()
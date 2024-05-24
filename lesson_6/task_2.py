from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")

input = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input.clear()
input.send_keys("SkyPro")
button = driver.find_element(By.CSS_SELECTOR, '#updatingButton')
button.click()
print(button.text)

sleep(5)  
driver.quit() 
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("http://uitestingplayground.com/dynamicid")

button = driver.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]') 
for i in range(1,4):
    if i <= 4:
        button.send_keys(Keys.RETURN)
        print('нажато', i)

sleep(10)
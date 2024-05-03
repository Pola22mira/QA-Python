from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login")
   
sleep(3)

field_username_locftor = '#username'
field_password_locftor = '#password'
button_locator = 'button.radius'

input_field_username = driver.find_element(By.CSS_SELECTOR, '#username') 
input_field_username.send_keys("tomsmith")
sleep(3)

input_field_password = driver.find_element(By.CSS_SELECTOR, '#password') 
input_field_password.send_keys("SuperSecretPassword!")
sleep(3)

driver.find_element(By.CSS_SELECTOR, 'button.radius').click() 
sleep(3)
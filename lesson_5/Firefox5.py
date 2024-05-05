from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
options=Options()
firefox_profile = FirefoxProfile()
firefox_profile.set_preference("javascript.enabled", False)
options.profile = firefox_profile
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/inputs")
    
sleep(4)

input_field = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]') 

input_field.send_keys("1000")
    
sleep(4)
input_field.clear()
sleep(4)

input_field.send_keys("999")
sleep(4)
driver.quit()
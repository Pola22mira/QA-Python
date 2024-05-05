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
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(5)

element = driver.find_element(By.CSS_SELECTOR, '#modal .modal-footer')
element.click()
sleep(5)

driver.quit()
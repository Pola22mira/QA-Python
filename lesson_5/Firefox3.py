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
driver.get("http://uitestingplayground.com/classattr")


button = driver.find_element(By.CSS_SELECTOR, '.btn-primary') 
i = 1
while i <= 3:
    try:
        button.send_keys(Keys.ENTER)
        print('нажато ENTER', i)
        i = i + 1
    except:
        button.send_keys(Keys.ESCAPE)
        print('нажато ESC')
    
sleep(5)
driver.quit()
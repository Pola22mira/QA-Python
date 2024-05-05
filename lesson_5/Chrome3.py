from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

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
    
sleep(10)
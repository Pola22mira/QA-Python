from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10) 

def test_calculator():
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    input_delay = driver.find_element(By.ID, 'delay')
    input_delay.clear()
    input_delay.send_keys("45")
    
    button_7 = driver.find_element(By.XPATH, '//div[@class="keys"]/span[text()="7"]')
    button_7.click()
    
    button_plus = driver.find_element(By.XPATH, '//div[@class="keys"]/span[text()="+"]')
    button_plus.click()
    
    button_8 = driver.find_element(By.XPATH, '//div[@class="keys"]/span[text()="8"]')
    button_8.click()
    
    button_equal = driver.find_element(By.XPATH, '//div[@class="keys"]/span[text()="="]')
    button_equal.click()
    
    sleep(45)
    value = driver.find_element(By.CSS_SELECTOR, 'div.screen').text
    assert value == '15'
    
    driver.quit()
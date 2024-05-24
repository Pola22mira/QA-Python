from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10) 

def test_buying():
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.find_element(By.ID, 'user-name').clear()
    driver.find_element(By.ID, 'user-name').send_keys("standard_user")
    driver.find_element(By.ID, 'password').clear()
    driver.find_element(By.ID, 'password').send_keys("secret_sauce")
    driver.find_element(By.ID, 'login-button').click()

    item = driver.find_element(By.XPATH, '//div[text()="Sauce Labs Backpack"]/ancestor::div[@class="inventory_item_description"]')
    item.find_element(By.TAG_NAME, 'button').click()

    item = driver.find_element(By.XPATH, '//div[text()="Sauce Labs Bolt T-Shirt"]/ancestor::div[@class="inventory_item_description"]')
    item.find_element(By.TAG_NAME, 'button').click()

    item = driver.find_element(By.XPATH, '//div[text()="Sauce Labs Onesie"]/ancestor::div[@class="inventory_item_description"]')
    item.find_element(By.TAG_NAME, 'button').click()
 
    driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()
    driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys("Polina")
    driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys("Novikova")
    driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, '#continue').click()

    sum = driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
    assert '$58.29' in sum

    driver.quit()
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
driver.implicitly_wait(4) 

def test_input_fields():
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.maximize_window()

    driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys("SkyPro")
    driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').clear()
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    zip_code_color = driver.find_element(By.CSS_SELECTOR, '#zip-code')
    assert zip_code_color.get_attribute("class") == "alert py-2 alert-danger"

    other_fields = ['#first_name, #input_last_name, #input_address, #input_email, #input_phone, #input_city, #input_country, #job_position, #company']
    for field in other_fields:
        assert driver.find_element(By.CSS_SELECTOR, field).get_attribute("class") == "alert py-2 alert-success"

    driver.quit()
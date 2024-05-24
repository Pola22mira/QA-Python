from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter = WebDriverWait(driver, 40, 0.1)
waiter.until(
    EC.text_to_be_present_in_element((By.XPATH, '//p[@class="lead"]'), 'Done!')
)
src = driver.find_element(By.CSS_SELECTOR, '#image-container>#award').get_attribute("src")
print(src)

sleep(5)  
driver.quit() 
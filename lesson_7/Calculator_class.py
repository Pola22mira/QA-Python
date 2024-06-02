from time import sleep
from selenium.webdriver.common.by import By

class Calculator:
    
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()
        
        
    def set_delay(self, delay):
        input_delay = self.driver.find_element(By.ID, 'delay')
        input_delay.clear()
        input_delay.send_keys(delay)        
        
        
    def click_values(self, first_num, sing, second_num):
        self.driver.find_element(By.XPATH, f'//div[@class="keys"]/span[text()="{first_num}"]').click()         
        self.driver.find_element(By.XPATH, f'//div[@class="keys"]/span[text()="{sing}"]').click()        
        self.driver.find_element(By.XPATH, f'//div[@class="keys"]/span[text()="{second_num}"]').click()        
        self.driver.find_element(By.XPATH, '//div[@class="keys"]/span[text()="="]').click()
    
        
    def waiting(self, delay):
        sleep(int(delay))
        
        
    def get_value(self):
        value = self.driver.find_element(By.CSS_SELECTOR, 'div.screen').text
        return value
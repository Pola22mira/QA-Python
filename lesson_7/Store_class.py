from selenium.webdriver.common.by import By

class Store:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()
        
        
    def authorization(self, user, password):
        self.driver.find_element(By.ID, 'user-name').clear()
        self.driver.find_element(By.ID, 'user-name').send_keys(user)
        self.driver.find_element(By.ID, 'password').clear()
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.ID, 'login-button').click()        
        
        
    def add_goods(self, item1, item2, item3):
        item1 = self.driver.find_element(By.XPATH, f'//div[text()="{item1}"]/ancestor::div[@class="inventory_item_description"]')
        item1.find_element(By.TAG_NAME, 'button').click()

        item2 = self.driver.find_element(By.XPATH, f'//div[text()="{item2}"]/ancestor::div[@class="inventory_item_description"]')
        item2.find_element(By.TAG_NAME, 'button').click()

        item3 = self.driver.find_element(By.XPATH, f'//div[text()="{item3}"]/ancestor::div[@class="inventory_item_description"]')
        item3.find_element(By.TAG_NAME, 'button').click()
        
                
    def get_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()
        
        
    def click_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, '#checkout').click()
        
        
    def fill_form(self):
        self.driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys("Polina")
        self.driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys("Novikova")
        self.driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, '#continue').click() 
          
        
    def get_sum(self):
        sum = self.driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
        return sum 
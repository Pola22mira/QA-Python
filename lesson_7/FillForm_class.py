from selenium.webdriver.common.by import By

class FillForm:
    
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()
        
    def fill_fields(self, first_name, last_name, address, email, phone, city, country, job_position, company):
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys(address)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys(city)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys(country)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys(job_position)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys(company)

    def zip_code_clear(self):
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').clear()

    def submit_click(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    def zip_code_field_color(self):
        zip_code_color = self.driver.find_element(By.CSS_SELECTOR, '#zip-code')
        return zip_code_color.get_attribute("class") 
    
    def other_fields_color(self):
        other_fields = ['#first-name', '#last-name', '#address', '#e-mail', '#phone', '#city', '#country', '#job-position', '#company']
        colors = [(self.driver.find_element(By.CSS_SELECTOR, field).get_attribute("class")) for field in other_fields]
        return colors   
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

# открыть страницу
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# пять раз кликнуть на кнопку Add Element
button = driver.find_element(By.CSS_SELECTOR, '#content > div > button')  

for i in range(1,6):
    if i <= 6:
        button.send_keys(Keys.RETURN)
        print('нажато', i)

# собрать со страницы список кнопок Delete
buttons_delete = driver.find_elements(By.CSS_SELECTOR, "button.added-manually")

#вывести на экран размер списка
print(len(buttons_delete))

sleep(10)
driver.quit()
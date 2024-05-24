from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Store_class import Store

def test_store():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    store = Store(browser)
    store.authorization("standard_user", "secret_sauce")
    store.add_goods("Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie")
    store.get_cart()           
    store.click_checkout()    
    store.fill_form()
    assert '$58.29' in store.get_sum()
    
    browser.quit()    
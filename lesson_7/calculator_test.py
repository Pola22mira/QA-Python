from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Calculator_class import Calculator


def test_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    calculator = Calculator(browser)
    delay = "10"
    calculator.set_delay(delay)
    calculator.click_values('7', '+', '8')
    calculator.waiting(delay)
    result_as_is = calculator.get_value()
    result_to_be = "15"
    assert result_as_is == result_to_be
    
    browser.quit() 
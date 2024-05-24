from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from FillForm_class import FillForm

def test_colour_fields_form():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    fill_form = FillForm(browser)
    fill_form.fill_fields("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "Москва", "Россия", "QA", "SkyPro")
    fill_form.zip_code_clear()    
    fill_form.submit_click()
    
    zip_code_color = fill_form.zip_code_field_color()
    assert zip_code_color == "alert py-2 alert-danger"
    
    other_fields_colors = fill_form.other_fields_color()
    for color in other_fields_colors:
        assert color == "alert py-2 alert-success"
       
    browser.quit()
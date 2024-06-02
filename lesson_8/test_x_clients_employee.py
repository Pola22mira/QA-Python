import requests
import json
from EmployeeApi import EmployeeApi

api = EmployeeApi("https://x-clients-be.onrender.com")


def test_get_employee_list():
    # создать новую компанию
    name = "Company Polla"    
    result = api.create_company(name=name)
    company_id = result["id"]
    # добавить работника
    first_name = "Иоанн"
    middle_name = "Васильевич"
    last_name = "Нееепрофессиональный"
    email = "string@bk.ru"
    api.add_employee(company_id, first_name, middle_name, last_name, email)    
    # получить список сотрудников    
    body = api.get_employee_list(company_id)
    assert body.status_code == 200 
    assert body.json()[0]["firstName"] == "Иоанн"
    assert body.json()[0]["middleName"] == "Васильевич"
    assert body.json()[0]["lastName"] == "Нееепрофессиональный"
    assert len(body.json()[0]) == 12
    
def test_get_employee_list_empty():
    # создать новую компанию
    name = "Polla"
    result = api.create_company(name=name)
    company_id = result["id"]    
    # получить список сотрудников    
    body = api.get_employee_list(company_id)
    assert body.status_code == 200 
    assert body.json() == [] 
        
def test_add_employee():
    # создать новую компанию
    name = "Polla"
    result = api.create_company(name=name)
    new_id = result["id"]
    # добавить работника
    first_name = "Иоанн"
    middle_name = "Васильевич"
    last_name = "Нееепрофессиональный"
    email = "string@bk.ru"
    body = api.add_employee(new_id, first_name, middle_name, last_name, email)  
    assert len(body) == 1
    assert type(body["id"]) == int
    
def test_add_employee_with_null_fields():
    # создать новую компанию
    name = "Polla"
    result = api.create_company(name=name)
    new_id = result["id"]
    # добавить работника
    id = None
    company_id = new_id 
    first_name = "Иоанн"
    middle_name = "Васильевич"
    last_name = "Нееепрофессиональный"
    email = "string@bk.ru" 
    url = None
    phone = "+79661234567" 
    birthdate  = None 
    isActive = None    
    added = api.add_employee_check_fields(id, company_id, first_name, middle_name, last_name, email, url, phone, birthdate, isActive)
    employee_id = added["id"]
    # запросить сотрудника по id
    body = api.get_employee_by_id(employee_id)    
    assert body["firstName"] == "Иоанн"
    assert body["middleName"] == "Васильевич"
    assert body["lastName"] == "Нееепрофессиональный"
    assert len(body) == 12

    
def test_get_employee_by_id():
    # создать новую компанию
    name = "Polla-19"    
    result = api.create_company(name=name)
    company_id = result["id"]
    # добавить сотрудника
    first_name = "Иоанн"
    middle_name = "Васильевич"
    last_name = "Нееепрофессиональный"
    email = "ioann@bk.ru"
    added = api.add_employee(company_id, first_name, middle_name, last_name, email)   
    employee_id = added["id"]
    # запросить сотрудника по id
    body = api.get_employee_by_id(employee_id)        
    # проверки
    assert body["firstName"] == "Иоанн"
    assert body["middleName"] == "Васильевич"
    assert body["lastName"] == "Нееепрофессиональный"
    assert len(body) == 12    
    
def test_change_employee_data():
    # создать новую компанию
    name = "Вторая компания Polla"    
    result = api.create_company(name=name)
    company_id = result["id"]
    # добавить работника
    first_name = "Иоанн"
    middle_name = "Васильевич"
    last_name = "Нееепрофессиональный"
    email = "ioann@bk.ru"
    added = api.add_employee(company_id, first_name, middle_name, last_name, email)  
    employee_id = added["id"]
    # получить сотрудника по id
    body = api.get_employee_by_id(employee_id)        
    # проверки
    assert body["lastName"] == "Нееепрофессиональный"    
    # внести изменения в информацию о сотруднике
    new_last_name = "Московский"
    new_email = "moscow@bk.ru"
    api.change_employee_data(employee_id, new_last_name, new_email)   
    # снова получить сотрудника по id
    body = api.get_employee_by_id(employee_id)       
    assert body["lastName"] == new_last_name
    assert body["email"] == new_email
    
def test_change_employee_data_check_fields():
    # создать новую компанию
    name = "Вторая компания Polla"    
    result = api.create_company(name=name)
    company_id = result["id"]
    # добавить работника
    first_name = "Иоанн"
    middle_name = "Васильевич"
    last_name = "Нееепрофессиональный"
    email = "ioann@bk.ru"
    added = api.add_employee(company_id, first_name, middle_name, last_name, email)  
    employee_id = added["id"]
    # внести изменения в информацию о сотруднике
    new_last_name = "Московский"
    new_email = "moscow@bk.ru"    
    new_url = None
    new_phone = None
    isActive = None
    changed = api.change_employee_data_check_fields(employee_id, new_last_name, new_email, new_url, new_phone, isActive)          
    assert changed["id"] == employee_id
    assert len(changed) == 4    
from EmployeeApi import EmployeeApi
from EmployeeTable import EmployeeTable

api = EmployeeApi("https://x-clients-be.onrender.com")
db = EmployeeTable("postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")


def test_get_employee_list_by_company_id():      
    # создать компанию и получить ее id
    company_id = db.create_company_and_get_id()
    # добавить сотрудников
    first_name = 'Иванушка'
    last_name = 'Коровкин'
    phone = '+76661236587'    
    db.add_employee(first_name, last_name, phone, company_id)
    first_name = 'Николай'
    last_name = 'Зорькин'
    phone = '+76661236588'   
    db.add_employee(first_name, last_name, phone, company_id)  
    api_result = api.get_company_employees(company_id)        
    db_result =  db.get_company_employees(company_id) 
    # удалить сотрудников и компанию 
    db.delete_employee(company_id)
    db.delete_company(company_id)     
    assert len(api_result) == len(db_result) == 2    
    for employee in db_result:
        assert employee["company_id"] == company_id   
        
    
def test_get_one_employee_by_employee_id():     
    # создать компанию и получить ее id
    company_id = db.create_company_and_get_id()
    # добавить сотрудника
    first_name = 'Ив'
    last_name = 'Коровин'     
    employee = api.add_employee(first_name, last_name, company_id)
    employee_id = employee["id"]    
    result = api.get_employee_by_id(employee_id)    
    # удалить сотрудников и компанию 
    db.delete_employee(company_id)
    db.delete_company(company_id)     
    assert result["id"] == employee_id 
    assert result["firstName"] == first_name
    assert result["lastName"] == last_name
    assert result["companyId"] == company_id   
    

def test_add_employee():   
    # создать компанию и получить ее id
    company_id = db.create_company_and_get_id()
    # добавить сотрудника
    first_name = "Иоанн"
    last_name = "Нееепрофессиональный"
    body = api.add_employee(first_name, last_name, company_id)
    added = db.get_company_employees(company_id)  
    # удалить сотрудников и компанию 
    db.delete_employee(company_id)
    db.delete_company(company_id)    
    assert len(body) == 1
    assert type(body["id"]) == int
    assert added[0]["first_name"] == first_name
    assert added[0]["last_name"] == last_name
    assert added[0]["company_id"] == company_id

    
def test_edit_employee():
    # создать компанию и получить ее id
    company_id = db.create_company_and_get_id()
    # добавить сотрудника
    first_name = "Иоанн"
    last_name = "Нееепрофессиональный"
    employee_id = api.add_employee(first_name, last_name, company_id)["id"]    
    # внести изменения в информацию о сотруднике
    new_last_name = "Московский"
    new_email = "moscow@bk.ru"
    edited = api.edit_employee(employee_id, new_last_name, new_email)   
    # получить сотрудника по id
    got = api.get_employee_by_id(employee_id)     
    # удалить сотрудников и компанию 
    db.delete_employee(company_id)
    db.delete_company(company_id)  
    assert edited["id"] == employee_id  
    assert edited["email"] == new_email       
    assert got["lastName"] == new_last_name
    assert got["email"] == new_email    

    
# def test_delete_employee_my():    
#     db.delete_employee(6875)  
    
# def test_delete_company_by_id():
#     db.delete_company(6875)
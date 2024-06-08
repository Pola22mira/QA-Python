import requests


class EmployeeApi:
    
    def __init__(self, url):
        self.url = url
    
    def get_company_employees(self, id):
        resp = requests.get(self.url+'/employee?company='+str(id))
        return resp.json()  
       
    def get_token(self, user='bloom', password='fire-fairy'):
        creds = {
            "username": user,
            "password": password
        } 
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]     
    
    def add_employee(self,  first_name, last_name, company_id):
        employee = {
        "id": 0,
        "firstName": first_name,
        "lastName": last_name,
        "middleName": "",
        "companyId": company_id,
        "email": "email@bk.ru",
        "url": "string",
        "phone": "+79660312345",
        "birthdate": "2024-06-02T12:33:33.734Z",
        "isActive": True
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee', headers=my_headers, json=employee)  
        return resp.json()    
    
    def get_employee_by_id(self, employee_id):
        resp = requests.get(self.url + '/employee/'+ str(employee_id))  
        return resp.json()
    
    def edit_employee(self, employee_id, new_last_name, new_email):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        new_data = {
        "lastName": new_last_name,
        "email": new_email        
        }                
        resp = requests.patch(self.url + '/employee/'+ str(employee_id), headers=my_headers, json=new_data)  
        return resp.json()  
    
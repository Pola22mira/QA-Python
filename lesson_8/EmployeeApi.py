import requests
import json


class EmployeeApi:
    
    def __init__(self, url):
        self.url = url
    
    def get_employee_list(self, id):
        resp = requests.get(self.url+'/employee?company='+str(id))
        return resp  
       
    def get_token(self, user='bloom', password='fire-fairy'):
        creds = {
            "username": user,
            "password": password
        } 
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]  
    
    def create_company(self, name, description=""):
        company = {
            "name": name,
            "description": description
        }       
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/company', headers=my_headers, json=company)  
        return resp.json()       
    
    def add_employee(self, company_id, first_name, middle_name, last_name, email):
        employee = {
        "id": 0,
        "firstName": first_name,
        "lastName": last_name,
        "middleName": middle_name,
        "companyId": company_id,
        "email": email,
        "url": "string",
        "phone": "string",
        "birthdate": "2024-06-02T12:33:33.734Z",
        "isActive": True
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee', headers=my_headers, json=employee)  
        return resp.json()
    
    def add_employee_check_fields(self, id, company_id, first_name, middle_name, last_name, email, url, phone, birthdate, isActive):
        employee = {
        "id": id,
        "firstName": first_name,
        "lastName": last_name,
        "middleName": middle_name,
        "companyId": company_id,
        "email": email,
        "url": url,
        "phone": phone,
        "birthdate": birthdate,
        "isActive": isActive
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee', headers=my_headers, json=employee)  
        return resp.json()        
    
    def get_employee_by_id(self, employee_id):
        resp = requests.get(self.url + '/employee/'+ str(employee_id))  
        return resp.json()
    
    def change_employee_data(self, employee_id, new_last_name, new_email):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        new_data = {
        "lastName": new_last_name,
        "email": new_email        
        }                
        resp = requests.patch(self.url + '/employee/'+ str(employee_id), headers=my_headers, json=new_data)  
        return resp.json()
    
    def change_employee_data_check_fields(self, employee_id, new_last_name, new_email, new_url, new_phone, isActive):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        new_data = {        
        "lastName": new_last_name,
        "email": new_email,
        "url": new_url,
        "phone": new_phone,
        "isActive": isActive
        }                     
        resp = requests.patch(self.url + '/employee/'+ str(employee_id), headers=my_headers, json=new_data)  
        return resp.json()        
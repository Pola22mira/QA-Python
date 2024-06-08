from sqlalchemy import create_engine
from sqlalchemy.sql import text
import random

class EmployeeTable:
    __scripts = {
        "select company employees": text("select * from employee where \"company_id\" = :id"),    
        "delete company by id": text("delete from company where id = :id_to_delete"),
        "insert new company": text("insert into company (\"name\") values (:new_name)"),
        "get max id": "select MAX(id) from company",
        "insert new employee": text("insert into employee (\"first_name\", \"last_name\", \"phone\", \"company_id\") values (:first_name, :last_name, :phone, :company_id)"),
        "delete employee by company id": text("delete from employee where \"company_id\" = :id")
    }
    
    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)
    
    def generate_random_company_name(self):
        self.names = ['Компания-10 Pola', 'Компания-11 Pola', 'Компания-12 Pola', 'Компания-13 Pola', 'Компания-14 Pola', 'Компания-15 Pola']
        return random.choice(self.names)  
    
    def create_company_and_get_id(self):
        name = self.generate_random_company_name()
        self.__db.execute(self.__scripts["insert new company"], new_name = name)
        max_id = self.__db.execute(self.__scripts["get max id"]).fetchall()[0][0] 
        return max_id 
    
    def get_company_employees(self, company_id):
        return self.__db.execute(self.__scripts["select company employees"], id = company_id).fetchall()    
    
    def delete_company(self, id):
        self.__db.execute(self.__scripts["delete company by id"], id_to_delete = id)  
        
    def add_employee(self, my_first_name, my_last_name, my_phone, my_company_id):
        return self.__db.execute(self.__scripts["insert new employee"], first_name = my_first_name, last_name = my_last_name, phone = my_phone, company_id = my_company_id) 
    
    def delete_employee(self, company_id):
        self.__db.execute(self.__scripts["delete employee by company id"], id = company_id)
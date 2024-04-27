class User:

    def __init__(self, first_name, last_name):
        print("я создался")
        self.first_name = first_name
        self.last_name = last_name  

    def sayFirstName(self):
        print('Моё имя: ', self.first_name)  
    
    def sayLastName(self):
        print('Моя фaмилия: ', self.last_name) 
        
    def sayFullName(self):
        print('Мои имя и фамилия: ', self.first_name, self.last_name)   
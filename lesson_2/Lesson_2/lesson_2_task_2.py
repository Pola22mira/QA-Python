'''1) Создайте функцию is_year_leap, принимающую один аргумент — год (число) — и возвращающую 
True, если год високосный, и False — если иначе. 
   2) В этом же файле напишите код, который вызывает функцию и передает в нее год (выберите любой).
Результат вызова функции должен сохраняться в переменную.Выведите в консоль ответ: 
год <номер года>: <True|False>'''

# Часть первая:
def is_year_leap ():
    year = int(input("Введите год: "))
    if (year % 4 ==0):
       print ('True')
    else:
        print ('False') 


is_year_leap ()


# Часть вторая:  
def year(a):
    if (a % 4 ==0):
        print ("год ", a,": True", sep="") # или: print (f"год {a}: True")
        return a, True
    else:
        print ("год ", a,": False", sep="") # или: print (f"год {a}: False")
        return a, False 

    
year(2025)
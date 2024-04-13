'''Напишите функцию month_to_season(), которая принимает один аргумент — номер месяца — 
и возвращает название сезона, к которому относится этот месяц. Например, передаем 2, 
на выходе получаем «Зима».'''

m = int(input("Введите номер месяца: "))

def month_to_season():
    if m in range(1,3):
        print("Зима")
    elif m == 12: 
        print("Зима")
    elif m in range(3,6): 
        print("Весна")
    elif m in range(6,9): 
        print("Лето")
    else: 
        print("Осень")

month_to_season()






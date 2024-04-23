'''Напишите функцию fizz_buzz, которая принимает один аргумент — n (число).
Функция должна печатать числа от 1 до n. При этом: если число делится на 3, печатать 
Fizz; если число делится на 5, печатать Buzz; если число делится на 3 и на 5, печатать 
FizzBuzz.'''

n = 17
def fizz_buzz ():
    for x in range(1,n+1):
        if (x % 3==0) and (x % 5 ==0): 
            print("FizzBuzz")
        elif(x % 3==0): 
            print("Fizz")
        elif(x % 5 ==0):
            print("Buzz")
        else:
            print(x)
        
fizz_buzz ()
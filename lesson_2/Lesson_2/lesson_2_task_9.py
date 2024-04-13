'''Создайте переменные: var_1 = 37, var_2 = 99 Напишите код, который 
меняет значения переменных местами (var_1  должен быть равен 99, а var_2 —  37). 
Выведите обновленные переменные на экран. '''

var_1 = 37
var_2 = 99
var_1 = 99
var_2 = 37
print("var_1 = ", var_1, ",  var_2 = ", var_2, sep="")


# или:
var_1 = 37
var_2 = 99
s = var_1 + var_2
var_1 = s - var_1
var_2 = s - var_2
print("var_1 = ", var_1, ",  var_2 = ", var_2, sep="")

# или: 
var_1 = 37
var_2 = 99
х = int

x = var_1
var_1 = var_2
var_2 = x
print("var_1 = ", var_1, ",  var_2 = ", var_2, sep="")             
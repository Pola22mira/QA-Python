'''Дан список lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20].
Выведите сумму всех элементов списка.'''

lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
total = sum(lst)
print(total)

# или:
total = 0
for num in lst:
    total += num
print(total)
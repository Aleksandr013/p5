# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

a = int(input('Введите число А: '))
b = int(input('Введите число B: '))
def Sum(a, b):
    if b == 0: return a 
    else: return 1 + Sum(a, b - 1)
print(f"{a} + {b} = {Sum(a, b)}")
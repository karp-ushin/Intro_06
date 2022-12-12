# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from math import ceil
lst = list(map(int, input("Enter list elements separated by comma").replace(" ", "").split(",")))
n = len(lst)
print([lst[i]*lst[n-1-i] for i in range(ceil(n/2))])

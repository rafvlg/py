# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint
n = int(input("Введите целое число: ")) #Вводим число
i = 3
p = 3
a = [randint(1, 1000) for i in range(10) for p in range(10)] # создаем массив
print(f"Список: {a}") # Выводим список/массив
print(f"Самое близкое по виличине число:{min(a, key = lambda c:abs(c-n))}") #выводим количество вхождений числа X в список A
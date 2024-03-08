import random

# 1. Заполнить случайными элементами одномерный массив A, состоящий из 10 целочисленных элементов.
A = [random.randint(-100, 100) for _ in range(10)]

# 2. Вывести в консоль минимальный по модулю элемент.
min_abs_element = A[0]
for num in A:
    if abs(num) < abs(min_abs_element):
        min_abs_element = num

print("Минимальный по модулю элемент массива A:", min_abs_element)
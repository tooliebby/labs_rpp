import random

# 1. Заполнить случайными элементами одномерный массив A, состоящий из 10 целочисленных элементов.
A = [random.randint(-100, 100) for _ in range(10)]

# 3. Вывести массив в консоль в обратном порядке.
print("Массив A в обратном порядке:", end=' ')
for i in range(len(A)-1, -1, -1):
    print(A[i], end=' ')
print()
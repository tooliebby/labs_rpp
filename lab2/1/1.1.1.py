#1.1.1
#Считать с клавиатуры три произвольных числа, найти минимальное среди них и вывести на экран.

a = float(input("Введите число:"))
b = float(input("Введите число:"))
c = float(input("Введите число:"))

min = min(a,b,c)

print("Минимальное число",min)

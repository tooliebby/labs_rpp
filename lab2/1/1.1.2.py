#1.1.2
#Считать с клавиатуры три произвольных числа, вывести в консоль те числа, которые попадают в интервал [1, 50].

a = int(input("Введите число:"))
b = int(input("Введите число:"))
c = int(input("Введите число:"))

if 1 < a <=50:
    print("Число:",a,"входит в интервал от 1 до 50")
if 1 < b <=50:
    print("Число:",b,"входит в интервал от 1 до 50")
if 1 < c <=50:
    print("Число:",c,"входит в интервал от 1 до 50")
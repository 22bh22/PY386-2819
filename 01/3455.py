﻿#Задача №3455. Гипотенуза
#https://informatics.msk.ru/mod/statements/view.php?id=3309)#1
#Дано два числа a и b. Выведите гипотенузу треугольника с заданными катетами.
#Входные данные
#Вводятся два целых положительных числа, не превышающих 1000.
#Выходные данные
#Выведите ответ на задачу с точностью 10 знаков после запятой
a=int(input("Введите длину первого катета\n"))
b=int(input("Введите длину второго катета\n"))
c=(a**2+b**2)**0.5
print(f"Гипотенуза прямоугольного треугольника со сторонами {a} и {b} составляет:\n%.10f"%c)
x=input()
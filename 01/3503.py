﻿#Задача №3503. Знак числа
#https://informatics.msk.ru/mod/statements/view3.php?id=3380&chapterid=3503#1
#В математике функция sign(x) (знак числа) определена так:
#sign(x) = 1,   если x > 0,
#sign(x) = -1, если x < 0,
#sign(x) = 0,   если x = 0.
#Для данного числа x выведите значение sign(x).
#Входные данные
#Вводится одно целое число.
#Выходные данные
#Выведите ответ на задачу.
#Примечание
#Эту задачу желательно решить с использованием каскадных инструкций if... elif... else.
x=int(input("Введите целое положительное или отрицательное число:\n"))
if x>0:
	print("1")
elif x<0:
	print("-1")
else:
	print("0")
x=input()
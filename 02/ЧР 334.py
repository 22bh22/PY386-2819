#Задача №334. Остаток
#https://informatics.msk.ru/mod/statements/view3.php?id=280&chapterid=334#1
#Ввод и вывод данных производятся через стандартные потоки ввода-вывода. Для хранения целых чисел необходимо использовать 4-байтовые переменные (например, тип longint в Free Pascal).
#Входные данные
#Вводятся 4 числа: a, b, c и d. 
#Выходные данные
#Выведите все числа на отрезке от a до b, дающие остаток c при делении на d. Если таких чисел не существует, то ничего выводить не нужно.

print("Требуется ввести целых 4 числа!")
a=int(input("Введите целое число (начало интервала): "))
b=int(input("Введите целое число (конец интервала): "))
c=int(input("Введите целое число (нужный остаток от деления): "))
d=int(input("Введите целое число (делитель): "))

if a>b:
	a,b=b,a
s=""
#my_list=list()
for i in range(a,b+1):
	if i % d == c:
		#my_list.append(i)
#		if i == 0:
#			s=str(i)
#		else:
			s+=" "+str(i)
if len(s)>1:
	print("Числа между ", a, " и ", b, ", дающие при делении на ", d, " остаток ", c,": ",s[1:],".",sep="")
input()
#Задача №3508. Тестирующая система
#https://informatics.msk.ru/mod/statements/view3.php?id=3380&chapterid=3508#1
#Денис Павлович задал школьникам задачу: “Если данное четырехзначное число является симметричным,
#выведите 1, иначе выведите любое другое целое число”. 
#Для проверки Денис Павлович использует заранее подготовленный набор тестов и правильных ответов к ним.
#Ире кажется, что она решила эту задачу, но тестирующая система Ejudge почему-то не принимает ее решение.
#Ира думает, что это происходит оттого, что она выводит не то любое другое число, 
#которое записано в ответах у Дениса Павловича.

#Напишите программу, которая по ответу Дениса Павловича
#и по ответу Иры определяет, верно ли Ира решила задачу.
#
#Входные данные
#Программа получает на вход два числа: ответ Дениса Павловича и ответ Иры.
#
#Выходные данные
#Программа должна вывести YES, если Ира дала верный ответ и NO в противном случае.
s = "NO"
#xDP = 1
#xi = 11
xDP = int(input("Введите ответ Дениса Павловича: "))
xi = int(input("Введите ответ Иры: "))
if (xi == 1 and xDP == 1) or (xi != 1 and xDP != 1):
	s = "YES"
print(s)
input("Для завершения нажмите любую клавишу...")
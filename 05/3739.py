#Задача №3739. Первое и последнее вхождение
#https://informatics.msk.ru/mod/statements/view3.php?id=3863&chapterid=3739#1
#Дана строка. Если в этой строке буква f встречается только один раз, выведите её индекс.
#Если она встречается два и более раз, выведите индекс её первого и последнего появления.
#Если буква f в данной строке не встречается, ничего не выводите.
#
#При решении этой задачи нельзя использовать метод count и циклы.
#
#Входные данные
#Вводится строка.
#
#Выходные данные
#Выведите ответ на задачу.

import re
s = "20Tf2fgdfgdfgdfgdfgdfgdfgdfgdfgd;fgl,dfl;g,dlf,gdfm,gkldfOBO"
#s = "01f2"
#s = input("Введите текстовую строку, содержащую или несодержащую буквы f: ")
result = s.find("f")
if result > -1:
	if result == len(s) - s[::-1].find("f") - 1:
		print(result + 1)
	else:
		print(result + 1, len(s) - s[::-1].find("f"))

input("Для завершения нажмите любую клавишу...")
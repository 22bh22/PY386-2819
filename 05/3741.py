#Задача №3741. Удаление фрагмента
#https://informatics.msk.ru/mod/statements/view3.php?id=3863&chapterid=3741#1
#Дана строка, в которой буква h встречается минимум два раза.
#Удалите из этой строки первое и последнее вхождение буквы h, а также все символы, находящиеся между ними.
#
#Входные данные
#Вводится строка.
#
#Выходные данные
#Выведите ответ на задачу.

import re
s = "20Thf2fgdfgdfgdfgdfgdfgdfgdfgdfgd;fgl,dfl;g,dlf,gdfm,gkldfhOBO"
#s = input("Введите текстовую строку, содержащую хотя бы 2 буквы h: ")
pattern = re.compile("[h].*[h]")
#result = re.sub(r"India", "the World", "AV is largest Analytics community of India")
result = re.sub(pattern, "", s)
print(result)

input("Для завершения нажмите любую клавишу...")
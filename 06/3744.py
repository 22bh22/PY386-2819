#Задача №3744. Замена подстроки
#https://informatics.msk.ru/mod/statements/view3.php?id=3863&chapterid=3744#1
#Дана строка. Замените в этой строке все цифры 1 на слово one.
#
#Входные данные
#Вводится строка.
#
#Выходные данные
#Выведите ответ на задачу.
s = "I\'m the chosen 1"
#s = (input("Введите текстовую строку, содержащую цифры 1: ")
s = s.replace("1", "one")
print(s)
input("Для завершения нажмите любую клавишу...")
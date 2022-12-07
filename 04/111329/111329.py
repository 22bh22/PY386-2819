#Задача №111329. Построчное обращение
#https://informatics.msk.ru/mod/statements/view3.php?id=5763&chapterid=111329#1
#Выведите все строки данного файла в обратном порядке.
#Для этого считайте список всех строк при помощи метода readlines().
#Последняя строка входного файла обязательно заканчивается символом '\n'.

import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "input_111329.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as file:
	s=file.readlines()
	print(s[::-1])
input("Для завершения нажмите любую клавишу...")
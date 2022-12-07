#Задача №111328. Обращение строки
#https://informatics.msk.ru/mod/statements/view3.php?id=5763&chapterid=111328#1
#Во входном файле записана одна текстовая строка, возможно, содержащая пробелы.
#Выведите эту строку в обратном порядке.
#Строка во входном файле заканчивается символом конца строки '\n'.

import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "input_111328.txt"
abs_file_path = os.path.join(script_dir, rel_path)

#перевести текстовой список в числовой
#for i, elem in enumerate(my_array):
	#my_array[i]=int(elem)
s = ""

with open(abs_file_path) as file:
	for row in file:
		ss = row
		for i, elem in enumerate(row):
			s += row[-i]
print("Исходная строка - ", ss, ";", chr(10) ,"инвертированная строка - " ,s, ".", sep="")
input("Для завершения нажмите любую клавишу...")
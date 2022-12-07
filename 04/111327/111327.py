#Задача №111327. Числа могут быть где угодно
#https://informatics.msk.ru/mod/statements/view3.php?id=5763&chapterid=111327#1
#Во входном файле записано два целых числа, которые могут быть разделены пробелами и концами строк.
#Выведите в выходной файл их сумму.
#Указание. Считайте весь файл в строковую переменную при помощи метода read()
#и разбейте ее на части при помощи метода split().


import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "input_111327.txt"
abs_file_path = os.path.join(script_dir, rel_path)

#перевести текстовой список в числовой
#for i, elem in enumerate(my_array):
	#my_array[i]=int(elem)

my_sum = 0
x = 0
s = "Сложено число "
with open(abs_file_path) as file:
	for row in file:
		my_array=row.strip().split(" ")
		for i, elem in enumerate(my_array):
			if my_array[i].isdigit():
				my_sum += int(elem)
				x += 1
				if x == 1:
					s += str(my_array[i])
				elif x == 2:
					s += " с числом " + str(my_array[i])
if x ==2:
	print(s + ". Получилась сумма: " + str(my_sum) + ".")
input("Для завершения нажмите любую клавишу...")
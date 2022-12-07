#Задача №111335. Статистика по файлу
#https://informatics.msk.ru/mod/statements/view3.php?id=5763&chapterid=111335#1
#Дан файл. Определите сколько в нем букв (латинского алфавита), слов, строк.
#Выведите три найденных числа в формате, приведенном в примере.
#Для экономии памяти читайте файл посимвольно,
#то есть не сохраняя целиком в памяти файл или отдельные его строки.

import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "input_111335.txt"
abs_file_path = os.path.join(script_dir, rel_path)
s=" "
N_spaces = 0
N_rows = 1
N_letters = 0
with open(abs_file_path) as file:
	while s:
		s=file.read(1)
		#print (s)
		if s == chr(32):
			N_spaces += 1
		if s == chr(10):
			N_rows += 1
		if s.isalpha():
			N_letters += 1
print("Input file contains: ", chr(10), N_letters, " letters", chr(10), N_spaces + N_rows, " words", chr(10), N_rows, " lines", sep = "")
input("Для завершения нажмите любую клавишу...")
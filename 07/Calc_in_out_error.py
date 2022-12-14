#Создать консольную программу-калькулятор с интерактивным меню со следующими функциями:
#	Сложение двух чисел
#	Вычитание двух чисел
#	Умножение двух чисел
#	Деление двух чисел
#	Возведение первого числа в степень второго числа

#Переписать калькулятор таким образом, чтобы из него получился один пакет со структурой
#calc
#	__init__.py
#	operations.py
#	history.py
#В файле operations.py должны хранится все функции, которые занимаются высчитываением результата.
#В них не должно быть взаимодействия с пользователем через консоль (терминал).
#В файле history.py должна быть описана вся работа со списком истории и загрузкой и выгрузкой их
#в файл.

#Из файла calc.py импортируется одноимённая функция калькулятора
#Из файла input.txt берутся данные число1, число2, операнд
#Данные подставляются в функцию
#Результат вписывается в файл output.txt
#Из файла history.py берётся функция записи в лог
#...
#...пишется лог в файл log.txt

#12345678901234567890123456789012345678901234567890123456789012345678902
#11111111112222222222333333333344444444445555555555666666666677777777772

#from Next.hello import hello
#hello()


from Next.operations import calc
from Next.history import history
import os

#script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
#rel_path = "Next\input.txt"
#abs_file_path = os.path.join(script_dir, rel_path)
abs_file_path = input("Введите полный путь к файлу input.txt")
try:
	f_input = open(abs_file_path,'r')											#открыть файл input.txt для чтения
except FileNotFoundError:
	print("Не удалось обнаружить файл с входными данными по адресу:\n", abs_file_path, ".\n", sep = "")
else:
	rel_path = "Next\output.txt"
	abs_file_path = os.path.join(script_dir, rel_path)

	f_output = open(abs_file_path,'w', encoding="UTF-8")						#открыть файл output.txt для дозаписи
	my_count = 0
	rel_path = "Next\log.txt"
	abs_file_path = os.path.join(script_dir, rel_path)

	print("Эта программа обрабатывает данные из файла input.txt")
	print("Она сохраняет результат в файлах output.txt и log.txt")
	print("Все эти файлы хранятся в папке Next")
	for i in f_input:															#для каждой строки
		my_count += 1
		i = i.rstrip()															#удалить перенос строки и пробелы в конце (если есть)
		print("Из строки ", my_count, " файла input.txt получены данные:", i)
		x = i.split(",")														#разбить строку
		y = calc(x[0], x[1], x[2])												#обработать строку калькулятором
		s_output = str(y)														#результат приготовить к записи в файл output.txt
		print("В файл output.txt дописывается строка: ", s_output)
		f_output.write(s_output + chr(10))
		s_log = history(x[0], x[1], x[2], y, abs_file_path, my_count)			#обработать данные для перевода в человекочитаемый вид
		print("В файл лога дописывается: ", s_log)

	f_input.close() 					#закрыть файл input.txt
	f_output.close() 					#закрыть файл output.txt
input("Для завершения нажмите любую клавишу...")
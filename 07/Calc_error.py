#Создать консольную программу-калькулятор с интерактивным меню со следующими функциями:
#Сложение двух чисел
#Вычитание двух чисел
#Умножение двух чисел
#Деление двух чисел
#Возведение первого числа в степень второго числа
#
#def int_or_float(s):
#	try:
#		int(s)
#	except ValueError:
#		return float(s)
#	else:
#		return int(s)

from blackheartfunctions import int_or_float
		
print("Это программа-калькулятор")
my_list = ['*', '/', '^', '+', '-', '**']
while True:
	a = input("Введите число 1: ")
	try:
		a = int_or_float(a)
	except ValueError:
		print("Вы ввели некорректные данные: ", a, ".", sep = "")
		#print(f"Вы ввели некорректные данные: {a}")
	else:
		s = "Введите операнд " + str(my_list) + ":"
		c = input(s)
		if c in my_list:
			b = input("Введите число 2: ")
			try:
				b = int_or_float(b)
			except ValueError:
				#print(f'Вы ввели некорректные данные: {b}')
				print("Вы ввели некорректные данные: ", b, ".", sep = "")
			else:
				if c == "^" or c == "**":
					try:
						c = a ** b
					except OverflowError:
						print("Число", a, "при возведении в степень", b, \
						"выдаёт слишком большой результат (недоступен для отображения).\n", sep=None)
					else:
						print("Число", a, "было возведено в степень", b, "результат:", int_or_float(c), sep=None)
				elif c == "*":
					try:
						c = a * b
					except OverflowError:
						print("Число", a, "при умножении на", b, \
						"выдаёт слишком большой результат (недоступен для отображения).\n", sep=None)
					else:
						print("Число", a, "было умножено на", b, "результат:", int_or_float(c), sep=None)
				elif c == "/":
					try:
						c = a / b
					except OverflowError:
						print("Число", a, "при делении на", b, \
						"выдаёт слишком большой результат (недоступен для отображения).\n", sep=None)
					except ZeroDivisionError:
						print("Число", a, \
						"не может быть поделено на 0.\nРезультат недоступен для отображения.\n", sep=None)
					else:
						print("Число", a, "было разделено на", b, "результат:", int_or_float(c), sep=None)
				elif c == "+":
					try:
						c = a + b
					except OverflowError:
						print("Число", a, "при сложении с", b, \
						"выдаёт слишком большой результат (недоступен для отображения).\n", sep=None)
					else:
						print("Число", a, "было сложено с", b, "результат:", int_or_float(c), sep=None)
				elif c == "-":
					try:
						c = a - b
					except OverflowError:
						print("При вычитании числа", a, "от числа", b, \
						"выдаёт слишком большой результат (недоступен для отображения).\n", sep=None)
					else:
						print("Число", b, "было отнято от", a, "результат:", int_or_float(c), sep=None)
		else:
			#print(f'Вы ввели значение {c}, не являющееся допустимым операндом.\n')
			print("Вы ввели значение ", c, "не являющееся допустимым операндом.\n", sep = "")
	x = input("Для завершения напишите \"Выход\" или \"Exit\" и нажмите Ввод\\Enter.\n")
	if x == "Выход" or x == "выход" or x == "Exit" or x == "exit" or x == "Учше" or x == "учше" or x == "Ds[jl" or x == "ds[jl":
		break
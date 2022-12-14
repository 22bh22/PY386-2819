#В файле operations.py должны хранится все функции,
#которые занимаются высчитыванием результата.
#В них не должно быть взаимодействия с пользователем через консоль (терминал).
#12345678901234567890123456789012345678901234567890123456789012345678902
#11111111112222222222333333333344444444445555555555666666666677777777772
from blackheartfunctions import int_or_float
def calc(a, b, c):
	x = 0
	try:
		float(a)
	except ValueError:
		x = ("Произошла ошибка. Введены некорректные данные" + str(a), None, None)
		return x
	else:
		a = float(a)
		try:
			float(b)
		except ValueError:
			x = ("Произошла ошибка. Введены некорректные данные" + str(b), None, None)
			return x
		else:
			b = float(b)
			if c == "^" or c == "**":
				try:
					x = a ** b
				except OverflowError:
					print("Число", a, "при возведении в степень", b, \
					"выдаёт слишком большой результат (недоступен для отображения).\n", sep=None)
				else:
					print("Число", a, "было возведено в степень", b, "результат:", int_or_float(x), sep=None)
			elif c == "*":
				try:
					x = a * b
				except OverflowError:
					print("Число", a, "при умножении на", b, \
					"выдаёт слишком большой результат (недоступен для отображения).\n", sep=None)
				else:
					print("Число", a, "было умножено на", b, "результат:", int_or_float(x), sep=None)
			elif c == "/":
				try:
					x = a / b
				except OverflowError:
					print("Число", a, "при делении на", b, \
					"выдаёт слишком большой результат (недоступен для отображения).\n", sep=None)
				except ZeroDivisionError:
					print("Число", a, \
					"не может быть поделено на 0.\nРезультат недоступен для отображения.\n", sep=None)
				else:
					print("Число", a, "было разделено на", b, "результат:", int_or_float(x), sep=None)
			elif c == "+":
				try:
					x = a + b
				except OverflowError:
					print("Число", a, "при сложении с", b, \
					"выдаёт слишком большой результат (недоступен для отображения).\n", sep=None)
				else:
					print("Число", a, "было сложено с", b, "результат:", int_or_float(x), sep=None)
			elif c == "-":
				try:
					x = a - b
				except OverflowError:
					print("При вычитании числа", a, "от числа", b, \
					"выдаёт слишком большой результат (недоступен для отображения).\n", sep=None)
				else:
					print("Число", b, "было отнято от", a, "результат:", int_or_float(x), sep=None)
			return x
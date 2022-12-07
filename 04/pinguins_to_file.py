import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "pinguins_output.txt"
abs_file_path = os.path.join(script_dir, rel_path)

n=int(input("Введите число пингвинов: "))
#print("   _~_    \n  (o o)   \n /  V  \  \n/(  _  )\ \n  ^^ ^^   ")
if n>=0:
	s1="   _~_     "
	s2="  (o o)    "
	s3=" /  V  \   "
	s4="/(  _  )\  "
	s5="  ^^ ^^    "

	with open(abs_file_path, 'a', encoding="UTF-8") as file:
		file.write(s1*n + chr(10))
		file.write(s2*n + chr(10))
		file.write(s3*n + chr(10))
		file.write(s4*n + chr(10))
		file.write(s5*n + chr(10))
else:
	print("Ошибка! Введённое число ", n, " отрицательное. Выполнение программы остановлено.", sep="")
input("Для завершения нажмите любую клавишу...")
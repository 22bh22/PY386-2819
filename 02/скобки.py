s = "[{()}](){}"
s=str(input("Введите строку из открывающих и закрывающих скобок (обычных, квадратных и фигурных):\n"))
len1=len(s)
len2=0
x1 = chr(40)	#(
x2 = chr(41)	#)
y1=chr(91)		#[
y2=chr(93)		#]
z1=chr(123)		#{
z2=chr(125)		#}
s_temp=""
if s.count(x1)!=s.count(x2) or s.count(y1)!=s.count(y2) or s.count(z1)!=s.count(z2):
	print("Это строка - однозначно неправильная строка!")
else:
	for i in range(1,len(s)):
		if ord(s[i]) == 40 or ord(s[i]) == 41 or ord(s[i]) == 91 or ord(s[i]) == 93 or ord(s[i]) == 123 or ord(s[i]) == 125:
			s_temp+=s[i]
	while len1!=len2:
		len1=len(s)
		x_del = x1 + x2
		s=s.replace(x_del,"")
		x_del=y1+y2
		s=s.replace(x_del,"")
		x_del=z1+z2
		s=s.replace(x_del,"")
		len2=len(s)
	if len(s) == 0:
		print("Это строка - хорошая строка!")
	else:
		print("Это строка - неправильная строка!")
input()
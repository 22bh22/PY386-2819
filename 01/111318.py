#Задача №111318. Поиск подстроки
#https://informatics.msk.ru/mod/statements/view3.php?id=5761&chapterid=111318#1
#Даны две строки, возможно, содержащие пробелы. Выведите слово YES, если первая строка является подстрокой второй строки или слово NO в противном случае.
#Решение оформите в виде функции IsSubstring(Pattern, Source).
def Is_Sub_String(a, b):
	if a in b == True:
		Is_Sub_String=str("YES")
		
	else:
		Is_Sub_String=str("NO")
	return(Is_Sub_String)
a=str("hole in the ground")
b=str("In a hole in the ground there lived a hobbit.")
print(Is_Sub_String(a,b))
x=input()

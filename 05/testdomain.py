#Написать RE которая мэтчит адреса эл. почты только с конкретным именем домена (testdomain): 
#****@testdomain.com - valid
#****@anotherdomain.com - not valid

import re
s = "not valid"
inputText = "****@anotherdomain.com"
inputText = "****@testdomain.com"
pattern = re.compile("@testdomain.com")
if re.search(pattern, inputText):
	s = "valid"
print(s)
input("Для завершения нажмите любую клавишу...")
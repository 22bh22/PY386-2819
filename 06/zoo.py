#Дан код:
#
#class Animal:
#	def __init__(self, name, space):
#		self.name = name
#		self.space = space
#
#	def __str__(self):
#		return self.name
#
#
#class Cage:
#	def __init__(self, space):
#		self.space = space
#
#	def add_animal(self, animal: Animal) -> bool:
#		raise NotImplementedError
#
#	def get_animals(self) -> Iterable[Animal]:
#		raise NotImplementedError
#
#	def free_space(self) -> int:
#		raise NotImplementedError
#
#
#cage1 = Cage(300)
#cage2 = Cage(200)
#
#lion = Animal("Alex", 150)
#pinguin1 = Animal("Gunter", 20)
#pinguin2 = Animal("Ganter", 15)
#pinguin3 = Animal("Ginter", 25)
#begemoth = Animal("Gloria", 200)
#giraffe = Animal("Melvin", 110)
#zebra = Animal("Martin", 70)
#
#print(cage1.add_animal(lion))	  # True
#print(cage2.add_animal(pingiun1))  # True
#print(cage1.add_animal(pinguin2))  # True
#print(cage2.add_animal(pinguin3))  # True
#print(cage1.add_animal(begemoth))  # False
#print(cage2.add_animal(giraffe))   # True
#print(cage1.add_animal(zebra))	 # True
#print(cage1.free_space())		  # 65
#print(cage2.free_space())		  # 45
#print(cage1.get_animals())		 # ['Alex', 'Ganter', 'Martin']
#print(cage2.get_animals())		 # ['Gunter', 'Ginter', 'Melvin']
#
#
#Реализовать в классах методы, чтобы код, который идёт после определения классов работал так,
#как указано в комментариях.
#Менять можно только сами классы




class Animal:
	def __init__(self, name, space):
		self.name = name
		self.space = space

	def __str__(self):
		return self.name


class Cage:
	def __init__(self, space):
		self.space = space
		self.x = []

	def __repr__(self):
		return f"{self.space}"

	def add_animal(self, animal: Animal) -> bool:
		if (self.space >= animal.space):
			self.space -= animal.space
			self.x.append(animal.name)
			return True
		else:
			return False
	
	def get_animals(self):
		return self.x

	def show_free_space(self) -> int:
		return self.space

cage1 = Cage(300)
#print(cage1.show_free_space())
#pinguin1 = Animal("Gunter", 20)
#cage1.add_animal(pinguin1)
#print(cage1.show_free_space())
cage2 = Cage(200)

lion = Animal("Alex", 150)
pinguin1 = Animal("Gunter", 20)
pinguin2 = Animal("Ganter", 15)
pinguin3 = Animal("Ginter", 25)
begemoth = Animal("Gloria", 200)
giraffe = Animal("Melvin", 110)
zebra = Animal("Martin", 70)

print(cage1.add_animal(lion))	  # True
print(cage2.add_animal(pinguin1))  # True
print(cage1.add_animal(pinguin2))  # True
print(cage2.add_animal(pinguin3))  # True
print(cage1.add_animal(begemoth))  # False
print(cage2.add_animal(giraffe))   # True
print(cage1.add_animal(zebra))	 # True
print(cage1.show_free_space())		  # 65
print(cage2.show_free_space())		  # 45
print(cage1.get_animals())		 # ['Alex', 'Ganter', 'Martin']
print(cage2.get_animals())		 # ['Gunter', 'Ginter', 'Melvin']
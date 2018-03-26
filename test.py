class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog("Zac")
e = Dog("Tom")

a = [e,d]

for i in range(len(a)):
	print(a[i].name)

e.name = "name2"

for i in range(len(a)):
	print(a[i].name)